# iterable -> __iter__ -> iterator object (protokół nazywa się iterator)
# iterator ->__iter__ & __next__ -> item | StopIteration
from typing import Iterator

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
# print(iterator)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for number in iterator:
#     print(number)


class Range:
    def __init__(self, start: int, stop: int | None = None, step: int = 1,
                 /) -> None:  # / wymusza pozycyjne, nei da się nazwanych
        if stop is None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step
        self.item = start
        self.counter = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter >= (self.stop - self.start) / self.step:
            raise StopIteration("Something is no yes")

        result = self.item
        self.counter += 1
        self.item += self.step
        return result


r1 = Range(0, 5, 1)
it = iter(r1)

print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))

# for element in Range(5):
#     print(element)