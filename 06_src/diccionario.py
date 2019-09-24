alumnos = []

a = {'Nombre': 'Javier', 'Curso': 1, 'Clase': 'A'}
alumnos.append(a)

a = {'Nombre': 'Alice', 'Curso': 2, 'Clase': 'C'}
alumnos.append(a)

a = {'Nombre': 'Bob', 'Curso': 3, 'Clase': 'B'}
alumnos.append(a)

for a in alumnos:
    print(a['Nombre'], a['Curso'], a['Clase'])
