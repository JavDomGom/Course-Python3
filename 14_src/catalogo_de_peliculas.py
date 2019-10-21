from io import open
import pickle

class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    fichero_catalogo = 'catalogo.bin'
    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def eliminar(self):
        if len(self.peliculas) > 0:
            indice = int(input('Introduzca el número de película que quiere borrar: ')) - 1

            if indice >= 0 and indice <= len(self.peliculas):
                print('Borrando película "{}" del catalogo ...'.format(self.peliculas[indice]))
                del self.peliculas[indice]
                self.guardar()
    def mostrar(self):
        print('Lista de películas existentes:\n')
        if len(self.peliculas) == 0:
            print('El catálogo está vacío')
            return
        for i, p in enumerate(self.peliculas):
            print('\t{}. {}'.format(i + 1, p))

    def cargar(self):
        fichero = open(self.fichero_catalogo, 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print('Catalogo vacío, generando uno nuevo ...')
        finally:
            fichero.close()
            print('Se han cargado {} películas'.format(len(self.peliculas)))

    def guardar(self):
        fichero = open(self.fichero_catalogo, 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()


# Se crea un objeto catálogo.
c = Catalogo()

print('\n MENU \n======')

while True:
    print('\n1: Mostrar catálogo de películas')
    print('2: Añadir película nueva')
    print('3: Eliminar película')
    print('4: Salir\n')

    user_choice = input('Selecciona una opción: ')

    if user_choice == '1':
        c.mostrar()
    elif user_choice == '2':
        titulo = input('Introduzca un título: ')
        duracion = int(input('Introduzca una duración en minutos: '))
        lanzamiento = int(input('Introduzca el año de lanzamiento: '))
        c.agregar(Pelicula(titulo, duracion, lanzamiento))
    elif user_choice == '3':
        c.mostrar()
        c.eliminar()
    elif user_choice == '4':
        print('Saliendo del programa!')
        break
    else:
        print('Opción no válida, vuelve a intentarlo.\n')
