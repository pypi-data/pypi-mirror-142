import collections
import functools
import inspect
import typing

import attrs
import typing_extensions

import interactions
from . import context
from . import converters
from . import errors
from .utils import maybe_coroutine

__all__ = (
    "CommandParameter",
    "ArgsIterator",
    "MolterCommand",
    "message_command",
    "msg_command",
)

# 3.8+ compatibility
NoneType = type(None)

try:
    from types import UnionType

    UNION_TYPES = {typing.Union, UnionType}
except ImportError:  # 3.8-3.9
    UNION_TYPES = {typing.Union}


@attrs.define(slots=True)
class CommandParameter:
    """An object representing parameters in a command."""

    name: str = attrs.field(default=None)
    default: typing.Optional[typing.Any] = attrs.field(default=None)
    type: type = attrs.field(default=None)
    converters: typing.List[
        typing.Callable[[context.MolterContext, str], typing.Any]
    ] = attrs.field(factory=list)
    greedy: bool = attrs.field(default=False)
    union: bool = attrs.field(default=False)
    variable: bool = attrs.field(default=False)
    consume_rest: bool = attrs.field(default=False)

    @property
    def optional(self) -> bool:
        return self.default != interactions.MISSING


@attrs.define(slots=True)
class ArgsIterator:
    """
    An iterator over the arguments of a command.
    Has functions to control the iteration.
    """

    args: typing.Sequence[str] = attrs.field(converter=tuple)
    index: int = attrs.field(init=False, default=0)
    length: int = attrs.field(init=False, default=0)

    def __iter__(self):
        self.length = len(self.args)
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration

        result = self.args[self.index]
        self.index += 1
        return result

    def consume_rest(self):
        result = self.args[self.index - 1 :]
        self.index = self.length
        return result

    def back(self, count: int = 1):
        self.index -= count

    def reset(self):
        self.index = 0

    @property
    def finished(self):
        return self.index >= self.length


def _get_name(x: typing.Any):
    try:
        return x.__name__
    except AttributeError:
        return repr(x) if hasattr(x, "__origin__") else x.__class__.__name__


def _convert_to_bool(argument: str) -> bool:
    lowered = argument.lower()
    if lowered in {"yes", "y", "true", "t", "1", "enable", "on"}:
        return True
    elif lowered in {"no", "n", "false", "f", "0", "disable", "off"}:
        return False
    else:
        raise errors.BadArgument(f"{argument} is not a recognised boolean option.")


def _get_from_anno_type(anno: typing_extensions.Annotated, name):
    """
    Handles dealing with Annotated annotations, getting their
    (first and what should be only) type annotation.
    This allows correct type hinting with, say, Converters,
    for example.
    """
    # this is treated how it usually is during runtime
    # the first argument is ignored and the rest is treated as is

    args = typing_extensions.get_args(anno)[1:]
    if len(args) > 1:
        # we could treat this as a union, but id rather have a user
        # use an actual union type here
        # from what ive seen, multiple arguments for Annotated are
        # meant to be used to narrow down a type rather than
        # be used as a union anyways
        raise ValueError(
            f"{_get_name(anno)} for {name} has more than 2 arguments, which is"
            " unsupported."
        )

    return args[0]


def _get_converter(
    anno: type, name: str
) -> typing.Callable[[context.MolterContext, str], typing.Any]:  # type: ignore
    if typing_extensions.get_origin(anno) == typing_extensions.Annotated:
        anno = _get_from_anno_type(anno, name)

    if converter := converters.INTER_OBJECT_TO_CONVERTER.get(anno, None):
        return converter().convert

    elif inspect.isclass(anno) and issubclass(anno, converters.Converter):
        return anno().convert  # type: ignore

    elif hasattr(anno, "convert") and inspect.isfunction(anno.convert):  # type: ignore
        return anno.convert  # type: ignore

    elif typing_extensions.get_origin(anno) is typing.Literal:
        literals = typing_extensions.get_args(anno)
        return converters.LiteralConverter(literals).convert

    elif inspect.isfunction(anno):
        num_params = len(inspect.signature(anno).parameters.values())
        if num_params == 2:
            return lambda ctx, arg: anno(ctx, arg)
        elif num_params == 1:
            return lambda ctx, arg: anno(arg)
        elif num_params == 0:
            return lambda ctx, arg: anno()
        else:
            ValueError(
                f"{_get_name(anno)} for {name} has more than 2 arguments, which is"
                " unsupported."
            )

    elif anno == bool:
        return lambda ctx, arg: _convert_to_bool(arg)

    elif anno == inspect._empty:
        return lambda ctx, arg: str(arg)

    else:
        return lambda ctx, arg: anno(arg)


