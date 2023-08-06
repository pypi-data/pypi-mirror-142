"""Functions for my_traceback subpackage."""

from __future__ import annotations
from typing import Type, Sequence
import traceback as traceback_module
import sys
from types import TracebackType
import textwrap

from ..str_formating import format_str

sys_hook_backup = sys.excepthook

EXCEPTION_INDENT = 4


from typing_extensions import Literal

from ..colors.colors_module import colors_config, colorize_traceback
from ..str_formating import format_str

# TODO color + tests + docs
def raise_enhanced(exception_type: Type[Exception], value: str, traceback: None | TracebackType) -> None:
    """Enhance printed exception. Message as well as traceback. It adds colors if configured. You can call
    it directly.

    Args:
        exception_type (Type[Exception]): _description_
        value (str): _description_
        traceback (None | TracebackType): _description_
    """

    traceback_list = traceback_module.format_tb(traceback, limit=None)

    traceback_str = colorize_traceback(f"Traceback (most recent call last): \n{''.join(traceback_list)}")
    traceback_str = textwrap.indent(text=traceback_str, prefix=" " * EXCEPTION_INDENT)

    message = format_str(value, caption=exception_type.__name__, indent=EXCEPTION_INDENT)

    print(f"\n\n{traceback_str}{message}")


def enhance_excepthook():
    """Change default excepthook to formatted one.

    That means that if there is a uncaught raise, output message with traceback will be colored if
    possible.
    """
    sys.excepthook = raise_enhanced


def enhance_excepthook_reset():
    """Reset original excepthook."""
    sys.excepthook = sys_hook_backup


def get_traceback_str_with_removed_frames(lines: Sequence[str], exact_match: bool = True) -> str:
    """Remove particular levels of stack trace defined by content.

    Note:
        If not using exact_match, beware of not using short message that can be also elsewhere, where not
        supposed, as it can make debugging a nightmare.

    Args:
        lines (list): Line in call stack that we want to hide.
        exact_match (bool, optional): If True, stack frame will be removed only if it is exactly the same.
            If False, then line can be just subset of stack frame.

    Returns:
        str: String traceback ready to be printed.

    Example:
        >>> def buggy():
        ...     return 1 / 0
        ...
        >>> try:
        ...     buggy()
        ... except ZeroDivisionError:
        ...     traceback = get_traceback_str_with_removed_frames([])
        ...     traceback_cleaned = get_traceback_str_with_removed_frames(["buggy()"])
        >>> "buggy()" in traceback
        True
        >>> "buggy()" not in traceback_cleaned
        True

    """
    exc = traceback_module.TracebackException(*sys.exc_info())  # type: ignore

    if exact_match:
        for i in exc.stack[:]:
            if i.line in lines:
                exc.stack.remove(i)

    else:
        for i in exc.stack[:]:
            for j in lines:
                if i.line and i.line in j:
                    exc.stack.remove(i)

    return "".join(exc.format())


# TODO rename to format exception???
def format_traceback(
    message: str = "",
    caption: str = "error_type",
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "ERROR",
    remove_frame_by_line_str: None | list = None,
) -> str:
    """Raise warning with current traceback as content. It means, that error was caught, but still
    something crashed.

    Args:
        message (str): Any string content of traceback.
        caption (str, optional): Caption of warning. If 'error_type', than Error type (e.g. ZeroDivisionError)
        is used. Defaults to 'error_type'.
        level (Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], optional): Defaults to "DEBUG".
        stack_level (int, optional): How many calls to log from error. Defaults to 3.
        remove_frame_by_line_str(None | list, optional): If there is some level in stack that should be
        omitted, add line here. Defaults to None.
    """
    if remove_frame_by_line_str:
        separated_traceback = get_traceback_str_with_removed_frames(remove_frame_by_line_str)

    else:
        separated_traceback = traceback_module.format_exc()

    if caption == "error_type":
        try:
            caption = sys.exc_info()[1].__class__.__name__
        except AttributeError:
            caption = "Error"

    if colors_config.USE_COLORS:
        separated_traceback = colorize_traceback(separated_traceback)

    separated_traceback = separated_traceback.rstrip()

    separated_traceback = format_str(
        message=message,
        caption=caption,
        use_object_conversion=False,
        uncolored_message=f"\n\n{separated_traceback}" if message else f"{separated_traceback}",
        level=level,
    )

    return separated_traceback
