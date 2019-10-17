from io import open

fichero = open('fichero.txt', 'r+')

lineas = fichero.readlines()
lineas[2] = 'Linea modificada.'

fichero.seek(0)
fichero.writelines(lineas)
fichero.seek(0)

texto = fichero.read()

fichero.close()

print(texto)
