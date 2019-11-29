import re

# texto = 'En esta cadena se encuentra una palabra mágica'
#
# # # Buscar si en texto se encuentra la palabra "mágica".
# # print(re.search('mágica', texto)) # Esto puede devolver dos cosas: un objeto ó None.
#
# palabra = 'mágica'
#
# # re.search: Buscar un patrón en una cadena.
# encontrado = re.search(palabra, texto)
#
# if encontrado is not None:
#     print('Se ha encontrado la palabra.')
# else:
#     print('No se ha encontrado la palabra.')
#
# # Saber en qué posicion de la cadena texto aparece la plabara "mágica".
# print(encontrado.start())
#
# # Saber en qué posicion de la cadena texto termina la plabara "mágica".
# print(encontrado.end())

# # re.match: Buscar un patrón al principio de otra cadena.
# texto = 'Hola mundo!'
# print(re.match('Hola', texto)) # Devuelve un objeto.
# print(re.match('Mola', texto)) # Devuelve None.

# # re.split: Dividir una cadena a partir de un patrón.
# texto = 'Vamos a dividir esta cadena'
# print(re.split(' ', texto)) # ['Vamos', 'a', 'dividir', 'esta', 'cadena']

# # re.sub: Sustituye todas las coincidencias en una cadena.
# texto = 'Hola amigo'
# print(re.sub('amigo', 'amiga', texto)) # Hola amiga

# # re.findall: Buscar todas las coincidencias en una cadena.
# texto = 'hola adios hola hola hello'
# print(re.findall('hola', texto)) # ['hola', 'hola', 'hola']
# print(re.findall('hola|hello', texto)) # ['hola', 'hola', 'hola', 'hello']

# Patrones con sintaxis repetida.
texto = 'hla hola hoola hooola hoooooola'

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

## Meta-carácter "*": Ninguna o más repeticiones de la letra a su izquierda.

# Si encuentra el carácter "h" seguido del carácter "o" cero o más veces.
patrones = ['ho*'] # ['h', 'ho', 'hoo', 'hooo', 'hoooooo']

# Si encuentra el carácter "h" seguido del carácter "o" cero o más veces seguido de "la".
patrones = ['ho*la'] # ['hla', 'hola', 'hoola', 'hooola', 'hoooooola']

# Si encuentra el carácter "h" seguido del carácter "u" cero o más veces seguido de "la".
patrones = ['hu*la'] # ['hla']

## Meta-carácter "+": Una o más repeticiones de la letra a su izquierda.

# Si encuentra el carácter "h" seguido del carácter "o" una o más veces.
patrones = ['ho+'] # ['ho', 'hoo', 'hooo', 'hoooooo']

## Meta-carácter "?": Una o ninguna repetición de la letra a su izquierda.

# Si encuentra el carácter "h" seguido del carácter "o" ninguna o una vez.
patrones = ['ho?'] # ['h', 'ho', 'ho', 'ho', 'ho']

# Si encuentra el carácter "h" seguido del carácter "o" ninguna o una vez y luego "la".
patrones = ['ho?la'] # ['hla', 'hola']

buscar(patrones, texto)
