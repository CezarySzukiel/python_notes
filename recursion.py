# Dijkstra
import types


# Napisz funkcję do dodawania liczb

# def add(n, acc=0):
#     if n == 0:
#         return acc
#     else:
#         return add(n - 1, acc + n)


# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

# print(add(1000))


# Alex Bill - wymyslił trampolinę

def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)

    return g


def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)


def ft(n, curr=0, next_=1):
    if n == 0:
        yield curr
    else:
        yield ft(n - 1, next_, curr + next_)


import sys

sys.set_int_max_str_digits(1000000)


# print(len(f'{tramp(ft, 100000)}'))

# napisz fn do usuwania znaków
# 'ala ma kota!?' -> !? -> ala ma kota
# bez regex
# użyj rekurencji (replace)

def remove_chars(text: str, chars: str) -> str:
    if chars:
        return remove_chars(
            text.replace(chars[0], ''),
            chars[1:]
        )
    return text


print(remove_chars('ala? ma! kota?', '!?a'))
