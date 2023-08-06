from typing import Callable, Optional, TypeVar

from argparse import ArgumentTypeError

from . import unix

T = TypeVar("T")

def select_char(chars: str, ignore_case: bool = True, allow_empty: bool = True, silent: bool = False) -> Optional[str]:
    return unix.select_char(chars, ignore_case, allow_empty, silent)

def select_bool(default: Optional[bool] = None, ignore_case: bool = True, allow_empty: bool = True, silent: bool = False) -> Optional[bool]:
    result = select_char("yn", ignore_case, allow_empty, silent)
    return (result.lower() == "y") if result else default

def select_str(verify: Callable[[str], bool] = lambda text: True, default: Optional[str] = None, silent: bool = False) -> str:
    result = unix.select_str(lambda text: verify(text) or (len(text) == 0 and default is not None), silent)
    return result if result or not default else default

def select(convert: Callable[[str], T], default: Optional[T] = None, allow_empty: bool = False, silent: bool = False) -> Optional[T]:
    allow_empty = allow_empty if default is None else True
    def verify(text: str) -> bool:
        if len(text) < 1 and allow_empty:
            return True
        try:
            convert(text)
            return True
        except (ValueError, ArgumentTypeError):
            return False
    result = select_str(verify, default="" if allow_empty else None, silent=silent)
    return convert(result) if len(result) > 0 or not allow_empty else default


