import sys

from typing import Union, Optional, Tuple

from ..fmt import Text
from . import config


def print_question(text: Union[str, Text], inline: Optional[bool] = None) -> None:
    if inline is None:
        inline = len(Text(text).unformatted) <= config.AUTO_INLINE_MAX_CHARACTER_COUNT
    txt: Tuple[Union[str, Text], ...]
    if inline:
        txt = (config.QUESTION_PREFIX, text, config.QUESTION_INLINE_SUFFIX,)
    else:
        txt = (text, "\r\n", config.QUESTION_PREFIX,)
    print(Text(*txt, config=config.QUESTION_FORMAT), end="", flush=True)

