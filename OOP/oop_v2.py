class A:
    @staticmethod
    def magic():
        print(f'class A')


class B:
    @staticmethod
    def magic():
        print(f'class B')


# class C(A):  # A, B C A, ale nie może wstawić 2 razy tej samej klasy, chyba że X(B, C, A), wtedy drzewo się zgadza
class C:
    @staticmethod
    def magic():
        print(f'class C')


class X(A, B, C):
    pass
    # @staticmethod
    # def magic():
    #     print(f'class X')


x = X()
x.magic()
print(X.__mro__) # pokazuje w jakiej kolejności python szuka metod w klasach