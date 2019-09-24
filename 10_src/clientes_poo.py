class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print('Cliente no encontrado')

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), '--> Borrado')
                return
        print('Cliente no encontrado')

javier = Cliente(nombre='Javier', apellidos='Dominguez', dni='00000000A')
beatriz = Cliente('11111111B', 'Beatriz', 'Gimenez')

empresa = Empresa(clientes=[javier, beatriz])

print(empresa.clientes)
empresa.mostrar_cliente(dni='00000000A')
empresa.borrar_cliente(dni='11111111B')
print(empresa.clientes)
