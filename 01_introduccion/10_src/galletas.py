class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        self.chocolate = False

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('Si tiene chocolate')
        else:
            print('No tiene chocolate')

g1 = Galleta('salada', 'amarilla')
g2 = Galleta('dulce', 'verde')

print('\nEstado actual de las galletas')
g1.tiene_chocolate()
g2.tiene_chocolate()

print('\nAñado chocolate a la primera galleta ...')
g1.chocolatear()

print('\nEstado actual de las galletas')
g1.tiene_chocolate()
g2.tiene_chocolate()
