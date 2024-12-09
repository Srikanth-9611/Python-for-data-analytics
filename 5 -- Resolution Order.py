class A:
    def show(self):
        print("Method in Class A")
class B(A):
    def show(self):
        print("Method in Class B")
class C(A):
    def show(self):
        print("Method in Class C")
class D(B, C):
    pass
d = D()
d.show()
("Method Resolution Order for D:", D.__mro__)