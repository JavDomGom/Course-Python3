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
patron = ['ho*'] # ['h', 'ho', 'hoo', 'hooo', 'hoooooo']

# Si encuentra el carácter "h" seguido del carácter "o" cero o más veces seguido de "la".
patron = ['ho*la'] # ['hla', 'hola', 'hoola', 'hooola', 'hoooooola']

# Si encuentra el carácter "h" seguido del carácter "u" cero o más veces seguido de "la".
patron = ['hu*la'] # ['hla']

## Meta-carácter "+": Una o más repeticiones de la letra a su izquierda.

# Si encuentra el carácter "h" seguido del carácter "o" una o más veces.
patron = ['ho+'] # ['ho', 'hoo', 'hooo', 'hoooooo']

## Meta-carácter "?": Una o ninguna repetición de la letra a su izquierda.

# Si encuentra el carácter "h" seguido del carácter "o" ninguna o una vez.
patron = ['ho?'] # ['h', 'ho', 'ho', 'ho', 'ho']

# Si encuentra el carácter "h" seguido del carácter "o" ninguna o una vez y luego "la".
patron = ['ho?la'] # ['hla', 'hola']

# Si encuentra el carácter "h" seguido del carácter "o" ninguna o una vez y luego "la".
patron = ['ho?la'] # ['hla', 'hola']

# Si encuentra el carácter "o" cero veces después de la "h".
patron = ['ho{0}la'] # ['hla']

# Si encuentra el carácter "o" solo una vez después de la "h".
patron = ['ho{1}la'] # ['hola']

# Si encuentra el carácter "o" un rango de entre cero y una veces después de la "h".
patron = ['ho{0,1}la'] # ['hla', 'hola']

# Si encuentra el carácter "o" un rango de entre dos y diez veces después de la "h".
patron = ['ho{2,10}la'] # ['hoola', 'hooola', 'hoooooola']

## Conjunto de carácteres

texto = 'hala hela hila hola hula'

patron = ['h[ou]la'] # ['hola', 'hula']

patron = ['h[aio]la'] # ['hala', 'hila', 'hola']

texto = 'haala heeela hiiiila hoooooola'

# Caracter "h" seguido de una "a" o "e" y luego "la".
patron = ['h[ae]la'] # []

# Caracter "h" seguido de cero o más veces "a" o "e" y luego "la".
patron = ['h[ae]*la'] # ['haala', 'heeela']

# Caracter "h" seguido de "i" o "o" entre 3 y nueve veces y luego "la".
patron = ['h[io]{3,9}la'] # ['hiiiila', 'hoooooola']

## Exclusión en conjunto de carácteres.

texto = 'hala hela hila hola hula'

# Caracter "h" seguido de cualquier vocal menos la "o" y luego "la".
patron = ['h[^o]la'] # ['hala', 'hela', 'hila', 'hula']

## Rangos

# [A-Z]: Cualquier carácter alfabético en mayúscula (no especial ni número).
# [a-z]: Cualquier carácter alfabético en minúscula (no especial ni número).
# [A-Za-z]: Cualquier carácter alfabético en mayúscula y minúscula (no especial ni número).
# [A-z]: Cualquier carácter alfabético en mayúscula y minúscula (no especial ni número).
# [0-9]Cualquier carácter numérico (no especial ni alfabético).
# [a-zA-Z0-9]Cualquier carácter alfanumérico (no especial).

texto = 'hola h0la Hola mola m0la M0la'

patron = ['h[a-z]la'] # ['hola']
patron = ['h[0-9]la'] # ['h0la']

# Cualquier carácter alfabético 4 veces.
patron = ['[A-z]{4}'] # ['hola', 'Hola', 'mola']

# Lo que empiece por mayúscula seguido de cualquier arácter alfanumérico 3 veces.
patron = ['[A-Z][A-z0-9]{3}'] # ['Hola', 'M0la']

## Carácteres escapados

# Código  Significado
# -------------------
# \d      numérico
# \D      no numérico
# \s      espacio en blanco
# \S      no espacio en blanco
# \w      alfanumérico
# \W      no alfanumérico

texto = 'Este curso de Python se publicó en 2016'

# Busca carácteres numéricos.
patron = [r'\d'] # ['2', '0', '1', '6']

# Busca carácteres numéricos que se repitan una o más veces.
patron = [r'\d+'] # ['2016']

# Busca carácteres no numéricos.
patron = [r'\D'] # ['E', 's', 't', 'e', ' ', 'c', 'u', 'r', 's', 'o', ' ', 'd', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 's', 'e', ' ', 'p', 'u', 'b', 'l', 'i', 'c', 'ó', ' ', 'e', 'n', ' ']

# Busca carácteres no numéricos que al menos se repitan una vez.
patron = [r'\D+'] # ['Este curso de Python se publicó en ']

# Busca espacios en blanco.
patron = [r'\s'] # [' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Busca no espacios en blanco.
patron = [r'\S'] # ['E', 's', 't', 'e', 'c', 'u', 'r', 's', 'o', 'd', 'e', 'P', 'y', 't', 'h', 'o', 'n', 's', 'e', 'p', 'u', 'b', 'l', 'i', 'c', 'ó', 'e', 'n', '2', '0', '1', '6']

# Busca no espacios en blanco una o más veces.
patron = [r'\S+'] # ['Este', 'curso', 'de', 'Python', 'se', 'publicó', 'en', '2016']

# Busca alfanuméricos.
patron = [r'\w'] # ['E', 's', 't', 'e', 'c', 'u', 'r', 's', 'o', 'd', 'e', 'P', 'y', 't', 'h', 'o', 'n', 's', 'e', 'p', 'u', 'b', 'l', 'i', 'c', 'ó', 'e', 'n', '2', '0', '1', '6']

# Busca alfanuméricos una o más veces.
patron = [r'\w+'] # ['Este', 'curso', 'de', 'Python', 'se', 'publicó', 'en', '2016']

# Busca no alfanuméricos.
patron = [r'\W'] # [' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Busca no alfanuméricos una o más veces.
patron = [r'\W+'] # [' ', ' ', ' ', ' ', ' ', ' ', ' ']

buscar(patron, texto)
