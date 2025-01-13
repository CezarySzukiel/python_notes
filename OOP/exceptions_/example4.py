from collections.abc import Callable


def get_user_name() -> str:
    user_name = input("Enter your name: \n")
    if len(user_name.strip()) == 0:
        raise ValueError("Empty name")

    return user_name


def handle_user_name(cb: Callable[[], str]) -> str:
    while True:
        try:
            return cb()
        except ValueError as e:
            print(e)
            continue


if __name__ == '__main__':
    user_name = handle_user_name(get_user_name)
    print(f"Hello {user_name}")
