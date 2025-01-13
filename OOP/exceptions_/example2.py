from collections.abc import Container
import math


class CustomError(Exception):
    pass


class TriangleError(Exception):
    def __init__(self, message: str = "Invalid triangle", sides: Container[float] | None = None) -> None:
        super().__init__(message)
        self._sides = sides

    @property
    def sides(self):
        if self._sides is None:
            raise AttributeError("No sides provided")
        return self._sides

    def __str__(self):
        try:
            return f"{self.args[0]} for sides {self.sides}"
        except AttributeError:
            return self.args[0]

    def __repr__(self):
        try:
            return f"{type(self).__name__}({self.args[0]!r}, {self.sides!r})"
        except AttributeError:
            return f"{type(self).__name__}({self.args[0]!r})"


def triangle_area(a: float, b: float, c: float) -> float:
    sides: list[float] = sorted((a, b, c))

    if sides[2] >= sides[0] + sides[1]:
        raise TriangleError("Yolo triangle", sides=sides)

    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


# print(triangle_area(3, 4, 5))
# print(triangle_area(1, 2, 3))
# print(triangle_area(1, 1, 3))


try:
    triangle_area(1, 1, 3)
except TriangleError as e:
    print(repr(e))