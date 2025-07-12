class A:
    def say_hello(self):
        return "Hello from A"


class B:
    def say_hello(self):
        return f"Hello from B {self.__class__.__class__}"


class C(A, B):
    pass


b = B()
c = C()
print(c.say_hello())  # Hello from A

print(b.say_hello())
