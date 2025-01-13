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

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(f'{key}={val!r}' for key, val in vars(self).items())})"


    @property
    def salary(self, salary):
        if salary < 10000:
            raise ValueError("Salary too low")
        self._salary = salary

    @salary.setter
    def salary(self):
        return self._salary

    @salary.deleter
    def salary(self):
        del self._salary

    @property
    def salart_gross(self):
        return self.salary * 1.23


e1 = Employee("Mateusz", 30, "Software Engineer C1", 10000)
e2 = Employee("Martyna", 35, "Software Engineer C1", 12000)

team = e1 + e2
print(team)