class A:
    def __init__(self):
        print('Soy de clase A')


class B:
    def __init__(self):
        print('Soy de clase B')


class C(B, A):
    pass

c = C()
