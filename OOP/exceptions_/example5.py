def magic(value):
    assert value != 42, "Custom message"
    return value


try:
    magic(42)
except AssertionError as e:
    print(e)