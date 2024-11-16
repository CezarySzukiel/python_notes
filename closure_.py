# def outer_fn():
#     x = 42
#
#     def inner_fn():
#         y = x * 2
#         return y
#
#     return inner_fn # zwracamy definicję funkcji, nie jej wynik
#
#
# result_fn = outer_fn()
# result = result_fn()
# print(result)
#
# def outer_fn():
#     az = 666
#     x = 42
#
#     def inner_fn():
#         nonlocal x
#         y = az * 2 + x
#         x += 1
#         return y
#
#     return inner_fn
#
#
# result_fn = outer_fn()
# # dunder -> double underscores
# print(result_fn.__closure__[0].cell_contents)
# print(result_fn.__closure__[1].cell_contents)
# result = result_fn()
# print(result_fn.__closure__[0].cell_contents)
# print(result_fn.__closure__[1].cell_contents)
# # print(result)
from time import sleep


# napisz generator liczb od 1 do nie skończoności z krokiem 1
# dodaj możliwość definicji startu od którego zaczyna liczyć
# dodaj możliwość zmiany numeracji


# def outer_fn(index=1):
#     def get_id_inner(new_index=None):
#         nonlocal index
#         if new_index is not None:
#             index = new_index
#         result = index
#         index += 1
#         return result
#
#     return get_id_inner
#
# gen_id = outer_fn()
# print(gen_id())
# print(gen_id())
# print(gen_id(42))
# print(gen_id())
# print(gen_id())


# nonlocal i global te 2 słowa kluczowe uważane są za nienajlepszą praktykę, przekaż tę funkcję tak, aby usunąć nonlocal

# def outer_fn(index=1):
#     def inner_fn(new_index=None):
#         if new_index is not None:
#             inner_fn.index = new_index
#
#         result = inner_fn.index
#         inner_fn.index += 1
#         return result
#
#     inner_fn.index = index
#
#     return inner_fn
#
#
# gen_id = outer_fn()
# print(gen_id())
# print(gen_id())
# print(gen_id(42))
# print(gen_id())
# print(gen_id())

# napisz  funkcję, która w zależności od pierqwszego el kolekcji, będzie dzielić następne elementty, bądź mnożyć
# >= 0  - ma mnożyć przez 2
# < 0 - ma dzielić przez 2

# def calculate():
#     predicate = None
#     def inner(item):
#         nonlocal predicate
#         if predicate is None:
#             predicate = item >= 0
#
#         if predicate:
#             return item * 2
#         return item / 2
#
#     return inner
#
#
# calc=calculate()
#
# r1 = list(map(calculate(), [1, 2, 3, 4]))
# r2 = list(map(calculate(), [-1, 2, 3, 4]))
#
# r3 = list(map(calc, [1, 2, 3, 4]))
# r4 = list(map(calc, [-1, 2, 3, 4]))
#
# print(r1, r2, r3, r4)

# memoizing lvl - 1
# zapamiętywanie wyniku funkcji, żeby reużyć, aby nie liczyć ponownie
# Rules:
# - fn musi być pure
# - relatywnie niewielka ilość róznych kombinacji parametrów

#
# def calculate_magic(a, b):
#     # jakieś intensive CPU task
#     sleep(3)
#     return a + b

#
# def memoize():
#     cache = {}
#
#     def inner(a, b):
#         key = f"{a},{b}"
#         if key not in cache:
#             # intensive CPU task
#             sleep(3)
#             cache[key] = a + b
#         return cache[key]
#
#     return inner


# calculate_magic = memoize()

def calculate_magic(a, b):
    # jakieś intensive CPU task
    sleep(3)
    return a + b

def calculate

print(calculate_magic(1, 2))
print(calculate_magic(2, 2))
print(calculate_magic(1, 2))
print(calculate_magic(2, 2))


def memoize(cb):
    cache = {}

    def inner(*args):
        if args not in cache:
            cache[args] = cb(*args)
        return cache[args]

    return inner


def calculate_magic(a, b, /):
    # intensive CPU task
    sleep(3)
    return a + b


def calculate_tribonacci(a, b, c, /):
    # intensive CPU task
    sleep(3)
    return a + b + c


calculate_magic_cache = memoize(calculate_magic)
calculate_tribonacci_cache = memoize(calculate_tribonacci)

print(calculate_magic_cache(1, 2))
print(calculate_magic_cache(2, 2))
print(calculate_magic_cache(1, 2))
print(calculate_magic_cache(2, 2))
print(calculate_tribonacci_cache(2, 2, 2))