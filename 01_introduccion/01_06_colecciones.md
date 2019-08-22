# Colecciones

En Python, además de las listas también tenemos un tipo especial de dato llamado colecciones, y a que a su vez se divide en varias estructuras de datos que veremos en detalle en esta sección:

- Tuplas
- Conjuntos
- Diccionarios

Además, podemos simular dos colecciones tradicionales de otros lenguajes como las `Pilas` y las `Colas` utilizando datos de tipo `lista` o librerías y módulos de Python.

## Tuplas
Las tuplas son unas colecciones parecidas a las listas, con la diferencia de que las tuplas son inmutables. Se suelen utilizar para asegurarnos de que determinados datos no se puedan modificar. Python utiliza tuplas en alguna de sus funciones para devolver resultados inmutables. La manera de definir un dato de tipo tupla es parecido a las listas, solo que en vez de usar corchetes `[]` se utilizan paréntesis `()`. Dentro de los paréntesis se incluyen los elementos como si fueran una lista. Para poder ver un ejemplo práctico vamos a crear un archivo llamado `tupla.py` y dentro vamos a incluír el siguiente código:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla)
```
Si ejecutamos el programa obtendremos el siguiente resultado:

```bash
python3 tupla.py
(100, 'Hola', [1, 2, 3], 3.14)
```

Las tuplas, al igual que las listas aceptan indexación y **slicing**. Por ejemplo, podremos consultar el primer elemento con el índice `[0]` o el último elemento de la tupla con el índice `[-1]`:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[0])
print(tupla[-1])
```

Al ejecutarlo obtendremos el siguiente resultado:

```bash
python3 tupla.py
100
3.14
```

Y también podremos imprimir todos los elementos desde el tercero hasta el final con el **slicing** `[2:]`:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[2:])
```

```bash
python3 tupla.py
([1, 2, 3], 3.14)
```

En este caso, uno de los elementos de la tupla es una lista, también podremos acceder a uno de los elementos internos de esa lista tal y como lo hacíamos cuando teníamos listas dentro de listas, con dobles índices, por ejemplo:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[2][1])
```

```bash
python3 tupla.py
2
```

Antes se ha mencionado que las tuplas es un tipo de dato parecido a las listas pero que su valor en inmutable. Vamos a modificar el código de nuestro programa para intentar modificar el primer valor de nuestra tupla y ver el error que devuelve:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

tupla[0] = 37

print(tupla)
```

Si ejecutamos el programa veremos que devuelve el siguiente error en el que se indica que las tuplas  son objetos que no soportan la asignación de valores a cualquiera de su elementos:

```bash
python3 tupla.py
Traceback (most recent call last):
  File "tupla.py", line 3, in <module>
    tupla[0] = 37
TypeError: 'tuple' object does not support item assignment
```

Al igual que la listas también tienen una longitud, que representaría el número de elementos que tiene, y para ello se utiliza de nuevo la función `len()`, por ejemplo:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(len(tupla))
```
```bash
python3 tupla.py
4
```

Tanto en las listas como en las tuplas se puede buscar la psoición de un elemento si conocemos el valor de dicho elemento, esto se consigue invocando al método `.index()` de la siguiente manera, por ejemplo, modifiquemos el código de nuestro programa para que nos devuelva la posición del elemento `[1, 2, 3]`:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla.index([1, 2, 3]))
```

El ejecutarlo nos devuelve la posición `2`, e sdecir, el elemento que está en tercer lugar, pues en los índices siempre se empieza a contar desde `0`:

```bash
python3 tupla.py
2
```

Otro método interesante que podemos usar tanto en listas como en tuplas en el método `.count()`, este nos devolverá el número de veces que aparece repetido un elemento conocido en la lista o en la tupla. Editemos el código de nuestro programa para ver unos ejemplos:

```python
tupla = (100, 'Hola', 100, 100, [1, 2, 3], 3.14)

