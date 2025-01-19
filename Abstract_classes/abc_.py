from abc import ABCMeta, ABC, abstractmethod


class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return issubclass(type(instance), cls)

    def __subclasscheck__(cls, subclass):
        if (
                hasattr(subclass, "swipe") and callable(subclass.swipe)
                and
                hasattr(subclass, "sharpen") and callable(subclass.sharpen)
        ):
            return True
        return super().__subclasscheck__(subclass)


class Sword(ABC):
    """Abstract Base Class"""

    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def sharpen(self):
        raise NotImplementedError

    def thrust(self):
        print("Thrust!", type(self).__name__)


class BroadSword:
    def swipe(self):
        print("Swoosh!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)


class SamuraiSword:
    def swipe(self):
        print("Slice!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)


class Rifle:
    def fire(self):
        print("Bang!!", type(self).__name__)


class Sabre(Sword):
    def swipe(self):
        print("Boom!", type(self).__name__)

    def sharpen(self):
        print("Shink!", type(self).__name__)


@Sword.register
class LightSabre:
    def swipe(self):
        print("Ffffkrrrrshhzzzwooooom..wooom..wooom!", type(self).__name__)


# Sword.register(LightSabre)

samurai_sword = SamuraiSword()
rifle = Rifle()
sabre = Sabre()
# print(LightSabre.__mro__)
print(issubclass(LightSabre, Sword))
print(issubclass(SamuraiSword, Sword))
# print(isinstance(samurai_sword, Sword))
samurai_sword.thrust()