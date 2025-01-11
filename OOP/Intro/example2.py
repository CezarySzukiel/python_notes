# class Employee:
#     pass
#
#
# e = Employee()
# print(e)
# print(e.__dict__) # {}

# class Employee:
#     def __init__(self):
#         self.__dict__["name"] = "Mateusz"
#         self.__dict__["age"] = 30
#         self.__dict__["position"] = "Software Engineer"
#         self.__dict__["salary"] = 10000
#
#
# e = Employee()
# print(e.__dict__) # {'name': 'Mateusz', 'age': 30, 'position': 'Software Engineer', 'salary': 10000}

# class Employee:
#     def __init__(self):
#         self.name = "Mateusz"
#         self.age = 30
#         self.position = "Software Engineer"
#         self.salary = 10000


# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
# e = Employee("Mateusz", 30, "Software Engineer", 10000)

# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
#     def increase_salary(self, percent):
#         self.salary += self.salary * (percent / 100)
#
#     def info(self):
#         return f'{self.name} is {self.position} and earns {self.salary}'
#
#
# e = Employee("Mateusz", 30, "Software Engineer", 10000)
#
# Employee.increase_salary(e, 20)
# e.increase_salary(20)
# print(e.info())

# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
#     def increase_salary(self, percent):
#         self.salary += self.salary * (percent / 100)
#
#     def info(self):
#         return f'{self.name} is {self.position} and earns {self.salary}'
#
#
# e = Employee("Mateusz", 30, "Software Engineer", 10000)
#
# Employee.increase_salary(e, 20)
# e.increase_salary(20)
# print(e.info())

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
        # return f"{type(self).__name__}({self.name!r}, {self.age!r}, {self.position!r}, {self.salary!r})"
        return f"{type(self).__name__}({', '.join(f'{key}={val!r}' for key, val in vars(self).items())})"
        # generic repr
        # vars zwraca __dict__ obiektu

# !r wywołuje dunder format co wywołuje repra

e = Employee("Mateusz", 30, "Software Engineer", 10000)

Employee.increase_salary(e, 20)
e.increase_salary(20)
print(e.info())
print(vars(e))
print(repr(e))
