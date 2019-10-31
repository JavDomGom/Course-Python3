import sqlite3

conexion = sqlite3.connect('ejemplo.db')

cursor = conexion.cursor()
# cursor.execute('CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))')
# cursor.execute('INSERT INTO usuarios VALUES ("Richard", 66, "rms@gnu.org")')
# cursor.execute('SELECT * FROM usuarios')
# usuario = cursor.fetchone()

# usuarios = [
#     ('Beatriz', 18, 'beatriz@ejemplo.com'),
#     ('Nico', 19, 'nico@ejemplo.com'),
#     ('Inés', 20, 'ines@ejemplo.com')
# ]
#
# cursor.executemany('INSERT INTO usuarios VALUES (?, ?, ?)', usuarios)

cursor.execute('SELECT * FROM usuarios')

usuarios = cursor.fetchall()

for usuario in usuarios:
    print('Nombre:{}\tEdad: {}\tEmail:{}'.format(usuario[0], usuario[1], usuario[2]))

conexion.commit()
conexion.close()
