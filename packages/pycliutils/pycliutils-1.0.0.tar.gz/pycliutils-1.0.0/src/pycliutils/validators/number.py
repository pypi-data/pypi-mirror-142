import sys

from typing import Callable, Generic, Optional, Type, TypeVar, cast
if sys.version_info >= (3, 8):
    from typing import get_args

from argparse import ArgumentTypeError


N = TypeVar("N", int, float)


class Range(Generic[N]):

    @property
    def type(self) -> Type[N]:
        if self._type is not None:
            return self._type
        t = getattr(self, "__orig_class__", None)
        assert t is not None, f"{self.__class__.__name__} must overwrite property type with correct type"
        if sys.version_info >= (3, 8):
            return cast(Type[N], get_args(t)[0])
        else:
            return t.__args__[0]  # type: ignore[no-any-return]

    def __init__(
            self,
            minv: Optional[N] = None,
            maxv: Optional[N] = None,
            min_eq: bool = True,
            max_eq: bool = True,
            typ: Optional[Type[N]] = None) -> None:
        self.min: Optional[N] = minv
        self.max: Optional[N] = maxv
        self.min_eq = min_eq
        self.max_eq = max_eq
        self._type: Optional[Type[N]] = typ

    def __call__(self, value: str) -> N:
        try:
            parg = self.type(value)
        except ValueError as e:
            raise ArgumentTypeError("value must be of type %s" % self.type.__name__) from e
        bmin = self.min is None or self.min < parg or (self.min_eq and parg == self.min)
        bmax = self.max is None or self.max > parg or (self.max_eq and parg == self.max)
        if bmax and bmin:
            return parg
        if self.min is not None:
            if self.max is not None:
                raise ArgumentTypeError("value must be in range %s to %s" % (self.min, self.max))
            if self.min == 0:
                raise ArgumentTypeError("value must be positive")
            if self.min_eq:
                raise ArgumentTypeError("value must be at least %s" % self.min)
            raise ArgumentTypeError("value must be greater than %s" % self.min)
        if self.max_eq:
            raise ArgumentTypeError("value must be at most %s" % self.max)
        if self.max == 0:
            raise ArgumentTypeError("value must be negative")
        raise ArgumentTypeError("value must be less than %s" % self.max)


class RangeInt(Range[int]):

    @property
    def type(self) -> Type[int]:
        return int


class RangeFloat(Range[float]):

    @property
    def type(self) -> Type[float]:
        return float