print(tupla.count(100))
```
```bash
python3 tupla.py
3
```

Aunque las tuplas y las listas tienen muchos métodos en común hay algunos métodos que no están disponibles en las tuplas como por ejemplo el pétodo `.append()` para añadir nuevos elementos, puesto que las tuplas son inmutables y no se pueden ni editar, si siquiera añadir o eliminar elementos.

## Conjuntos

Los conjuntos son colecciones desordenadas de elementos únicos. Se suelen utilizar para comprobar pertenecias a grupos y eliminación de elementos duplicados.

Para empezar a trabajar con los conjuntos vamos a crear un archivo nuevo llamado `conjuntos.py` y vamos a ir escribiendo código en él. Para crear un conjunto, si este va a ser un cojnuto vacío se hace de la siguiente manera:

```python
conjunto = set()
```

Pero si queremos un conjunto que contenga elementos solo hay que escribir los elementos que se quieren añadir a dicho conjunto entre llaves `{}` y separados por comas, por ejemplo:

```python
conjunto = {1, 2, 3}

print(conjunto)
```
```bash
python3 conjunto.py
{1, 2, 3}
```

Ahra vamos a utilizar el método `.add()` para añadir un nuevo elemento a este conjunto, por ejemplo el número `4`:

```python
conjunto.add(4)
```
```bash
python3 conjunto.py
{1, 2, 3, 4}
```

Se puede ver cómo se ha añadido el número `4` al conjunto, justo al final. Ahora vamos a añadir otro elemento nuevo, por ejemplo el número `0` y mostremos cómo imprime el valor del conjunto:

```python
conjunto.add(0)
```
```bash
python3 conjunto.py
{0, 1, 2, 3, 4}
```

Se ve cómo lo ha añadido, pero no lo ha incluído al final de los elementos, si no al principio, aparentemente lo está ordenando numéricamente. Probamos ahora a añadir un nuevo elemento de tipo **string**:

```python
conjunto.add('H')
```
```bash
python3 conjunto.py
{0, 1, 2, 3, 4, 'H'}
```

La letra "`H`" la ha añadido al final. Ahora vamos a añadir dos letras más, la letra "`A`" y la letra "`Z`" y veamos qué pasa:

```python
conjunto.add('A')
conjunto.add('Z')
```
```bash
python3 conjunto.py
{0, 1, 2, 3, 4, 'A', 'Z', 'H'}
```

Los números los sigue mostrando en orden numérico de menos a mayor, pero los carácteres los muestra en un orden aleatorio, de hecho, si ejecutamos el programa varias veces seguidas podremos comprobar que el orden de las letras "`A`", "`H`" y "`Z`" va cambiando, por eso decimos que los conjuntos son un tipo de colecciones desordenadas.

Los cojnutos son muy útiles para comprobar la pertenencia a un grupo, por ejemplo, hagamos un grupo de personas llamado `conjuntoA`:

```python
conjuntoA = {'Javier', 'Bob', 'Alice'}
```

Para saber si una persona en concreto pertenece al conjunto `conjuntoA` debemos usar la palabra reservada `in` de la siguiente manera:

```python
'Javier' in conjuntoA
```

Esta comprobación devolverá un valor booleano, es decir `True` o `False`, usemos la función `print()` en nuestro código para poder visualizarlo:

```python
conjuntoA = {'Javier', 'Bob', 'Alice'}

print('Javier' in conjuntoA)
```
```bash
python3 conjunto.py
True
```

Si lo que queremos comprobar es si una persona en concreto no está en el conjunto `conjuntoA` podemos usar la negación `not` de la siguiente manera:

```python
conjuntoA = {'Javier', 'Bob', 'Alice'}

print('Javier' not in conjuntoA)
```
```bash
python3 conjunto.py
False
```

Algo muy interesante de los conjuntos es que no pueden contener elementos repetidos, si se añade varias veces el mismo elemento no dará ningún error, pero solo lo mostrará una vez, hagamos una prueba en nuestro código:

```python
conjuntoA = {'Javier', 'Bob', 'Javier', 'Javier', 'Alice'}

print(conjuntoA)
```
```bash
python3 conjunto.py
{'Alice', 'Javier', 'Bob'}
```

Podemos explotar esta funcionalidad de los conjuntos por ejemplo para eliminar elementos repetidos en una lista, pero para ello hay que emplear una técnica llamada **cast** en la que vamos a cambiar un tipo de dato a otro tipo, en este caso vamos a convertir una variable de tipo lista que contendrá elementos repetidos a una variable de tipo conjunto, por lo que se eliminarán, finalmente volveremos a hacer **cast** para volver a convertir nuestra variable a tipo lista, hagámoslo por pasos, primero creamos la variable `lista` de tipo lista con elementos repetidos:

```python
lista = [1, 2, 3, 3, 2, 1]
```

A continuación creamosuna nueva variable `conjunto` de tipo conjunto a la que le vamos a añadir como valor el contenido de la variable `lista` utilizando el método `set()` de la siguiente manera:

```python
lista = [1, 2, 3, 3, 2, 1]
conjunto = set(lista)

