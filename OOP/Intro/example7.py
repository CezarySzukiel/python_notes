class Employee:
    __slots__ = ("name", "age", "position", "salary")  # optymalizacja pamięci w py dla obiektów klasy Employee

    # istnieją tylko jeśli je stworzymy. od teraz klasa nie ma __dict__ i nie można dodawać nowych atrybutów po inicie

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)


class Tester(Employee):
    def run_tests(self):
        print(f"{self.name} is running tests")
        print("all tests passed")


class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, "__slots__")


class Developer(SlotsInspectorMixin, Employee):
    def __init__(self, name, age, position, salary, tech_stack):
        super().__init__(name, age, position, salary)
        self.tech_stack = tech_stack

    # def increase_salary(self, percent, bonus=0):
    #     self.salary += self.salary * (percent / 100) + bonus
    #     # overriding, gdy się nadpisuje metodę powinny mieć ten sam prototyp (ta sama ilość parametrów, te same typingi

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


e1 = Tester("Mateusz", 30, "Software Engineer C1", 10000)
e2 = Developer("Martyna", 35, "Software Engineer C1", 12000)


print(isinstance(e1, Tester))
print(isinstance(e1, Employee))
print(isinstance(e1, object))

print(issubclass(Developer, Employee))
print(issubclass(Developer, Tester))

try:
    raise FloatingPointError("Floating point error")
