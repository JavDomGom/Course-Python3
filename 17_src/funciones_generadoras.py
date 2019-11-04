def pares(n):
    for numero in range(n+1):
        if numero % 2 == 0:
            yield numero

for numero in pares(10):
    print(numero)

print([numero for numero in pares(10)])

pares = pares(3)

print(next(pares))
print(next(pares))

lista = [1, 2, 3, 4, 5]
lista_iterable = iter(lista)

print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))
print(next(lista_iterable))

cadena = 'hola'
cadena_iterable = iter(cadena)

print(next(cadena_iterable))
print(next(cadena_iterable))
print(next(cadena_iterable))
