def exception_ultimate_example(value):
    match value:
        case 1:
            # temp_c(-280)
            raise ValueError("1 is not allowed")
        case 2:
            # add(1, "ala")
            raise TypeError("2 is not type of string")
        case 3:
            # [1, 2, 3,][41]
            raise IndexError("3 is not in range")
        case 4:
            raise KeyError("4 is not in dict")
        case 5:
            raise ZeroDivisionError("5 is not allowed")
        case 6:
            # any exception
            raise Exception("6 is not allowed")
        case _:
            return 42


def never(value):
    raise NotImplementedError("This function is not implemented yet")

# robimy exception do kazdego przypadku. nie za pomocą tupli, chyba że chcemy kilka przypadków obsłużyć tak samo
try:
    result = exception_ultimate_example(1)
except ValueError as e:
    "???"
except TypeError as e:
    "???"
except IndexError as e:
    "???"
except KeyError as e:
    "???"
except ArithmeticError as e:
    "???"
else:
    print("Else block")
finally:
    print("Finally block")

try:
   never(result)
except NotImplementedError as e:
    "???"
except ReferenceError as e:
    print("reference error")
except NameError as e:
    print("name error")
