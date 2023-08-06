import sys
from enum import Enum
from typing import Generic, Optional, Type, TypeVar, cast
if sys.version_info >= (3, 8):
    from typing import get_args

from argparse import ArgumentTypeError


E = TypeVar("E", bound=Enum)


class EnumSelector(Generic[E]):

    @property
    def type(self) -> Type[E]:
        if self._type is not None:
            return self._type
        t = getattr(self, "__orig_class__", None)
        assert t is not None, f"{self.__class__.__name__} must overwrite property type with correct type"
        if sys.version_info >= (3, 8):
            return cast(Type[E], get_args(t)[0])
        else:
            return t.__args__[0]

    def __init__(self, typ: Optional[Type[E]] = None) -> None:
        self._type: Optional[Type[E]] = typ

    def __call__(self, value: str) -> E:
        args = {str(entry): entry for entry in self.type}
        if value in args:
            return args[value]
        raise ArgumentTypeError(f"invalid {self.type.__name__} value: '{value}'")

