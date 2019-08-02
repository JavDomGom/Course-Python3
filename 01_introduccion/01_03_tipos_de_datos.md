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

Las listas son un tipo de datos en Python que permite agrupar diferentes elementos o *items*, e incluso siendo estos de diferentes tipos de datos, como carácteres, números enteros y flotantes, cadenas de caracteres, e incluso otras listas. Se definen entre corchetes "`[]`" y sus elementos han de ir separados por una coma.

Ejemplo de una lista en la que todos sus elementos son números enteros:

```python
>>> numeros = [3, -9, 12, 1, -27]
>>> numeros
[3, -9, 12, 1, -27]
```

Ejemplo de lista con todos sus elementos de tipo cadena de carateres o *string*:

```python
>>> caracteres = ['a', 'b', 'c', 'd', 'Hola']
>>> caracteres
['a', 'b', 'c', 'd', 'Hola']
```

En este ejemplo se muestra una lista con varios tipos de datos diferentes:

```python
>>> lista_variada = [1, 'Hola', -27, 'b', 3.14]
>>> lista_variada
[1, 'Hola', -27, 'b', 3.14]
```

E incluso se puede hacer una lista en la que sus elementos sean también listas, esto se conoce como listas anidadas:

```python
>>> lista_de_listas = [[3, -9], ['a', 'Hola'], [0.25, 3.14], [3, 'b', 15.9]]
>>> lista_de_listas
[[3, -9], ['a', 'Hola'], [0.25, 3.14], [3, 'b', 15.9]]
```

Al igual que en el tipo de datos *string* o cadenas de carácteres también se puede acceder a cada elemento de una lista indicando la posición del elemento mediante un índice. Por ejemplo, para mostrar el primer elemento de la una lista basta con indicar el índice `[0]`, véase el ejemplo:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e']
>>> letras[0]
'a'
```

Para mostrar toda la lista menos el último elemento:

```python
>>> letras[:-1]
['a', 'b', 'c', 'd']
```

O bien toda la lista menos los dos últimos elementos:

```python
>>> letras[:-2]
['a', 'b', 'c']
```

También los elementos que van desde el tercero hasta el final:

```python
>>> letras[2:]
['c', 'd', 'e']
```

O los elementos que van desde el segundo hasta el cuarto (el elemento indicado en el final del *slice* no se muestra):

```python
>>> letras[1:4]
['b', 'c', 'd']
```

Como se puede ver, el comportamiento del *slicing* es exactamente el mismo que cuando lo usábamos en las cadenas de carácteres. Anteriormente vimos cómo acceder a una posición del índice en una cadena de carácteres, y vimos que no era posible modificar un elemento de la cadena de carácteres mediante la reasignación de valor a su índice. En el caso de las listas si es posible, por ejemplo:

```python
>>> pares = [0, 2, 5, 6, 8]
>>> pares[2] = 4
>>> pares
[0, 2, 4, 6, 8]
```

También se pueden modificar varios elementos de la lista mediante un *slicing*, en este caso queremos cambiar las 3 primeras letras de una lista de letras:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f']
>>> letras[:3]
['a', 'b', 'c']
>>> letras[:3] = ['A', 'B', 'C']
>>> letras
['A', 'B', 'C', 'd', 'e', 'f']
```

Todos los elementos de una lista tienen un orden, al que se puede acceder mediente índices tal y como ya hemos visto. Para añadir nuevos elementos a la lista existe un método `append()` que nos permite incorporar nuevos elementos al final de la lista, por ejempo:

```python
>>> frutas = ['fresa', 'pera', 'uva']
>>> frutas.append('manzana')
>>> frutas
['fresa', 'pera', 'uva', 'manzana']
```

Para eliminar varios elementos de una lista se puede hacer dasignándole un valor de lista vacía "`[]`" a un rango de elementos mediante *slicing*, por ejemplo, si queremos eliminar los pres primeros elementos de la lista:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f']
>>> letras[:3] = []
>>> letras
['d', 'e', 'f']
```

En caso de que queramos borrar todos los elemento de la lista basta con reasignar el valor de la lista con una lista vacía:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f']
>>> letras = []
>>> letras
[]
```

