clientes = [
    {'nombre': 'Richard', 'apellidos': 'Stallman', 'dni': '01234567A'},
    {'nombre': 'Aaron', 'apellidos': 'Swartz', 'dni': '98765432Z'}
]


def mostrar_cliente(clientes, dni):
    for c in clientes:
        if dni == c['dni']:
            print('{} {}'.format(c['nombre'], c['apellidos']))
            return   # Si se encuentra el cliente se sale de la iteración.

    print('Clente no encontrado.')


def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if dni == c['dni']:
            del clientes[i]
            print(str(c), '--> Borrado')
            return   # Si se encuentra el cliente se sale de la iteración.

    print('Clente no encontrado.')


print(clientes)
borrar_cliente(clientes, '01234567A')
print(clientes)
