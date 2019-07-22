# Tipos de datos

## Números enteros y flotantes (decimales)

En Python 3 hay un tipo de datos para los números, concretamente para los números enteros y los flotantes o decimales. El intérprete de Python permite realizar con este tipo de datos cálculos simples como sumar, restar, multiplicar, dividir, operaciones módulo o potencias. Algunos ejemplos:

```python
>>> 1+2
3
>>> 7-2
5
>>> 5-9
-4
>>> 3*4
12
>>> 0.3*4
1.2
>>> 28/7
4.0
>>> 25%5
0
>>> 3**2
9
```

Se pueden realizar operaciones concatenadas más complejas. El orden correcto siempre será de izquierda a derecha, primero las multiplicaciones y divisiones, y luego las sumas y restas. Python se encargará de respetar el orden de los operadores automáticamente, por ejemplo:

```python
>>> 3-2+4*10
41
```
Como se puede ver, primero ha realizado la operación de multiplicación `4*10`, que da como resultado `40`, luego la operación resta `3-2`, que da como resultado `1`, y finalmente la suma `1+40`, que da como resultado `41`.

## Cadenas de carácteres

Otro tipo de datos son las cadenas de caracteres o cadenas de texto. Estas cadenas se pueden escribir dentro de unas comillas dobles (") o simples ('), por ejemplo:

```python
>>> 'Hola mundo!'
'Hola mundo!'
>>> "Hola mundo!"
'Hola mundo!'
```

Los dos ejemplos anteriores muestran un resultado por pantalla cuando se escribe una cadena de texto entre las comillas dobles o simples en el intérprete de Python, pero para poder tratar mejor estas cadenas de carácteres usaremos una función propia de Python llamada `print()`. No solo nos permitirá mostrar por pantalla el mensaje de texto que estamos escribiendo, si no que además es capaz de interpretar caracteres especiales como son las tabulaciones `\t`, los slatos de línea `n` y otros muchos más, de momento veremos estos dos, por emplo:

```python
>>> print('Hola\tmundo!')
Hola	mundo!
'Hola\nmundo!'
>>> print('Hola\nmundo!')
```

La función `print()` permite indicar si se quieren procesar o no los caracteres especiales como las tabulaciones o saltos de línea que hemos visto antes, ya que podría darse la casualidad de que nuestra cadena de texto incuya entre los carácteres `\n` o cualquier otro caracter especial. En este caso se le puede indicar que se quiere mostrar la cadena de testo en crudo o *raw* añadiéndo una letra `r` delante de las comillas simples o dobles que van dentro del paréntesis de la función `print()`, véase el ejemplo:

```python
>>> print(r'C:\nombre\de\un\directorio')
C:\nombre\de\un\directorio
```

Otra opción es escapar los caracteres que no queremos que se procesen, para ello se utiliza la contrabarra o *backslash* `\`, véase el ejemplo:

```python
>>> print('C:\\nombre\\de\\un\\directorio')
C:\nombre\de\un\directorio
```

Dentro de la función `print()` también se pueden realizar algunas operaciones con este tipo de dato de cadenas de carácteres, por ejemplo multiplicar un número de veces una cadena de texto como `Hola`:

```python
>>> print('Hola'*3)
HolaHolaHola
```

O sumar dos cadenas, en realidad no se realiza una suma algebráica, si no una concatenación de una cadena con otra, véase elejemplo:

```python
>>> print('Hola' + 'mundo')
Holamundo
>>> print('Hola' + ' ' + 'mundo')
Hola mundo
```

## Listas

Las listas es un tipo de datos en Python que permite agrupar diferentes elementos o *items*, e incluso siendo estos de diferentes tipos, como carácteres, números enteros y flotantes, cadenas de caracteres, e incluso otras listas. Se definen entre corchetes "[ ]" y sus elementos han de ir separados por una coma.

```python
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> ['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e']
>>> [1, 'Hola', -27, 'b', 3.14]
[1, 'Hola', -27, 'b', 3.14]
```