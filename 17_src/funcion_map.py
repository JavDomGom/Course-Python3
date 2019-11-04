# numeros = [2, 5, 10, 23, 50, 33]

# def doblar(numero):
#     return numero*2
#
# m = map(doblar, numeros)
#
# print(next(m))
# print(next(m))

# print(list(map(lambda x: x*2, numeros)))

# # Multiplicar todos los elementos de una primera lista por los de una segunda
# # lista y por los de una tercera.
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# c = [11, 12, 13, 14, 15]
#
# print(list(map(lambda x,y,z: x*y*z, a, b, c)))

# Incrementar un año la edad de cada persona.
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

# def incrementar(persona):
#     persona.edad += 1
#     return persona
#
# personas = map(incrementar, personas)
#
# for persona in personas:
#     print(persona)

personas = map(lambda persona: Persona(persona.nombre, persona.edad+1), personas)

for persona in personas:
    print(persona)