print(conjunto)
```

Si ejecutamos ahora nuestro programa nos devolverá un conjunto con los elementos de `lista` sin repetir:

```bash
python3 conjunto.py
{1, 2, 3}
```

Finalmente vamos a convertir de nuevo la variable `conjunto` sin elementos repetidos a una lista, para ello volvemos a hacer **cast** utilizando en este caos el método `list()` de la siguiente manera:

```python
lista = [1, 2, 3, 3, 2, 1]
conjunto = set(lista)
lista = list(conjunto)

print(lista)
```
```bash
python3 conjunto.py
[1, 2, 3]
```

En vez de hacer este **cast** doble en varias líneas podemos hacerlo más sencillo en una sola línea de la siguiente manera:

```python
lista = [1, 2, 3, 3, 2, 1]
lista = list(set(lista))

print(lista)
```
```bash
python3 conjunto.py
[1, 2, 3]
```

Este concepto también funciona con cadenas de carácteres, por ejemplo:

```python
cadena = "El perro de San Roque no tiene rabo"

print(set(cadena))
```
```bash
python3 conjunto.py
{'S', 'u', 'b', 'E', 'r', 'd', 'n', 'o', 'q', 'i', 'e', ' ', 't', 'a', 'p', 'R', 'l'}
```

Como resultado se crea un conjunto con todas las letras que aparecen en la variable de tipo **string** `cadena`, pero sin repetir y sin guardar un orden específico.

## Diccionarios

El último tipo de colección que vamos a ver son los diccionarios. Junto a las listas son las colecciones más utilizadas en Python. Se basa en una estructura mapeada, del ingñés **mapping** donde cada elemento de la colección se encuentra identificado mediante una clave única, por lo tanto no puede haber dos claves iguales en el mismo diccionario. Así pues, para crear un diccionario deberemos indicar siempre una clave, que generalmente será una cadena de caracteres, y un valor para cada elemento. Crearemos un nuevo archivo llamado `diccionario.py` para ir añadiendo el código de esta sección. Podemos crear un diccionario vacío escribiendo unas simples llaves `{}` sin nada dentro:

```python
diccionario_vacio = {}

print(diccionario_vacio)
```
```bash
python3 diccionario.py
{}
```

Podemos asegurarnos de que es un diccionario utilizando la función `type()`, que nos devolverá el tipo al que pertenece una variable:

```python
diccionario_vacio = {}

print(type(diccionario_vacio))
```
```bash
python3 diccionario.py
<class 'dict'>
```

Veamos un ejemplo en el que crearemos un diccionario de colores y su traducción al inglés:

```python
diccionario = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

print(diccionario)
```
```bash
python3 diccionario.py
{'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
```

Con esto ya tendríamos un diccionario definido con tres elementos con la estructura "`clave:valor`". Si quisiéramos saber el valor que tiene el color `amarillo` en esta estructra de datos tendríamos que hacerlo de la siguiente manera:

```python
diccionario = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

print(diccionario['amarillo'])
```
```bash
python3 diccionario.py
yellow
```

Para mostrar el `valor` de uno de los elementos del diccionario es necesario especificar la `clave`, en este ejemplo la clave es `'amarillo'` y el valor es `'yellow'`.

También podemos utilizar números como claves o índices, por ejemplo, vamos a crear un diccionario nuevo llamado números en el que las claves serán números enteros y los valores un **string** con su nombre:

```python
numeros = {10: 'diez', 23: 'veintitrés', 57: 'cincuenta y siete'}
```

Para acceder al valor de un índice del dicionario bastaría con especificar la clave, por ejemplo:

```python
print(numeros[57])
```
```bash
python3 diccionario.py
cincuenta y siete
```

Los diccionarios también nos permiten crear índices con la clave de tipo **string** y su valor de tipo numérico o entero, por ejemplo, creamos un dicionario que se llama `edades` de la siguiente manera:

```python
edades = {'Javier': 18, 'Alice': 21, 'Bob': 33}

print(edades)
```
```bash
python3 diccionario.py
{'Javier': 18, 'Alice': 21, 'Bob': 33}
```

Del mismo modo que podíamos modificar los registros de una lista también podremos modificar los registros de un diccionario. Volvamos al ejemplo de los colores para ver un ejemplo. Vamos a crear un diccionario llamado `colores`, este va a contener los nombres de algunos colores como clave y su traducción al inglés como valor.

```python
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
```

Ahora vamos a imprimir el diccionario antes de realizar alguna modificación y después cambiamos el índice o clave `azul`, que actualmente tiene como valor `blue`, le vamos a poner como nuevo valor `purple` y finalmente volvemos a imprimir el contenido del diccionario para ver que se ha modificado con éxito:

```python
colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}

