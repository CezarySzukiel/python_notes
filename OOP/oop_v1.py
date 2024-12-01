from collections.abc import Sized, Sequence, Container, Iterator, Iterable
# class - namespace (schema), szablon dla obiektów, które chcemy tworzyć. Schemat.
#     namespace, przestrzeń nazewnicza: en:
from typing import Any

from tornado.options import define


# class keyword
# pascal case (upper camel case)
# syntatic sugar = lukier składniowy inna składnia do jakiejś funkcjonalności

# NameFour = type('NameFour', (object,), attrs)
# nf = NameFour(666)
#
#
# # print(nf.x, nf.value)
#
#
# # class
#
# class NameFive:
#     def __new__(cls, *args: Any, **kwargs: Any) -> "NameFive":
#         self = super().__new__(cls)
#         return self
#
#     def __init__(self, value):
#         self.value = value
#         self.temp = 42
#
#
# # constructor - __new__
# # initializer - __init__
# n_five = NameFive(666)
# print(n_five.value)

# object- najwyższa klasa w pythonie, zawsze musi być w drzewie dziedziczenia.
# type to najwyższa metaclassa w pythonie
# bez syntatic sugar:
# class NameTwo(object, metaclass=type, other_params='value'):
#     pass


# by metaclass: oto dowód n to żę metaclassy tworzą klasy, bo type jest metaclassą`
# NameThree = type("NameThree", (), {})
#
# #  by metaclass with attributes:
# def init_(self, x):
#     self.x = x
# attrs ={
#     "__init__": init_,
#     "value": 42
# }
#
#
# NameFour = type('NameFour', (object,), attrs)
# nf = NameFour(666)


# print(nf.x, nf.value)


# class

# class NameFive:
#     def __new__(cls, *args: Any, **kwargs: Any) -> "NameFive":
#         self = super().__new__(cls)
#         return self
#
#     def __init__(self, value):
#         self.value = value
#         self.temp = 42


# constructor - __new__
# initializer - __init__
# n_five = NameFive(666)
# print(n_five.value)

# type inference - auto wykrywanie typu
class Auto:
    color = 'red' # share state, wszystkie obiekty utworzone z tej klasy będą mieć tą samą wartość, ale mogę zmienić wartość dla obiektu np dla bmw.color = 'black', jednocześnie ten obiekt nie ma żadnego zasięgu
    # pole klasy modyfikujemy tylko z poziomu klasy, nie z poziomu obiektu  (color to pole klasy)
    def __init__(self, model: str, max_speed: int, year: int) -> None:
        self.year = year
        self.max_speed = max_speed
        self.model = model
        self.engine = True
        self._color = type(self).color # tak to należy robić
        self.speed = 0

    def speed_up(self, amount: int) -> None:
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)

    def pimp(self, amouunt):
        self.nitro = True # niebezpieczna praktyka

    def magic(self, new_color):
        type(self).color = new_color # zmiana wartości pola klasy

    @classmethod # klass method manipuluje klasą, zwykła manipuluje obiektem, dlatego nie ma self, tylko cls
    def auto_nitro(cls, model: str, max_speed: int, year: int, nitro: bool) -> "Auto":
        self = super().__new__(cls) # tak samo można zapisać: self = cls.__new__(cls)
        self.__init__(model, max_speed, year)
        self.nitro = nitro
        return self

    @staticmethod # metoda statyczna to metoda która mogła by być funkcją, gdyby ją wyjąć poza klasę., jednak metoda jest logicznie związana z klasą, więc zostaje w klasie. (metoda, która nie ma świadomości klasowej)
    def magic():
        return "brum!!"

    def __Len__(self) -> int:
        return 42

    def __str__(self) -> str:
        return f"{self.model}"


bmw = Auto("E46", 180, 1995)
fiat = Auto("Uno", 240, 1999)
bmw.yolo = "black" # dynamiczne dodawanie atrybutów, bardzo zła praktyka
bmw.pimp("nitro")


# print(Auto.color)
# print(bmw.color) # nie znajduje color w obiekcie, więc szuka w klasie i tam jest
# print(fiat.color)
# print(vars(Auto)) # słownik ze wszystkimi property klasy, odwołuje się do __dict__
#
# # syntatic sugar
# bmw.speed_up(300) # metoda należy do klasy, nie obiektu
#
# Auto.speed_up(bmw, 300) # to samo co wyżej, ale bez syntatic sugar, ale po to się wprowadza syntatic sugar, żeby było czytelniej i żeby go używać
#
# print(bmw.speed)
# print(dir(Auto))
#
# toyota = Auto.auto_nitro("auris", 270, 1990, True)
# print(toyota.nitro)

print(len(bmw)) # pisząc def __Len__ ... w klasie dostaję możliwość wywołania len(bmw), podczas gdy normalnie bmw nie ma len
print(bmw.__len__())

# py ma low level api zbudowane na python features
# ale pomiędzy low level api a high api jest potężna optymalizacja. odwoływanie się do low level api poprzez dunder metody powoduje wyłączenie optymalizacji

# jak wyświetlić drzewo dziedziczenia:
print(Auto.__mro__) # method resolution order
print(issubclass(Auto, object)) # sprawdza czy Auto jest podklasą object
print(issubclass(Auto, Sized)) # sprawdza czy Auto jest podklasą Sized, to jest wirtualne dziedziczenie, bo Auto nie dziedziczy po Sized, ale ma metodę __len__, więc jest traktowane jakby dziedziczyło po Sized

