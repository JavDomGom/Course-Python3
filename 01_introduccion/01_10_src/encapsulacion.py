class Ejemplo:
    __atributo_privado = 'Soy un atributo inalcanzable desde fuera.'

    def __metodo_privado(self):
        print('Soy un método inalcanzable desde fuera.')

    def mostrar_atributo(self):
        return self.__atributo_privado

    def mostrar_metodo(self):
        return self.__metodo_privado()

e = Ejemplo()

e.mostrar_metodo()
