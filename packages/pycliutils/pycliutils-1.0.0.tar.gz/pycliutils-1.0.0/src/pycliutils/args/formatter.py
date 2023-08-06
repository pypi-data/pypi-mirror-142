import logging
from typing import Any, Callable, Dict, Generic, List, Literal, Optional, TextIO, Type, TypeVar, Sequence, Union, cast, overload

from . import config
from ..fmt import Color, TextConfig, TextFormat, Text


class ColorFormatter(logging.Formatter):
    """A class for formatting colored logs."""

    def format(self, record: logging.LogRecord) -> str:
        ln = record.levelname.upper()
        text_config = getattr(config, f"TEXT_{ln}_CONFIG", None)
        if text_config is not None:
            record.msg = Text(record.msg, config=text_config).parse()
        return super().format(record)

