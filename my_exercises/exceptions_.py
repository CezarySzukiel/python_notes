user_input = "0"  # Spróbuj też np. "zero" albo "2"

try:
    number = int(user_input)
    result = 10 / number
    print(f"Wynik: {result}")
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")
except ZeroDivisionError:
    print("Nie można dzielić przez zero.")



def risky_code():
    try:
        return 10 / 0  # ZeroDivisionError
    except Exception:
        print("Ups... coś nie zadziałało")
        return None

result = risky_code()
print(result)