def _greedy_parse(greedy: converters.Greedy, param: inspect.Parameter):
    if param.kind in {param.KEYWORD_ONLY, param.VAR_POSITIONAL}:
        raise ValueError("Greedy[...] cannot be a variable or keyword-only argument.")

    arg = typing_extensions.get_args(greedy)[0]

    if typing_extensions.get_origin(arg) == typing_extensions.Annotated:
        arg = _get_from_anno_type(arg, param.name)

    if arg in {NoneType, str}:
        raise ValueError(f"Greedy[{_get_name(arg)}] is invalid.")

    if typing_extensions.get_origin(
        arg
    ) in UNION_TYPES and NoneType in typing_extensions.get_args(arg):
        raise ValueError(f"Greedy[{repr(arg)}] is invalid.")

    return arg


def _get_params(func: typing.Callable):
    cmd_params: list[CommandParameter] = []

    # we need to ignore parameters like self and ctx, so this is the easiest way
    # forgive me, but this is the only reliable way i can find out if the function...
    if "." in func.__qualname__:  # is part of a class
        callback = functools.partial(func, None, None)
    else:
        callback = functools.partial(func, None)

    params = inspect.signature(callback).parameters
    for name, param in params.items():
        cmd_param = CommandParameter()
        cmd_param.name = name
        cmd_param.default = (
            param.default if param.default is not param.empty else interactions.MISSING
        )

        cmd_param.type = anno = param.annotation

        if typing_extensions.get_origin(anno) == converters.Greedy:
            anno = _greedy_parse(anno, param)
            cmd_param.greedy = True

        if typing_extensions.get_origin(anno) in UNION_TYPES:
            cmd_param.union = True
            for arg in typing_extensions.get_args(anno):
                if arg != NoneType:
                    converter = _get_converter(arg, name)
                    cmd_param.converters.append(converter)
                elif not cmd_param.optional:  # d.py-like behavior
                    cmd_param.default = None
        else:
            converter = _get_converter(anno, name)
            cmd_param.converters.append(converter)

        if param.kind == param.KEYWORD_ONLY:
            cmd_param.consume_rest = True
            cmd_params.append(cmd_param)
            break
        elif param.kind == param.VAR_POSITIONAL:
            if cmd_param.optional:
                # there's a lot of parser ambiguities here, so i'd rather not
                raise ValueError(
                    "Variable arguments cannot have default values or be Optional."
                )

            cmd_param.variable = True
            cmd_params.append(cmd_param)
            break

        cmd_params.append(cmd_param)

    return cmd_params


async def _convert(param: CommandParameter, ctx: context.MolterContext, arg: str):
    converted = interactions.MISSING
    for converter in param.converters:
        try:
            converted = await maybe_coroutine(converter, ctx, arg)
            break
        except Exception as e:
            if not param.union and not param.optional:
                if isinstance(e, errors.BadArgument):
                    raise
                raise errors.BadArgument(str(e)) from e

    used_default = False
    if converted == interactions.MISSING:
        if param.optional:
            converted = param.default
            used_default = True
        else:
            union_types = typing_extensions.get_args(param.type)
            union_names = tuple(_get_name(t) for t in union_types)
            union_types_str = ", ".join(union_names[:-1]) + f", or {union_names[-1]}"
            raise errors.BadArgument(
                f'Could not convert "{arg}" into {union_types_str}.'
            )

    return converted, used_default


