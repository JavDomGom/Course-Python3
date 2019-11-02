import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

# cursor.execute('SELECT * FROM usuarios WHERE edad=19')
# cursor.execute('UPDATE usuarios SET nombre="Javier Dominguez", edad=18 WHERE dni="11111111A"')
cursor.execute('DELETE FROM usuarios WHERE dni="11111111A"')

conexion.commit()
conexion.close()
