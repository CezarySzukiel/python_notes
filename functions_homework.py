import ast


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

if __name__ == "__main__":
    file_path = 'functions_homework.py'
    print(f"Number of functions in {file_path}: {count_functions_in_file(file_path)}")
