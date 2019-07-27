# Tipos de datos

## Variables y constantes

En Python, como en la mayoría de lenguajes de programación, se puede asignar un tipo de dato a una variable o a una constante. Ambos son un nombre o alias que almacenará un tipo de dato en memoria durante la ejecución del programa. La diferencia técnica es que el valor de una variable puede variar durante la ejecución, sin embargo el valor de una constante no debería cambiar.

Los nombres de variables en Python solo admiten caracteres alfanuméricos y el guión bajo "_", no pueden empezar por un número y se suelen escribir en minúsculas. Si el nombre de una variable se compone de varias palabras es una buena práctica separarlas por un guión bajo:

```python
marca_de_coche = 'Tesla'
```

También se suele utilizar un sistema de escritura denominado *camel case*, en el que las palabras se escriben todas juntas y solo se escribe en mayúscula la primera letra de cada palabra, empezando siempre en minúscula:

```python
cincoNumerosPrimos = [2, 3, 5, 7, 11]
```

En cambio las constantantes se suelen escribir con todas las letras mayúsculas y si se componen de varias palabras, estas separadas por guión bajo:

```python
NUMERO_PI = 3.14159
```

A continuación veremos los diferentes tipos de datos que se le pueden asignar como valor a una variable o constante.

## Números enteros y flotantes (decimales)

Hay un tipo de datos para los números, concretamente para los números enteros y los flotantes o decimales. El intérprete de Python permite realizar con este tipo de datos cálculos simples como sumar, restar, multiplicar, dividir, operaciones módulo o potencias. Algunos ejemplos:

```python
>>> suma = 1+2
>>> suma
3
>>> resta = 7-2
>>> resta
5
>>> resta_negativa = 5-9
>>> resta_negativa
-4
>>> multiplicacion = 3*4
>>> multiplicacion
12
>>> multiplicacion_decimal = 0.3*4
>>> multiplicacion_decimal
1.2
>>> division = 28/7
>>> division
4.0
>>> operacion_modulo = 25%5
>>> operacion_modulo
0
>>> potencia = 3**2
>>> potencia
9
```

Se pueden realizar operaciones concatenadas más complejas. El orden correcto siempre será de izquierda a derecha, primero las multiplicaciones y divisiones, y luego las sumas y restas. Python se encargará de respetar el orden de los operadores automáticamente, por ejemplo:

```python
>>> operaciones_seguidas = 3-2+4*10
>>> operaciones_seguidas
41
```

Como se puede ver, primero ha realizado la operación de multiplicación `4*10`, que da como resultado `40`, luego la operación resta `3-2`, que da como resultado `1`, y finalmente la suma `1+40`, que da como resultado `41`.

Y por supuesto se puede hacer operaciones con tan solo el nombre de las variables, de modo que se utilizará los valores que estas tengan almacendo en memoria.

```python
>>> numero_a = 5
>>> numero_b = 3
>>> numero_a * numero_b
15
```

## Cadenas de carácteres o *string*

