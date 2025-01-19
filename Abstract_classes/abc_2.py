from abc import ABC, abstractmethod


def abstractmethod_custom(fn):
    fn.__isabstractmethod__ = True
    return fn


def get_answer(fn):
    def inner(*args, **kwargs):
        return 42

    return inner


class AbstractBaseClass(ABC):

    @staticmethod
    @abstractmethod
    def abstract_static_method():
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def abstract_class_method(cls):
        raise NotImplementedError

    @property
    @abstractmethod
    def abstract_property(self):
        raise NotImplementedError

    @abstract_property.setter
    @abstractmethod
    def abstract_property(self, value):
        raise NotImplementedError


class ConcreteClass(AbstractBaseClass):

    @staticmethod
    def abstract_static_method():
        pass

    @classmethod
    def abstract_class_method(cls):
        pass

    @property
    def abstract_property(self):
        return 42


c = ConcreteClass()