print(colores)

colores['azul'] = 'purple'

print(colores)
```
```bash
python3 diccionario.py
{'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
{'amarillo': 'yellow', 'azul': 'purple', 'verde': 'green'}
```

También podemos borrar una entrada del diccionario, es decir suna clave y su valor, para ello es necesario usar el método `.del()` y especificar la clave a borrar, véase el ejemplo:

```python
del(colores['azul'])

print(colores)
```
```bash
python3 diccionario.py
{'amarillo': 'yellow', 'verde': 'green'}
```

Otra cosa bastante útil que podemos hacer con un diccionario es recorrer todos sus items con un bucle `for`, veamos un primer ejemplo:

```python
edades = {'Javier': 18, 'Alice': 21, 'Bob': 33}

for clave in edades:
    print(clave)
```
```bash
python3 diccionario.py
Javier
Alice
Bob
```

De este modo podremos listar la clave de cada uno de los índices del diccionario, pero quizás podría interesarnos acceder a los valores. Esto se puede realizar de la siguiente manera:

```python
for clave in edades:
    print(edades[clave])
```
```bash
python3 diccionario.py
18
21
33
```

Si lo que quiseramos es mostrar tanto la clave como el valor podríamos hacerlo de la siguiente manera:

```python
for clave in edades:
    print(clave, edades[clave])
```
```bash
python3 diccionario.py
Javier 18
Alice 21
Bob 33
```

Sin embargo esta forma es un poco rudimentaria, existen formas más óptimas de acceder a ambos datos, por ejemplo con el método `.items()` y seteando en el bucle las dos variables de la siguiente manera:

```python
for clave, valor in edades.items():
    print(clave, valor)
```
```bash
python3 diccionario.py
Javier 18
Alice 21
Bob 33
```

Para terminar esta sección veremos cómo se puede crear una estructura de datos un poco más avanzada, por ejemplo creando una lista con varios diccionarios como elementos y cómo podemos luego acceder a los datos de cada diccionario con un bucle `for`, bien para mostrarlos o para editarlo, veamos un ejemplo. Primero crearemos una lista vacía llamada `alumnos`:

```python
alumnos = []
```

A continuación crearemos un diccionario llamado `a` y registrará tres datos de una alumno, por ejemplo `'Nombre'`, `'Curso'` y `'Clase'`.

```python
a = {'Nombre': 'Javier', 'Curso': 1, 'Clase': 'A'}
```

Añadimos este primer diccionario como un elemento a la lista `alumnos`.

```python
alumnos.append(a)
```

Repetimos los dos pasos anteriores un par de veces con otros dos alumnos más:

```python
a = {'Nombre': 'Alice', 'Curso': 2, 'Clase': 'C'}
alumnos.append(a)

a = {'Nombre': 'Bob', 'Curso': 3, 'Clase': 'B'}
alumnos.append(a)
```

Y finalmente recorremos la lista `alumnos` con un bucle for, seteando como variable `a` cada elemento, que en este caso es un diccionario. Luego dentro del bucle haremos un `print()` de los tres datos de cada diccionario `a`, es decir `'Nombre'`, `'Curso'` y `'Clase'`.

```python
for a in alumnos:
    print(a['Nombre'], a['Curso'], a['Clase'])
```
```bash
python3 diccionario.py
Javier 1 A
Alice 2 C
Bob 3 B
```

Como se puede ver, es relativamente sencillo crear una lista que haga la función de una simple base de datos de alumnos, y ahora ya sabemos cómo podemos acceder a los datos de cada elemento de la lista, que son los datos de los alumnos.

## Pilas

El lenguaje Python no implementa una colección del tipo `pila` como en otros lenguajes, sin embargo podemos simularlas fácilmente con listas. Una `pila` es una colección de elementos ordenados y únicamente permite dos acciones, añadir elementos a la pila y sacar elementos de la pila. Lo interesante de las pilas es que el último elemento en entrar en la pila es el primero en salir, en inglés se denomina `LIFO` (**Last In, Fist Out**), como si se tratara de una pila de platos sucios que hay que lavar a mano, se van dejando encima de una mesa, y luego se van cogiendo uno a uno para lavarlos, en cuyo caso se coge primero el último plato sucio que se dejó en la pila.

Para simular el comportamiento de una `pila` en Python comenzaremos creando un nuevo fichero llamdo `pila.py` y crearemos una lista llamada `p` con unos cuantos valores:

```python
pila = [0, 1, 2, 3, 4]
```

A continuación añadimos un nuevo elemento a la pila `p` mediante el método `.append()`, que es el que usábamos para añadir elementos a una lista, ya que es exactamente lo que queremos hacer, puesto que estamos usando listas para simular una pila. Añadamos también una línea para imprimir el resultado tras añadir un elemento a la pila.

```python
pila.append(5)

print(pila)
```
```bash
python3 pila.py
[0, 1, 2, 3, 4, 5]
```

Como se puede comprobar, el úlitmo elemento que hemos añadido a la `pila` es el número `5`. Ahora para eliminar el último elemento de la pila usaremos un nuevo método que tienen disponible las listas llamado `.pop()`.

```python
pila.pop()
print(pila)
```
```bash
python3 pila.py
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
```

Ahora al ejecutar el programa, se puede ver que tras ejecutar el método `.pop()` si se imprime el contenido de la pila esta ya no tiene el último elemento. Probemos a añadir después de nuestro código varias llamadas al método `.pop()` seguidas e imprimamos el nuevo estado de la pila.

```python
pila.pop()
pila.pop()
pila.pop()
print(pila)
```
```bash
python3 pila.py
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4]
[0, 1]
```

Cada llamada al método `.pop()` se elimina el último elemento que entró en la `pila`, en este caso se han eliminado 3 elementos más.

## Colas

Una `cola` es una estructura de datos parecida a las `pilas`, a diferencia de que el primer elemento en entrar en la `cola` es el primero en salir, en inglés se denomina `FIFO` (**First In, First Out**). Podríamos compararlo con una cola para entrar en la cita con el médico, el que primero llega es antendido y cuando termina sale.

Para poder ver cómo implementar una `cola` en Python primero vamos a crear un nuevo archivo llamado `cola.py` y tendremos que importar el módulo `deque` de la librería standard de Python `collections` de la siguiente manera:

```python
from collections import deque
```

Más adelante se explicará en detalle la importación de librerías y módulos de librerías en Python.

A continuación crearemos una cola vacía mediante el siguiente código:

```python
cola = deque()
print(cola)
```

Si imprimimos el contenido de la cola veremos que aparece como una lista vacía:

```bash
python3 cola.py
deque([])
```

Ahora vamos a añadir un primer elemento a esta cola que inicialmente esta vacía, como lo que contiene dentro es una `lista` podemos usar el método `.append()` que ya habíamos usado anteriormente para añadir elementos a una lista, por ejemplo una cadena de carácteres, además imprmimos el contenido de la cola de nuevo para comprobar que la cola ya tiene al menos un elemento:

```python
cola.append('Javier')
print(cola)
```
```bash
python3 cola.py
deque([])
deque(['Javier'])
```

Vamos a añadir un par de elementos más a la `cola`:

```python
cola.append('Bob')
cola.append('Alice')
print(cola)
```
```bash
python3 cola.py
deque([])
deque(['Javier'])
deque(['Javier', 'Bob', 'Alice'])
```

Ahora que ya tenemos una `cola` con varios elementos, que han sido introducidos secuencialmente, vamos a usar un método propio del módulo `deque` que hemos importado llamado `.popleft()` para eliminar el elemento de la `cola` que entró primero, en este caso es la cadena `'Javier'`, e imprimamos el nuevo estado de la cola:

```python
cola.popleft()
print(cola)
```
```bash
python3 cola.py
deque([])
deque(['Javier'])
deque(['Javier', 'Bob', 'Alice'])
deque(['Bob', 'Alice'])
```

El método `.popleft()` funciona como el método `.pop()` que hemos usado en las `pilas` solo que elimina los elementos de una lista por la izquierda en vez de por la derecha.