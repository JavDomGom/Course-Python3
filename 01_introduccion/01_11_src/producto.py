import copy


class Producto:

    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)


class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ''
    distribuidor = ''

    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


class Libro(Producto):
    isbn = ''
    autor = ''

    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio."""
    p.pvp -= (p.pvp / 100 * rebaja)
    return p


ad = Adorno('00000', 'Jarrón', 15.50, 'Jarrón de porcelana con dibujos')

al = Alimento('00001', 'Aceite de Oliva', 5, 'Botella de aceite de oliva virgen extra')
al.productor = 'La aceitera'
al.distribuidor = 'Distribuciones S.A.'

al_rebajado = rebajar_producto(al, 10)

print(al_rebajado)
print(al)

# li = Libro('00002', 'El enemigo conoce el sistema', 17.90, 'Libro sobre redes de hiper vigilancia')
# li.isbn = '8417636390'
# li.autor = 'Marta Peirano'

# productos = [al, li]

# productos.append(ad)

# for p in productos:
#     if isinstance(p, Adorno):
#         print(p.referencia, p.nombre)
#     elif isinstance(p, Alimento):
#         print(p.referencia, p.nombre, p.productor)
#     elif isinstance(p, Libro):
#         print(p.referencia, p.nombre, p.isbn)

lista_1 = [1, 2, 3]
lista_2 = lista_1

lista_2.append(4)
print(lista_1)
