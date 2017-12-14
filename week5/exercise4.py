class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")

# obj = D()
# obj.a returns 4
# obj.y() returns C.y
# some attributes are defined by __init__ and some by inheritance.
# If by init then when you run the init functions, if two of them define the same thing, then the last one overwrites the first one and you're left with the last version initialized. The last one wins.
## Inheritance works the opposite way - you go up the tree, searching left & up first but as soon as you find the attribute/method you stop so there is no overwriting, the first one wins.

# so,questions:
# init: obj.a was defined in C.init, then overwritten by B.init so it was 4 for a moment then it was 2. When you ask for it, there is no inheritance NONE .... why? because you already had that value for running the two inits as part of D's init.
# obj.y was NOT defined as part of the init process so unlike a, it will have to be found by inheritance. So, left to right depth first. Look at C. Found it. Stop.
