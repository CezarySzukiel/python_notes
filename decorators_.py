def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner


@capitalize
def hello(name):
    return f"Hello, {name}"


@capitalize
def goodbye(name):
    return f"Goodbye, {name}"


print(hello("jarek"))
print(goodbye("lech"))
