import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE usuarios(
#         dni VARCHAR(9) PRIMARY KEY,
#         nomre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
#     ''')
#
# usuarios = [
#     ('11111111A', 'Javier', 18, 'javier@ejemplo.com'),
#     ('22222222B', 'Beatriz', 19, 'beatriz@ejemplo.com'),
#     ('33333333C', 'Nico', 20, 'nico@ejemplo.com'),
#     ('44444444D', 'Inés', 21, 'ines@ejemplo.com')
# ]
#
# cursor.executemany('INSERT INTO usuarios VALUES (?, ?, ?, ?)', usuarios )

# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
#     ''')

# productos = [
#     ('Teclado', 'Logitech', 19.95),
#     ('Pantalla 19"', 'LG', 89.95)
# ]
#
# cursor.executemany('INSERT INTO productos VALUES (null, ?, ?, ?)', productos)

# cursor.execute('SELECT * FROM productos')
#
# productos = cursor.fetchall()
# for producto in productos:
#     print(producto)

cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    )
''')

usuarios = [
    ('11111111A', 'Javier', 18, 'javier@ejemplo.com'),
    ('22222222B', 'Beatriz', 19, 'beatriz@ejemplo.com'),
    ('33333333C', 'Nico', 20, 'nico@ejemplo.com'),
    ('44444444D', 'Inés', 21, 'ines@ejemplo.com')
]

cursor.executemany('INSERT INTO usuarios VALUES (null, ?, ?, ?, ?)', usuarios)

conexion.commit()
conexion.close()
