# Ask for forgiveness rather than permission.
x = 0
if x != 0:
    print(10 / x)  # ask for permission

try:  # ask for forgiveness
    10 / x
except ZeroDivisionError:
    print("Division by zero")


class Vector(object):
    def __init__(self, **components):
        protected_components = {f'_{key}': value for key, value in components.items()}
        self.__dict__.update(protected_components)

    def __getattr__(self, name):
        protected_name = f"_{name}"
        try:
            return self.__dict__[protected_name]
        except KeyError:
            raise AttributeError(f"{self!r} has no attribute {name!r}")

    def __setattr__(self, name, value):
        raise AttributeError(f"Can't set attribute {name!r}")

    def __delattr__(self, name):
        # delattr(self, f"_{name}")
        raise AttributeError(f"Can't delete attribute {name!r}")

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(
            f'{key}={value}' for key, value in self._args().items()
        )})"

    def _args(self):
        return {key[1:]: value for key, value in self.__dict__.items()}


# jeśli chcemy wyszukać atrybut klasy, to najpierw wywołuje się __getattribute__, a jeśli nie ma takiego atrybutu, to wywołuje się __getattr__
# v = Vector(x=1, y=2)
# v2 = Vector(p=1, q=2)
# print(v)
# v.__dict__["z"] = 42
# del v.__dict__["x"]
# print(v.__dict__)
# print(v2.__dict__)
# print(v.__getattr__("x"))
# print(v.z)
#
# print(getattr(v, "z"))
# print(hasattr(v, "z"))
# delattr(v, "z")

class ColoredVector(Vector):
    COLOR_INDEX = ("red", "green", "blue")

    def __init__(self, red, green, blue, **components):
        super().__init__(**components)
        self.__dict__["_color"] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = type(self).COLOR_INDEX.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__["_color"][channel]

    def __setattr__(self, name, value):
        try:
            channel = type(self).COLOR_INDEX.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__["_color"][channel] = value

    def _args(self):
        args = {color_name: getattr(self, color_name) for color_name in type(self).COLOR_INDEX}
        args.update(super()._args())  # wywołuję metodę z klasy bazowej w kontekście klasy dziedziczącej
        del args["color"]
        return args


# Proxy Logging logger, który zapisuje wszystkie wywołania każdego atrybutu. ma działać dla dowolnego obiektu, czyli ma być transparentnu

class LoggingProxy:
    def __init__(self, target):
        super().__setattr__("target", target)

    def __getattribute__(self, name):
        target = super().__getattribute__("target")
        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError(
                f"{super().__getattribute__('__class__').__name__}"
                f" could not forward request {name} to {target}"
            ) from e

        print(f"Retrieved attribute {name} = {value}")
        return value

    def __setattr__(self, name, value):
        target = super().__getattribute__("target")
        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError(
                f"{super().__getattribute__('__class__').__name__}"
                f" could not forward request {name} to {target}"
            ) from e

        print(f"Set attribute {name} = {value!r} on {target!r}")

    def __repr__ (self):
        target = super().__getattribute__("target")
        return repr(target)


v1 = ColoredVector(red=1, green=2, blue=3, x=1, y=2)
lp = LoggingProxy(v1)

print(lp.__repr__())
print(repr(lp))  # w py są optymalizacje wydajnościowe i są funkcje, które omijają __getattribute__
