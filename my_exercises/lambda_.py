from operator import index

lst = [1, 2, 3, 4, 5, 1]

print(lst.index)

squares = list(map(lambda x: x ** 2, lst))
print(squares)


def apply_to_all(callback, data):
    return [callback(x) for x in data]


squares = apply_to_all(lambda x: x ** 2, lst)
print(squares)


new_lst = apply_to_all(lambda x: (x, lst.index(x)), lst)

print(new_lst)