Si lo que se quiere es borrar un elemento concreto se puede hacer utilizando la instrucción `del` (*delete*) de la siguiente manera:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del letras[2]
>>> letras
['a', 'b', 'd', 'e', 'f']
```

En este caso se ha eliminado el tercer elemento de la lista, es decir, el carácter `'c'`. Esta instrucción `del` también permite eliminar varios elementos mediante *slicing*, por ejemplo, para eliminar el tercer y cuarto elemento de la lista:

```python
>>> letras = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del letras[2:4]
>>> letras
['a', 'b', 'e', 'f']
```

Volvamos a las listas anidadas, es decir, aquellas listas que sus elementos son a su vez otras listas. Veamos cómo se pueden construír y cómo se puede acceder a sus datos mediante múltiples índices, por ejemplo:

```python
>>> lista_1 = [0, 1, 2]
>>> lista_2 = [3, 4, 5]
>>> lista_3 = [6, 7, 8]
>>> lista_anidada = [lista_1, lista_2, lista_3]
>>> lista_anidada
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

Para acceder al primer elemento de `lista_anidada` basta con indicar el índice `[0]`.

```python
>>> lista_anidada[0]
[0, 1, 2]
```

Pero para acceder a uno de los elementos de este primer elemento de la lista `lista_anidada` se ha de indicar un segundo índice, donde se indicará la posición del elemento a que se quiere acceder, por ejemplo, para acceder al primer elemento de la primera lista:

```python
>>> lista_anidada[0][0]
0
```

Y para acceder al primer elemento de la segunda lista:

```python
>>> lista_anidada[1][0]
3
```

A continuación veremos algunos de los métodos que se pueden utilizar con las listas. Por ejepmplo, el método `len()` devolverá el tamaño de la lista, es decir, el número de elementos que tiene, véase el ejemplo:

```python
>>> lista = ['Dennis', 'Ken', 'Richard']
>>> len(lista)
3
```

El método `count()` devolverá el número de veces que existe un elemento dentro de una lista, por ejemplo:

```python
>>> mascotas = ['perro', 'gato', 'canario', 'gato', 'hurón']
>>> mascotas.count('gato')
2
```

El método `index()` devuelve el índice menor en el que se encuentra un elemento dentro de una lista, por ejemplo:

```python
>>> mascotas = ['perro', 'gato', 'canario', 'gato', 'hurón']
>>> mascotas.index('gato')
1
>>> mascotas.index('hurón')
4
```

El método `insert()` permite añadir un nuevo elemento a una lista, y además permite hacerlo en la posición del índice que le especifiquemos. Lo que sucederá con el resto de elementos que se encontraban en esa posición del índice en adelante es desplazarlos, véase el ejemplo en el que se añade una nueva mascota en la cuarta posición del índice:

```python
>>> mascotas.insert(3, 'iguana')
>>> mascotas
['perro', 'gato', 'canario', 'iguana', 'gato', 'hurón']
```

El método `pop()` elimina y devuelve un elemento de la lista. Si no se le pasa ningún argumento tendrá en cuenta el último elemento de la lista, y si se indica una posición del índice lo hará con el elemento indicado, véase el ejemplo:

```python
>>> mascotas.pop()
'hurón'
>>> mascotas
['perro', 'gato', 'canario', 'iguana', 'gato']
>>> mascotas.pop(1)
'gato'
>>> mascotas
['perro', 'canario', 'iguana', 'gato']
```

El método `reverse()` invertirá el orden de los elementos de una lista según su índice, por ejemplo:

```python
>>> mascotas
['perro', 'canario', 'iguana', 'gato']
>>> mascotas.reverse()
>>> mascotas
['gato', 'iguana', 'canario', 'perro']
```

El método `sort()` ordenará los elementos de una lista, de mayor a menor o alfabéticamente, por ejemplo:

