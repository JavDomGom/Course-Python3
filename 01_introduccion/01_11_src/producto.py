class Producto:

    def __init__(self, referencia, tipo, nombre, pvp, descripcion, productor=None, distribuidor=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.autor = autor

adorno = Producto('000A', 'Adorno', 'Jarrón', 15, 'Jarrón de porcelana con dibujos')

print(adorno.tipo)
print(adorno.descripcion)
