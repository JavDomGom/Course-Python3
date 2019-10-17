import pickle

fichero = open('lista.bin', 'rb')

lista = pickle.load(fichero)

fichero.close()

print(lista)
