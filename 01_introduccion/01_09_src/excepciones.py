lista = [1, 2, 3]


def comprueba_lista(l):
    print(l)
    if len(l) > 0:
        l.pop()
        comprueba_lista(l)

comprueba_lista(lista)