```python
>>> mascotas.sort()
>>> mascotas
['canario', 'gato', 'iguana', 'perro']
>>> numeros = [23, 48, 5, 19, 71, 9]
>>> numeros.sort()
>>> numeros
[5, 9, 19, 23, 48, 71]
```

A continuación se exlicarán algunas operaciones básicas que se pueden realizar con las listas. Por ejemplo, se pueden sumar varias listas con el operador suma `+`:

```python
>>> lista_1 = ['a', 'b', 'c']
>>> lista_2 = ['d', 'e', 'f']
>>> lista_1 + lista_2
['a', 'b', 'c', 'd', 'e', 'f']
```

También admite el operador multiplicación `*` para multiplicar elementos de una lista:

```python
>>> lista = ['Hola'] * 3
>>> lista
['Hola', 'Hola', 'Hola']
```
```python
>>> lista = ['a', 'b', 'c'] * 4
>>> lista
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
```

También permite averiguar si un elemento existe dentro de una lista mediante el uso de `in`, véase el ejemplo:

```python
>>> lista = ['rojo', 'verde', 'morado']
>>> 'verde' in lista
True
>>> 'azul' in lista
False
```

Y cómo no, podemos realizar iteraciones con los elementos de una lista, por ejemplo:

```python
>>> animales = ['perro', 'gato', 'pez', 'iguana', 'hurón']
>>> for animal in animales: print(animal)
...
perro
gato
pez
iguana
hurón
```

## Operadores y expresiones

### Operadores relacionales
Son aquellos operadores que se utilizan para realizar comparaciones.  Por ejemlo, el operador "igual qué" se escribe con el símbolo igual dos veces seguidas `==`, se utiliza de la siguiente manera:

```python
>>> 'a' == 'a'
True
>>> 7 == 9
False
```

Por lo contrario, el operador "distinto de" se utiliza para comprobar si dos o elementos son diferentes, se escribe con el símbolo de exclamación seguido de un igual `!=`, véase el ejemplo:

```python
>>> 'Hola' != 'hola'
True
>>> 8 != 27
True
>>> 3 != 3
False
```

El operador "mayor qué" se escribe con el símbolo `>` y sirve para comprobar si el primer elemento es mayor que el segundo, por ejemplo:

```python
>>> 3 > 7
False
>>> 9 > 0
True
```

Existe otro operador "mayor o igual qué", se escribe `>=` y sirve para comprobar si el primier elemento es mayor o igual qué el segundo, por ejemplo:

```python
>>> 3 >= 5
False
>>> 3 >= 3
True
>>> 3 >= 2
True
```

El operador "menor qué" se escribe con el símbolo `<` y sirve para comprobar si el primer elemento es menor que el segundo, por ejemplo:

```python
>>> 21 < 15
False
>>> -15 < -7
True
```

Por último hay también un operador "menor o igual qué", se escribe `<=` y sirve para comprobar si el primier elemento es menor o igual qué el segundo, por ejemplo:

```python
>>> -25 <= 128
True
>>> 17 <= 17
True
>>> 17 <= 16
False
```

Una vez explicados los operadores relacionales se pueden utilizar para realizar algunas comprobaciones más complejas, por ejemplo, se puede comparar si el resultado de una operación aritmética es igual a un número concreto:

```python
>>> 2 + 3 == 7
False
>>> 7 - 2 == 5
True
```

O si dos listas son iguales:

```python
>>> lista_1 = [0, 1, 2]
>>> lista_2 = [2, 3, 4]
>>> lista_1 == lista_2
False
```

En este caso devuelve un `False` por que evidentemente no son iguales, tienen elementos diferentes, pero ¿y si comprobamos la igualdad entre el último elemento de la primera lista y el primero de la segunda lista?

```python
>>> lista_1[-1] == lista_2[0]
True
```

También podemos comprobar la igualdad entre la longitud de la primera lista y la longitud de la segunda lista:

```python
>>> len(lista_1) == len(lista_2)
True
```

### Operadores lógicos



