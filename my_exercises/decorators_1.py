def wrapper(fn):
    def inner(*args):
        print("Function called with arguments:", args)

        return fn(*args)

    return inner


def multiply_by_2_before_action(fn):
    def inner(*args):
        print("mnożę każdy arg przez 2")
        modified_args = [arg * 2 for arg in args]
        return fn(*modified_args)

    return inner


def cast_to_float(fn):
    def inner(*args):
        print("castuję na float")
        modified_args = [float(arg) for arg in args]
        return fn(*modified_args)
    return inner


def multiply(multiplier):
    def decorator(fn):
        def inner(*args):
            print(f"mnożę każdy arg przez {multiplier}")
            modified_args = [arg * multiplier for arg in args]
            return fn(*modified_args)
        return inner
    return decorator




# @multiply_by_2_before_action
@wrapper
@cast_to_float
@wrapper
@multiply(multiplier=5)
@wrapper
def add(*args):
    """Returns the sum of all arguments."""
    print("sumuję")
    return sum(args)


a = add("1", "2", "3", "4", "5", "6")
print(a)

# def closure_counter():
#     counter = 0
#     def inner():
#         nonlocal counter
#         counter += 1
#         return counter
#     return inner
#
# counter = closure_counter()
# print(counter())
# print(counter())
# print(counter())
# print(counter())
