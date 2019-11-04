# Comprobar qué numero es múltiplo de 5.
numeros = [2, 5, 10, 23, 50, 33]

# def multiple(numero):
#     if numero%5 == 0:
#         return True
#
# print(list(filter(multiple, numeros)))

# print(list(filter(lambda numero: numero%5 == 0, numeros)))

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return '{} de {} años.'.format(self.nombre, self.edad)

personas = [
    Persona('Javier', 16),
    Persona('Beatriz', 17),
    Persona('Nico', 18),
    Persona('Inés', 19)
]

menores = filter(lambda persona: persona.edad < 18, personas)

for menor in menores:
    print(menor)
