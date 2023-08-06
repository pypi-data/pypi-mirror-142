import inspect
import sys

from abc import ABC, ABCMeta, abstractmethod

from typing import Any, Callable, Generic, List, Optional, Type, TypeVar, Union

from argparse import ArgumentTypeError

T = TypeVar("T")
I = TypeVar("I")
O = TypeVar("O")
O1 = TypeVar("O1")
O2 = TypeVar("O2")


class Converter(ABC, Generic[I, O]):

    @abstractmethod
    def convert(self, value: I) -> O:
        raise NotImplementedError

    def __call__(self, value: I) -> O:
        return self.convert(value)

    def is_valid(self, value: I) -> bool:
        try:
            self.convert(value)
        except (ValueError, ArgumentTypeError):
            return False
        return True

    def to_validator(self) -> "ConverterValidator[I]":
        return ConverterValidator(self)

    def chain(self, other: "Union[Converter[O, T], Callable[[O], T]]") -> "ConverterChain[I, T]":
        if not isinstance(other, Converter):
            other = FunctionConverter[O, T](other)
        return ConverterChain(self, other)

    def rchain(self, other: "Union[Converter[T, I], Callable[[T], I]]") -> "ConverterChain[T, O]":
        if not isinstance(other, Converter):
            other = FunctionConverter(other)
        return other.chain(self)

    def branch(self, other: "Union[Converter[I, T], Callable[[I], T]]") -> "ConverterBranch[I, O, T]":
        if not isinstance(other, Converter):
            other = FunctionConverter(other)
        return ConverterBranch(self, other)

    def rbranch(self, other: "Union[Converter[I, T], Callable[[I], T]]") -> "ConverterBranch[I, T, O]":
        if not isinstance(other, Converter):
            other = FunctionConverter(other)
        return other.branch(self)

    def __truediv__(self, other: "Union[Converter[O, T], Callable[[O], T], Any]") -> "ConverterChain[I, T]":
        if not callable(other):
            return NotImplemented
        return self.chain(other)

    def __rtruediv__(self, other: "Union[Callable[[T], I], Any]") -> "ConverterChain[T, O]":
        if not callable(other):
            return NotImplemented
        return self.rchain(other)

    def __rshift__(self, other: "Union[Converter[O, T], Callable[[O], T], Any]") -> "ConverterChain[I, T]":
        return self / other

    def __rrshift__(self, other: "Union[Callable[[T], I], Any]") -> "ConverterChain[T, O]":
        return other / self

    def __mul__(self, other: "Union[Converter[O, T], Callable[[O], T], Any]") -> "ConverterChain[I, T]":
        return self / other

    def __rmul__(self, other: "Union[Callable[[T], I], Any]") -> "ConverterChain[T, O]":
        return other / self

    def __add__(self, other: "Union[Converter[I, T], Callable[[I], T], Any]") -> "ConverterBranch[I, O, T]":
        if not callable(other):
            return NotImplemented
        return self.branch(other)

    def __radd__(self, other: "Union[Converter[I, T], Callable[[I], T], Any]") -> "ConverterBranch[I, T, O]":
        if not callable(other):
            return NotImplemented
        return self.rbranch(other)

    def __invert__(self) -> "ConverterValidator[I]":
        return self.to_validator()

class Validator(Converter[T, T]):

    def __init__(self, error_msg: Optional[str] = None) -> None:
        super().__init__()
        self.error_msg = error_msg  # TODO: check that error_msg is valid format str

    def convert(self, value: T) -> T:
        if self.validate(value) is False:
            msg = "Validation of %s failed"
            if self.error_msg is not None:
                try:
                    msg = self.error_msg % value
                except ValueError:
                    msg = self.error_msg
            raise ArgumentTypeError(msg % value)
        return value

    @abstractmethod
    def validate(self, value: T) -> Optional[bool]:
        raise NotImplementedError

class FunctionConverter(Converter[I, O]):

    def __init__(self, convert: Callable[[I], O]) -> None:
        super().__init__()
        self._converter = convert

    def convert(self, value: I) -> O:
        return self._converter(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._converter)})"

class FunctionValidator(Validator[T]):

    def __init__(self, validate: Callable[[T], Optional[bool]], error_msg: Optional[str] = None) -> None:
        super().__init__(error_msg)
        self._validator = validate

    def validate(self, value: T) -> Optional[bool]:
        return self._validator(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._validator)})"

class ConverterValidator(Validator[T]):

    def __init__(self, converter: Converter[T, O]) -> None:
        super().__init__()
        self._converter = converter

    def validate(self, value: T) -> None:
        self._converter(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._converter)})"

class ConverterChain(FunctionConverter[I, O]):

    def __init__(self, first_converter: Converter[I, T], second_converter: Converter[T, O]) -> None:
        super().__init__(lambda value: second_converter.convert(first_converter.convert(value)))
        self.first_converter = first_converter
        self.second_converter = second_converter

    def __repr__(self) -> str:
        converter = []
        stack = [self.second_converter, self.first_converter]
        while len(stack) > 0:
            c = stack.pop()
            if isinstance(c, ConverterChain):
                stack.append(c.second_converter)
                stack.append(c.first_converter)
            else:
                converter.append(c)
        return f"<ConverterChain: {', '.join(repr(c) for c in converter)}>"

class ConvertError(ArgumentTypeError):
    
    def __init__(self, msg: str, *errors: Union[ValueError, ArgumentTypeError]) -> None:
        super().__init__(msg)
        self.errors = errors

class ConverterBranch(Converter[I, Union[O1, O2]]):

    def __init__(self, first_converter: Converter[I, O1], second_converter: Converter[I, O2], error_msg: str = "could not convert value '%s'") -> None:
        self.error_msg = error_msg
        self.first_converter = first_converter
        self.second_converter = second_converter

    def convert(self, value: I) -> Union[O1, O2]:
        err_list: List[Union[ValueError, ArgumentTypeError]] = []
        try:
            return self.first_converter(value)
        except ConvertError as cerr:
            err_list.extend(cerr.errors)
        except (ValueError, ArgumentTypeError) as err:
            err_list.append(err)
        try:
            return self.second_converter(value)
        except ConvertError as cerr:
            err_list.extend(cerr.errors)
        except (ValueError, ArgumentTypeError) as err:
            err_list.append(err)
        try:
            msg = self.error_msg % value
        except TypeError:
            msg = self.error_msg
        raise ConvertError(msg, *err_list)


    def __repr__(self) -> str:
        converter = []
        stack = [self.second_converter, self.first_converter]
        while len(stack) > 0:
            c = stack.pop()
            if isinstance(c, ConverterChain):
                stack.append(c.second_converter)
                stack.append(c.first_converter)
            else:
                converter.append(c)
        return f"<ConverterBranch: {', '.join(repr(c) for c in converter)}>"
