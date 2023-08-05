import ctypes
from typing import (
    Generic, 
    TypeVar, 
    Any, 
    Type, 
    get_type_hints, 
    Callable, 
    Iterator
)

from typing_extensions import ParamSpec
import inspect
from functools import wraps
from contextlib import suppress

__all__ = (
    "dereference_address",
    "Pointer",
    "to_ptr",
    "decay"
)

T = TypeVar("T")
A = TypeVar("A")
P = ParamSpec("P")


def dereference_address(address: int) -> Any:
    """Dereference an address. Will cause a segmentation fault if the address is invalid."""
    return ctypes.cast(address, ctypes.py_object).value

class Pointer(Generic[T]):
    """Base class representing a pointer."""
    def __init__(self, address: int, typ: Type[T]) -> None:
        self._address = address
        self._type = typ

    @property
    def address(self) -> int:
        """Address of the pointer."""
        return self._address

    @property
    def type(self) -> Type[T]:
        """Type of the pointer."""
        return self._type

    def __repr__(self) -> str:
        return f"<pointer to {self.type.__name__} object at {hex(self.address)}>"

    def __str__(self) -> str:
        return hex(self.address)

    def dereference(self) -> T:
        """Dereference the pointer."""
        return dereference_address(self.address)

    def __iter__(self) -> Iterator[T]:
        """Dereference the pointer."""
        return iter({self.dereference()})

def to_ptr(val: T) -> Pointer[T]:
    """Convert a value to a pointer."""
    return Pointer(id(val), type(val))

def decay(func: Callable[P, T]) -> Callable[..., T]:
    """Automatically convert values to pointers when called."""
    @wraps(func)
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        hints = get_type_hints(func)
        actual: dict = {}
        params = inspect.signature(func).parameters

        for index, key in enumerate(params):
            if key in kwargs:
                actual[key] = kwargs[key]
            else:
                with suppress(IndexError):
                    actual[params[key].name] = args[index]
            
        for key, value in hints.items():
            if (hasattr(value, "__origin__")) and (value.__origin__ == Pointer):
                actual[key] = to_ptr(actual[key])

        return func(**actual)

        
    return inner