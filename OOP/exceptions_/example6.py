# context manager

class ContextManagerCustom:
    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')
        if exc_type is not None:
            print(f"Exception occured: {exc_type.__name__}")
            return False
        return True


with ContextManagerCustom() as cm:
    raise Exception('Some error')