# employee1_name = "Mateusz"
# employee1_age = 30
# employee1_position = "Software Engineer"
# employee1_salary = 10000
#
# employee2_name = "Martyna"
# employee2_age = 35
# employee2_position = "Senior Python Developer"
# employee2_salary = 12000

# employee1 = ["Mateusz", 30, "Software Engineer", 10000]
# employee2 = ["Martyna", 35, "Senior Python Developer", 12000]
#
# name = lambda employee: employee[0]
# age = lambda employee: employee[1]
# position = lambda employee: employee[2]
# salary = lambda employee: employee[3]

# utrzymanie takich danych jest trudne


employee1 = {
    "name": "Mateusz",
    "age": 30,
    "position": "Software Engineer",
    "salary": 10000,
}

employee2 = {
    "name": "Martyna",
    "age": 35,
    "position": "Senior Python Developer",
    "salary": 12000,
}


def init_employee(name, age, position, salary):
    return {
        "name": name,
        "age": age,
        "position": position,
        "salary": salary,
    }


employee3 = init_employee("Cezary", 34, "Frontend Developer", 8000)

print(employee3)


def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] * (percent / 100)


#   używa referencji do obiektu
#   łamie pure function


def employee_info(employee):
    return f'{employee["name"]} is {employee["position"]} and earns {employee["salary"]}'


employees = [employee1, employee2, employee3]

increase_salary(employee3, 10)

for employee in employees:
    print(employee_info(employee))
