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


a = Adorno('00000', 'Jarrón', 15.50, 'Jarrón de porcelana con dibujos')

print(a)
