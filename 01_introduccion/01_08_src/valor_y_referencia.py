def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns[:])

print(ns)
