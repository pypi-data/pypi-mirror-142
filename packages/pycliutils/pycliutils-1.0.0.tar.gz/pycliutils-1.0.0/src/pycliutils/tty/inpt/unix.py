import select
import sys
import termios
import tty

from typing import Callable, Optional

from ...fmt import Text, TextConfig
from .. import config

def set_cursor_format(config: Optional[TextConfig] = None) -> None:
    print(Text(" \b", config=config), end="", flush=True)


# read a single character on a unix system
# https://exceptionshub.com/python-read-a-single-character-from-the-user.html
def read_char(validate: Callable[[str], bool] = lambda c: True, silent: bool = False) -> str:
    fd = sys.stdin.fileno()

    old_settings = termios.tcgetattr(fd)
    char: Optional[str] = None
    try:
        tty.setraw(fd)
        while char is None or not validate(char):
            if char is not None:
                set_cursor_format(config.CURSOR_ERROR_FORMAT)
                select.select([sys.stdin], [], [], config.CURSOR_ERROR_TIME)[0]
            set_cursor_format(config.CURSOR_DEFAULT_FORMAT)
            char = sys.stdin.read(1)
            set_cursor_format()
            if ord(char) == 0x3:
                raise KeyboardInterrupt
        if not silent:
            if ord(char) == 0x7f:  # backspace
                print("\b \b", end="", flush=True)
            elif char in ["\r", "\n"]:
                print("\r\n", end="", flush=True)
            else:
                print(char, end="", flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return char


def select_str(verify: Callable[[str], bool], auto_accept: bool = False, silent: bool = False) -> str:
    out = ""
    while True:
        c = read_char(validate=lambda char: (verify(out) and (ord(char) != 0x4 or out=="")) if ord(char) in [0x4, ord("\n"), ord("\r")] else (ord(char) != 0x7f or len(out) > 0), silent=silent)
        ci = ord(c)
        if ci == 0x7f:
            out = out[:-1]
        elif ci in [0x4, 0xd]:  # EOF, Enter
            return out
        else:
            out += c
        if auto_accept and verify(out):
            return out


def select_char(chars: str, ignore_case: bool = True, allow_empty: bool = True, silent: bool = False) -> Optional[str]:
    if ignore_case:
        chars = chars.lower()
    def verify_char(char: str) -> bool:
        test_char = char.lower() if ignore_case else char
        if test_char in chars:
            return True
        if allow_empty and ord(test_char) in [0x4, ord('\r'), ord('\n')]:  # EOF, new line
            return True
        return False
    c = read_char(verify_char, silent=silent)
    if not silent:
        print("\r\n", end="", flush=True)
    return c

