from typing import Any, Callable, TypeVar, Iterator as Iterator_t, Optional, Union

MIN_32BIT_INT: int
MAX_32BIT_INT: int
MIN_64BIT_INT: int
MAX_64BIT_INT: int

T = TypeVar("T", bound="Iterator")

class Iterator:
    def __init__(
        self,
        objToIterate: Iterator_t[T],
        numFunc: Callable[[Iterator_t[T]], int],
        getFunc: Callable[[Iterator_t[T], int], T],
    ) -> None: ...
    def __iter__(self) -> "Iterator": ...
    def __next__(self) -> T: ...
    next: Callable[..., T]

class MetaClassForClassesWithEnums(type):
    class EnumError(TypeError): ...

    def __setattr__(cls, name: str, value: Any) -> None: ...
    def __delattr__(cls, name: str) -> None: ...

def get_handle(thing: Optional[Any]): ...
def invoke_if_valid(
    cb: Optional[Union[Callable[..., Any], Any]], value: Any
) -> Any: ...
def deprecated(
    func_or_reason: Any,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
def isNonScalarSequence(obj: Any) -> bool: ...