async def _greedy_convert(
    param: CommandParameter, ctx: context.MolterContext, args: ArgsIterator
):
    args.back()
    broke_off = False
    greedy_args = []

    for arg in args:
        try:
            greedy_arg, used_default = await _convert(param, ctx, arg)

            if used_default:
                raise errors.BadArgument()  # does it matter?

            greedy_args.append(greedy_arg)
        except errors.BadArgument:
            broke_off = True
            break

    if not greedy_args:
        if param.default:
            greedy_args = param.default  # im sorry, typehinters
        else:
            raise errors.BadArgument(
                f"Failed to find any arguments for {repr(param.type)}."
            )

    return greedy_args, broke_off


@attrs.define(
    slots=True,
    kw_only=True,
)
class MolterCommand:
    extension: typing.Any = attrs.field(default=None)
    "The extension this command belongs to."
    enabled: bool = attrs.field(default=True)
    "Whether this can be run at all."
    callback: typing.Callable[..., typing.Coroutine] = attrs.field(
        default=None,
    )
    "The coroutine to be called for this command"
    name: str = attrs.field()
    "The name of the command."

    params: typing.List[CommandParameter] = attrs.field()
    "The paramters of the command."
    aliases: typing.List[str] = attrs.field(
        factory=list,
    )
    "The list of aliases the command can be invoked under."
    hidden: bool = attrs.field(
        default=False,
    )
    "If `True`, the default help command does not show this in the help output."
    ignore_extra: bool = attrs.field(
        default=True,
    )
    """
    If `True`, ignores extraneous strings passed to a command if all its
    requirements are met (e.g. ?foo a b c when only expecting a and b).
    Otherwise, an error is raised. Defaults to True.
    """
    help: typing.Optional[str] = attrs.field()
    """The long help text for the command."""
    brief: typing.Optional[str] = attrs.field()
    "The short help text for the command."
    parent: typing.Optional["MolterCommand"] = attrs.field(
        default=None,
    )
    "The parent command, if applicable."
    command_dict: typing.Dict[str, "MolterCommand"] = attrs.field(
        factory=dict,
    )
    "A dict of a subcommand's name and the subcommand for this command."
    _usage: typing.Optional[str] = attrs.field(default=None)

    @params.default  # type: ignore
    def _fill_params(self):
        return _get_params(self.callback)

    def __attrs_post_init__(self) -> None:
        # we have to do this afterwards as these rely on the callback
        # and its own value, which is impossible to get with attrs
        # methods, i think

        if self.help:
            self.help = inspect.cleandoc(self.help)
        else:
            self.help = inspect.getdoc(self.callback)
            if isinstance(self.help, bytes):
                self.help = self.help.decode("utf-8")

        if self.brief is None:
            self.brief = self.help.splitlines()[0] if self.help is not None else None

    @property
    def usage(self) -> str:
        """
        A string displaying how the command can be used.
        If no string is set, it will default to the command's signature.
        Useful for help commands.
        """
        return self._usage or self.signature

    @usage.setter
    def usage(self, usage: str) -> None:
        self._usage = usage

    @property
    def qualified_name(self):
        """Returns the full qualified name of this command."""
        name_deq = collections.deque()
        command = self

        while command.parent is not None:
            name_deq.appendleft(command.name)
            command = command.parent

        name_deq.appendleft(command.name)
        return " ".join(name_deq)

    @property
    def all_commands(self):
        """Returns all unique subcommands underneath this command."""
        names = {c.name for c in self.command_dict.values()}
        return tuple(self.command_dict[n] for n in names)

    @property
    def signature(self) -> str:
        """Returns a POSIX-like signature useful for help command output."""
        if not self.params:
            return ""

        results = []

        for param in self.params:
            anno = param.type
            name = param.name

            if typing_extensions.get_origin(anno) == typing_extensions.Annotated:
                # message commands can only have two arguments in an annotation anyways
                anno = typing_extensions.get_args(anno)[1]

            if not param.greedy and param.union:
                union_args = typing_extensions.get_args(anno)
                if len(union_args) == 2 and param.optional:
                    anno = union_args[0]

            if typing_extensions.get_origin(anno) is typing.Literal:
                # it's better to list the values it can be than display the variable name itself
                name = "|".join(
                    f'"{v}"' if isinstance(v, str) else str(v)
                    for v in typing_extensions.get_args(anno)
                )

            # we need to do a lot of manipulations with the signature
            # string, so using a list as a string builder makes sense for performance
            result_builder: list[str] = []

            if param.optional and param.default is not None:
                # it would be weird making it look like name=None
                result_builder.append(f"{name}={param.default}")
            else:
                result_builder.append(name)

            if param.variable:
                # this is inside the brackets
                result_builder.append("...")

            # surround the result with brackets
            if param.optional:
                result_builder.insert(0, "[")
                result_builder.append("]")
            else:
                result_builder.insert(0, "<")
                result_builder.append(">")

            if param.greedy:
                # this is outside the brackets, making it differentiable from
                # a variable argument
                result_builder.append("...")

            results.append("".join(result_builder))

        return " ".join(results)

    def add_command(self, cmd: "MolterCommand"):
        """Adds a command as a subcommand to this command."""
        cmd.parent = self  # just so we know this is a subcommand

        cmd_names = frozenset(self.command_dict)
        if cmd.name in cmd_names:
            raise ValueError(
                "Duplicate Command! Multiple commands share the name/alias"
                f" `{self.qualified_name} {cmd.name}`"
            )
        self.command_dict[cmd.name] = cmd

        for alias in cmd.aliases:
            if alias in cmd_names:
                raise ValueError(
                    "Duplicate Command! Multiple commands share the name/alias"
                    f" `{self.qualified_name} {cmd.name}`"
                )
            self.command_dict[alias] = cmd

    def remove_command(self, name: str):
        """
        Removes a command as a subcommand from this command.
        If an alias is specified, only the alias will be removed.
        """
        command = self.command_dict.pop(name, None)

        if command is None or name in command.aliases:
            return

        for alias in command.aliases:
            self.command_dict.pop(alias, None)

    def get_command(self, name: str):
        """
        Gets a subcommand from this command. Can get subcommands of subcommands if needed.
        Args:
            name (`str`): The command to search for.
        Returns:
            `MolterCommand`: The command object, if found.
        """
        if " " not in name:
            return self.command_dict.get(name)

        names = name.split()
        if not names:
            return None

        cmd = self.command_dict.get(names[0])
        if not cmd or not cmd.command_dict:
            return cmd

        for name in names[1:]:
            try:
                cmd = cmd.command_dict[name]
            except (AttributeError, KeyError):
                return None

        return cmd

    def subcommand(
        self,
        name: str = None,
        *,
        aliases: typing.List[str] = None,
        help: str = None,
        brief: str = None,
        usage: str = None,
        enabled: bool = True,
        hidden: bool = False,
        ignore_extra: bool = True,
    ):
        """
        A decorator to declare a subcommand for a Molter message command.

        Parameters:
            name (`str`, optional): The name of the command.
            Defaults to the name of the coroutine.

            aliases (`list[str]`, optional): The list of aliases the
            command can be invoked under.

            help (`str`, optional): The long help text for the command.
            Defaults to the docstring of the coroutine, if there is one.

            brief (`str`, optional): The short help text for the command.
            Defaults to the first line of the help text, if there is one.

            usage(`str`, optional): A string displaying how the command
            can be used. If no string is set, it will default to the
            command's signature. Useful for help commands.

            enabled (`bool`, optional): Whether this command can be run
            at all. Defaults to True.

            hidden (`bool`, optional): If `True`, the default help
            command (when it is added) does not show this in the help
            output. Defaults to False.

            ignore_extra (`bool`, optional): If `True`, ignores extraneous
            strings passed to a command if all its requirements are met
            (e.g. ?foo a b c when only expecting a and b).
            Otherwise, an error is raised. Defaults to True.

        Returns:
            `molter.MolterCommand`: The command object.
        """

        def wrapper(func):
            cmd = MolterCommand(  # type: ignore
                callback=func,
                name=name or func.__name__,
                aliases=aliases or [],
                help=help,
                brief=brief,
                usage=usage,  # type: ignore
                enabled=enabled,
                hidden=hidden,
                ignore_extra=ignore_extra,
            )
            self.add_command(cmd)
            return cmd

        return wrapper

    async def __call__(self, ctx: context.MolterContext):
        """
        Runs the callback of this command.
        Args:
            ctx (`context.MolterContext`): The context to use for this command.
        """
        return await self.invoke(ctx)

    async def invoke(self, ctx: context.MolterContext):
        """
        Runs the callback of this command.
        Args:
            ctx (`context.MolterContext`): The context to use for this command.
        """
        # sourcery skip: remove-empty-nested-block, remove-redundant-if, remove-unnecessary-else
        callback = self.callback

        if len(self.params) == 0:
            return await callback(ctx)
        else:
            new_args: list[typing.Any] = []
            kwargs: dict[str, typing.Any] = {}
            args = ArgsIterator(tuple(ctx.args))
            param_index = 0

            for arg in args:
                while param_index < len(self.params):
                    param = self.params[param_index]

                    if param.consume_rest:
                        arg = " ".join(args.consume_rest())

                    if param.variable:
                        args_to_convert = args.consume_rest()
                        new_arg = [
                            await _convert(param, ctx, arg) for arg in args_to_convert
                        ]
                        new_arg = tuple(arg[0] for arg in new_arg)
                        new_args.append(new_arg)
                        param_index += 1
                        break

                    if param.greedy:
                        greedy_args, broke_off = await _greedy_convert(param, ctx, args)

                        new_args.append(greedy_args)
                        param_index += 1
                        if broke_off:
                            args.back()

                        if param.default:
                            continue
                        else:
                            break

                    converted, used_default = await _convert(param, ctx, arg)
                    if not param.consume_rest:
                        new_args.append(converted)
                    else:
                        kwargs[param.name] = converted
                    param_index += 1

                    if not used_default:
                        break

            if param_index < len(self.params):
                for param in self.params[param_index:]:
                    if not param.optional:
                        raise errors.BadArgument(
                            f"{param.name} is a required argument that is missing."
                        )
                    else:
                        if not param.consume_rest:
                            new_args.append(param.default)
                        else:
                            kwargs[param.name] = param.default
                            break
            elif not self.ignore_extra and not args.finished:
                raise errors.BadArgument(f"Too many arguments passed to {self.name}.")

            return await callback(ctx, *new_args, **kwargs)


