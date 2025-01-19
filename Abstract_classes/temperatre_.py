import functools
import inspect


def post_condition(predicate):
    def function_decorator(fn):
        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            result = fn(self, *args, **kwargs)
            if not predicate(self):
                r = object.__repr__(self)
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {r}."
                )
            return result

        return wrapper

    return function_decorator


class InvariantProperty:
    def __init__(self, referent, predicate):
        self._referent = referent
        self._predicate = predicate

    def _check_predicate(self, instance):
        if not self._predicate(instance):
            r = object.__repr__(instance)
            raise RuntimeError(
                f"Post-condition {self._predicate.__name__} not "
                f"maintained for {r}."
            )

    def __get__(self, instance, owner):
        result = self._referent.__get__(instance, owner)
        if instance is not None:
            self._check_predicate(instance)
        return result

    def __set__(self, instance, value):
        self._referent.__set__(instance, value)
        self._check_predicate(instance)

    def __delete__(self, instance):
        self._referent.__delete__(instance)
        self._check_predicate(instance)

    @property
    def __isabstractmethod__(self):
        return getattr(self._referent, "__isabstractmethod__", False)


def invariant(predicate):
    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                function_decorator = post_condition(predicate)
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)
            elif isinstance(member, property):
                proxy_property = InvariantProperty(member, predicate)
                setattr(cls, name, proxy_property)
        return cls

    return class_decorator


def above_absolute_zero(temperature):
    return temperature._kelvin >= 0


@invariant(above_absolute_zero)
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin

    def get_kelvin(self):
        return self._kelvin

    def set_kelvin(self, value):
        self._kelvin = value

    @property
    def celsius(self):
        return self._kelvin - 273.15

    @celsius.setter
    def celsius(self, value):
        self._kelvin = value + 273.15

    def __repr__(self):
        return f"{type(self).__name__}(kelvin={self._kelvin})"


t = Temperature(0)
t.set_kelvin(10)
t.celsius = 100
# print(t.get_kelvin())
# print(vars(Temperature))