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


def some_function(x):
    return f'processing {x}'


assert some_function(5) == 'processing 5'


def rate_limiter(function, limit=3):
    usage = 0

    def call_with_limit(*args):
        nonlocal usage
        if usage < limit:
            usage += 1
            return function(*args)
        return f'limit {limit} exceeded'

    return call_with_limit


limited_function = rate_limiter(some_function, limit=2)

assert limited_function(42) == 'processing 42'
assert limited_function(42) == 'processing 42'
assert limited_function(42) == 'limit 2 exceeded'


def char_counter():
    summary_text = ''

    def char_updater(text):
        nonlocal summary_text
        summary_text = summary_text + text
        return len(summary_text)

    return char_updater


text_1_len = char_counter()

assert text_1_len('Ala ma kota') == 11
assert text_1_len(' i wszy') == 18


def total_sum():
    cache = []

    def sum_nums(number):
        cache.append(number)
        return sum(cache)

    return sum_nums


summary = total_sum()

assert summary(5) == 5
assert summary(5) == 10
assert summary(5) == 15


def total_average():
    cache = []

    def updater(*args):
        cache.extend(args)
        return round(sum(cache) / len(cache), 1)

    return updater


average = total_average()

assert average(5, 5, 5) == 5
assert average(1, 2, 3, 4) == 3.6


def list_cache():
    cache = []

    def updater(*args):
        cache.extend(args)
        return cache

    return updater


my_list = list_cache()

assert my_list(1) == [1]
assert my_list(2, 3, 4, 5) == [1, 2, 3, 4, 5]


def switcher():
    state = False

    def updater():
        nonlocal state
        state = not state
        return state

    return updater


switch = switcher()

assert switch()
assert not switch()


def power(x):
    def inner(n):
        return x ** n

    return inner


two_to_power = power(2)
assert two_to_power(2) == 4
assert two_to_power(3) == 8


def keys_counter():
    cache = {}

    def updater(key):
        if not key in cache:
            cache.update({key: 1})
        else:
            cache[key] += 1
        return cache[key]

    return updater


count_key = keys_counter()

assert count_key("a") == 1
assert count_key("b") == 1
assert count_key("a") == 2
assert count_key("a") == 3


def reverse_(text):
    def inner():
        return text[::-1]

    return inner


reversed_Ola = reverse_("Ola")

assert reversed_Ola() == "alO"


def step_counter(steps_limit=10):
    position = 0

    def counter(steps):
        nonlocal position
        position += min(steps, steps_limit)
        return position

    return counter


move = step_counter()

assert move(5) == 5
assert move(11) == 15
assert move(10) == 25


def call_history():
    cache = []

    def inner(*args):
        [cache.append(i) for i in args]
        return cache

    return inner


def create_shopping_list():
    cache = set()

    def inner(action, product=None):
        if action == "show":
            print(cache)
        elif action == "add":
            cache.add(product)
        return cache

    return inner


shopping_list = create_shopping_list()

assert shopping_list("add", "bread") == {'bread'}
assert shopping_list("add", "milk") == {'bread', 'milk'}
shopping_list("show")

history = call_history()

assert history(1, 3, 5) == [1, 3, 5]
assert history(2, 4, 6) == [1, 3, 5, 2, 4, 6]


def validate_positive(func):
    def validator(*args):
        for i in args:
            if i < 0:
                return ValueError("argument, can't be less than zero")
            elif type(i) is not int:
                return ValueError("argument must be integer")
        return func(*args)

    return validator


@validate_positive
def add_numbers(a, b):
    return a + b


assert add_numbers(3, 5) == 8
try:
    add_numbers(-1, 5)
except ValueError as e:
    assert str(e) == "argument, can't be less than zero"


def create_vowel_counter():
    vowels = ["a", "e", "i", "o", "u", "y", "ą", "ę"]
    counter = 0

    def vowel_counter(text):
        nonlocal counter
        counter += len([i for i in text if i.lower() in vowels])
        return counter

    return vowel_counter


vowel_counter = create_vowel_counter()

assert vowel_counter("hello") == 2
assert vowel_counter("ala") == 4
assert vowel_counter("Pythonista") == 8

if __name__ == "__main__":
    file_path = 'functions_homework.py'
    print(f"Number of functions in {file_path}: {count_functions_in_file(file_path)}")
