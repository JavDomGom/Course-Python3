class Pelicula:

    # Contructor de clase.
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película {}'.format(self.titulo))

    # Redefinimos el método string
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)

p1 = Pelicula('El padrino', 175, 1972)

c = Catalogo([p1])
c.agregar(Pelicula('El padrino II', 202, 1974))

c.mostrar()
