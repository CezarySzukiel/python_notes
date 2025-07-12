tpl = (1, 2, 3, 4, 5)
lts = [1, 2, 3, 4, 5]

# Unpacking a tuple
a, b, c, *d = tpl
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
# Unpacking a list
a, b, c, *d = lts
print(f"a: {a}, b: {b}, c: {c}, d: {d}")
# Unpacking with a single element
a, *b, c, d = tpl
print(f"a: {a}, b: {b}, c: {c}, d: {d}")