import ast
import time


def count_functions_in_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)

    return sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))


def add(*args):
    return sum(args)


assert add(1, 2, 3, 4) == 10


def boolean_to_string(b):
    if b:
        return "True"
    return "False"


assert boolean_to_string(True) == "True"
assert boolean_to_string(False) == "False"


def is_even(n):
    if n % 2 == 0:
        return True
    return False


assert is_even(10)
assert not is_even(5)


def make_negative(number):
    return number if number <= 0 else number * -1


assert make_negative(-1) == -1
assert make_negative(0) == 0
assert make_negative(1) == -1


def pipe_fix(nums):
    return [i for i in range(nums[0], nums[-1] + 1)]


assert pipe_fix([-1, 4]) == [-1, 0, 1, 2, 3, 4]
assert pipe_fix([1, 5]) == [1, 2, 3, 4, 5]


def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


assert goals(5, 5, 5) == 15


def move(position, roll):
    return position + roll * 2


assert move(3, 6) == 15


def create_counter():
    counter = 0

    def counter_updater():
        nonlocal counter
        counter += 1
        return counter

    return counter_updater


counter = create_counter()

assert counter() == 1
assert counter() == 2
assert counter() == 3


def multiplier(n):
    def inner(num):
        return num * n

    return inner


times_two = multiplier(2)
times_three = multiplier(3)

assert times_two(5) == 10
assert times_three(5) == 15


def time_catcher(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


def slow_function(x):
    print("computing...")
    time.sleep(1)
    return x * x


assert slow_function(2) == 4
assert slow_function(4) == 16

print("*-" * 50)
print("next function")
print("*-" * 50)


def memoize(func):
    cache = {}

    def inner(num):
        if num not in cache:
            result = func(num)
            cache.update({num: result})
        return cache[num]

    return inner


memoized = memoize(slow_function)
assert time_catcher(memoized, 4) >= 1
assert time_catcher(memoized, 4) < 1
assert memoized(4) == 16


def fibonacci_generator():
    fibs = [0, 0]
    def fibonacci_first():
        result = fibs[-1] + fibs[-2]
        fibs.append(result)
        if result == 0:
            fibs[1] += 1
        return result
    return fibonacci_first


fib = fibonacci_generator()

assert fib() == 0
assert fib() == 1
assert fib() == 1
assert fib() == 2
assert fib() == 3
assert fib() == 5
assert fib() == 8


if __name__ == "__main__":
    file_path = 'functions_homework.py'
    print(f"Number of functions in {file_path}: {count_functions_in_file(file_path)}")
