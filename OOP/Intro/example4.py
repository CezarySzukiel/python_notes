class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return f'{self.name} is {self.position} and earns {self.salary}'

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
            # Jeśli użyjemy klasy notimplemented do zostanie zwrócony __add__ z klasy drugiego elementu
        return type(self)(self.name, self.age, self.position, self.salary

    def __repr__(self):
        # return f"{type(self).__name__}({self.name!r}, {self.age!r}, {self.position!r}, {self.salary!r})"
        return f"{type(self).__name__}({', '.join(f'{key}={val!r}' for key, val in vars(self).items())})"
        # generic repr
        # vars zwraca __dict__ obiektu

# !r wywołuje dunder format co wywołuje repra

e1 = Employee("Mateusz", 30, "Software Engineer C1", 10000)
e2 = Employee("Martyna", 35, "Software Engineer C1", 12000)

team = e1 + e2
print(team)

