from abc import ABC, abstractmethod
from collections.abc import Iterable, Generator
from typing import Any, TypeVar


class NonStringIterable(ABC):
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is NonStringIterable:
            if issubclass(subclass, str):
                return False
            if hasattr(subclass, "__iter__") and callable(subclass.__iter__):
                return True
        return NotImplemented



TD = TypeVar("TD")

data: list[Any] = [(1, 2), [3, 4, [1, 2], [2, 3, 4, 5]], [1, 2]]
data1: list[Any] = [1, 2, 3, 4, 1, 2, 2, 3, 4, 5, 1, 2]
data3: list[Any] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November', 'December']

T = TypeVar("T")


def flatten(items: Iterable[T]) -> Generator[T]:
    for item in items:
        if isinstance(item, NonStringIterable):
            yield from flatten(item)
        else:
            yield item


result = list(flatten(data))
result2 = list(flatten(data1))
result3 = list(flatten(data3))

if __name__ == "__main__":
    print(result)
    print(result2)
    print(result3)


    # assert result == [1, 2, 3, 4]

    def abstract_static_method():
        raise NotImplementedError
