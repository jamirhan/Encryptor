class A:
    def fun(self):
        print('meh')

    def gun(self):
        self.fun()


class B(A):
    def fun(self):
        print('geh')


g = B()
g.gun()
