from io import open

texto = 'Esta es una línea de texto.\nY esta es otra línea de texto.\n'

fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()