def message_command(
    name: str = None,
    *,
    aliases: typing.List[str] = None,
    help: str = None,
    brief: str = None,
    usage: str = None,
    enabled: bool = True,
    hidden: bool = False,
    ignore_extra: bool = True,
):
    """
    A decorator to declare a coroutine as a Molter message command.

    Parameters:
        name (`str`, optional): The name of the command.
        Defaults to the name of the coroutine.

        aliases (`list[str]`, optional): The list of aliases the
        command can be invoked under.

        help (`str`, optional): The long help text for the command.
        Defaults to the docstring of the coroutine, if there is one.

        brief (`str`, optional): The short help text for the command.
        Defaults to the first line of the help text, if there is one.

        usage(`str`, optional): A string displaying how the command
        can be used. If no string is set, it will default to the
        command's signature. Useful for help commands.

        enabled (`bool`, optional): Whether this command can be run
        at all. Defaults to True.

        hidden (`bool`, optional): If `True`, the default help
        command (when it is added) does not show this in the help
        output. Defaults to False.

        ignore_extra (`bool`, optional): If `True`, ignores extraneous
        strings passed to a command if all its requirements are met
        (e.g. ?foo a b c when only expecting a and b).
        Otherwise, an error is raised. Defaults to True.

    Returns:
        `molter.MolterCommand`: The command object.
    """

    def wrapper(func):
        return MolterCommand(  # type: ignore
            callback=func,
            name=name or func.__name__,
            aliases=aliases or [],
            help=help,
            brief=brief,
            usage=usage,  # type: ignore
            enabled=enabled,
            hidden=hidden,
            ignore_extra=ignore_extra,
        )

    return wrapper


msg_command = message_command
prefix_command = message_command
text_based_command = message_command