Otro tipo de datos son las cadenas de caracteres o *string*. Estas cadenas se pueden escribir dentro de unas comillas dobles (") o simples ('), por ejemplo:

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

Para trabajar más cómodamente y poder estudiar algunas de las opciones que permite realizar Python con las cadenas de texto o *strings* usaremos variables. Por ejemplo, se puede acceder fácilmente a un carácter en concreto de una cadena de carácteres, pues estos están colocados en una posición de la cadena. En este ejemplo la variable `nombre` contiene como valor una cadena de carácteres ordenados mediante el siguiente índice:

```python
>>> nombre = 'Javier'
```

```
 J   a   v   i   e   r
 |   |   |   |   |   |
[0] [1] [2] [3] [4] [5]
```

Accederemos a ellos mediante el uso de índices en el que se indicará la posición del carácter a mostrar, vease el siguiente ejemplo:

```python
>>> nombre[0] # Carácter en la posición 0
'J'
>>> nombre[1] # Carácter en la posición 1
'a'
>>> nombre[3] # Carácter en la posición 3
'i'
>>> nombre[4] # Carácter en la posición 4
'e'
```

También existen los índices negativos, por ejemplo para acceder al último carácter de la cadena sin que sea necesario conocer la posición del mismo:

```python
>>> nombre[-1] # Último caracter de nombre
'r'
>>> nombre[-2] # Penúltimo caracter de nombre
'e'
>>> nombre[-3] # Antepenúltimo caracter de nombre
'i'
```

También existe la posibilidad de extraer porciones de cadenas de texto, se consigue mediante una opción de los índices llamada *slicing*, en la que se ha de indicar dentro de los corchetes una pusición de inicio, seguido del símbolo de dos puntos ":" y una posición de final. Por ejemplo, para extraer solo los tres primeros carácteres de la variable `nombre` de ha inidicar la posición `0`, que es la primera, dos puntos `:` y el carácter en el que queremos que se pare y no muestre, en este caso es el cuarto carácter, es decir la posición `3`:

```python
>>> nombre[0:3]
'Jav'
```

Como se puede ver, el último caracter indicado, en el ejemplo anterior el `3`, nunca se incluye. Pero si queremos incluír el último caracter bastaría con no indicar nada, en este otro ejemplo se puede ver cómo extraer los carácteres desde el tercero hasta el último, incluyéndolo:

```python
>>> nombre[2:]
'vier'
```

Y también se puede no indicar ningún caracter de inicio, por ejemplo, para mostrar desde el inicio de la cadena hasta el tercer carácter:

```python
>>> nombre[:2]
'Ja'
```

O bien todos los elementos de la cadena menos el último o los dos últimos:

```python
>>> nombre[:-1]
'Javie'
>>> nombre[:-2]
'Javi'
```

La variable `nombre` contiene una cadena de 6 carácteres, eso es un índice que va desde el `0` hasta el `5`, pero ¿Qué sucederá si indicamos índices mayores de los disponibles? Por ejemplo, desde el índice `21` hasta el final

```python
>>> nombre[21:]
''
```

En este caso no muestra nada, pues no existe nada desde la posición `21` del índice hasta un final. Pero y ¿si indicamos que nos muestre desde el inicio de la cadena hasta la posición `21`?

```python
>>> nombre[:21]
'Javier'
```

En este otro caso mostrará toda la cadena, pues a pesar de que el índice no tiene `21` posiciones muestra todas las disponibles.

Ahora que ya se conoce el funcionamiento de las cadenas de carácteres y el acceso a cada elemento de la cadena mediante índices, es posible que el alumno s epregunte si es posible modificar el valor de algun elemento de la cadena de carácteres. Para el tipo de dato *string* o cadena de carácteres no es posible hacerlo directamente, véase un ejemplo y el error que devuelve:

```python
>>> nombre[0] = 'X'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Como se puede ver, el error es claro, indica que para el tipo de dato `str` (*string*) no es posible la asignación de valores a un *item* o elemento de la cadena. Pero si queremos modificar solo el primer carácter de la cadena `'J'` por el carácter `'X'` es posible mediante la siguiente operación:

```python
>>> nombre = 'X' + nombre[1:]
>>> nombre
'Xavier'
```

Lo que ha sucedido es que se ha reasignado un valor completo a la variable `nombre`. En este caso hemos indicado que el nuevo valor será el carácter `'X'` seguido de todos los carácteres que tiene la variable `nombre` antes de la reasignación de valor, pero solo desde el segundo carácter hasta el final, es decir el índice con *slice* `[1:]`.

El tipo de datos *string* o cadena de carácteres permite utilizar una función de Python llamada `len()` a la que se le debe indicar entre los paréntesis la cadena de carácteres, de modo que devuelve la longitud en número de carácteres. Vease algunos ejemplos:

```python
>>> nombre = 'Javier'
>>> apellidos = 'Domínguez'
>>> len(nombre)
6
>>> len(apellidos)
9
```

La función `len()` no está disponible para todos los tipos de datos, más adelante veremos en qué otras ocasiones se puede utlizar.

## Listas

Las listas son un tipo de datos en Python que permite agrupar diferentes elementos o *items*, e incluso siendo estos de diferentes tipos de datos, como carácteres, números enteros y flotantes, cadenas de caracteres, e incluso otras listas. Se definen entre corchetes "[ ]" y sus elementos han de ir separados por una coma.

Ejemplo de una lista en la que todos sus elementos son números enteros:

```python
>>> [3, -9, 12, 1, -27]
[3, -9, 12, 1, -27]
```

Ejemplo de lista con todos sus elementos de tipo cadena de carateres o *string*:

```python
>>> ['a', 'b', 'c', 'd', 'Hola']
['a', 'b', 'c', 'd', 'Hola']
```

En este ejemplo se muestra una lista con varios tipos de datos diferentes:

```python
>>> [1, 'Hola', -27, 'b', 3.14]
[1, 'Hola', -27, 'b', 3.14]
```

E incluso se puede hacer una lista en la que sus elementos sean también una lista:

```python
>>> [[3, -9], ['a', 'Hola'], [0.25, 3.14], [3, 'b', 15.9]]
[[3, -9], ['a', 'Hola'], [0.25, 3.14], [3, 'b', 15.9]]
```
