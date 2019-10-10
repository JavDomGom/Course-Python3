# Módulos y paquetes

Los módulos son archivos que contienen definiciones y declaraciones en lenguaje Python. De esta manera es posible importarlos en otros scripts o programas y reutilizar estas funcionalidades y a la vez conseguiremos crear una jerarquía mucho más práctica en nuestros proyectos conteniendo los módulos en paquetes.

En esta unidad vamos a ver cómo podemos crear nuestros propios módulos y paquetes en Python, así como su manejo, y un repaso por algunos de los módulos standard más útiles.

## Módulos

Vamos a crear un módulo que tendrá la única funcionalidad de saludar mediante un mensaje por pantalla. Para ello crearemos un archivo llamado `saludos.py` con la siguiente función:

```python
def saludar():
    print('Hola, te estoy saludando desde la función saludar del módulo saludos')
```

Ahora crearemos en el mismo directorio otro archivo llamado `test.py` donde importaremos el módulo `saludos` de la siguiente manera:

```python
import saludos
```

Una vez que ya tenemos importado el módulo `saludos` ya podemos hacer uso de sus funciones, pero no podemos hacerlo del mismo modo que cuando teníamos funciones definidas en nuestro parchivo principal, en estos casos hay que hacerlo anteponiendo el nombre del módulo y un punto (`.`), por ejemplo:

```python
saludos.saludar()
```

Si ejecutamos nuestros programa `test.py` obtendremos la siguiente salida por pantalla:

```bash
python3 test.py
Hola, te estoy saludando desde la función saludar del módulo saludos
```

Para no tener que anteponer el nombre del módulo cada vez que queramos invocar a una de sus funciones se puede importar la función o funciones concretas de un módulo de la siguiente manera:

```python
from saludos import saludar

saludar()
```
```bash
python3 test.py
Hola, te estoy saludando desde la función saludar del módulo saludos
```

Si tuviéramos muchas funciones en el módulo `saludos` y quisiéramos importarlas todas podríamos cambiar el nombre de la función por un asterísco (`*`):

```python
from saludos import *
```

Pero esto podría no interesarnos cuando hay muchas funciones y solo queremos usar unas pocas.

También podemos reutilizar clases definidas en el módulo `saludos`, por ejemplo:

```python
class Saludo():

    def __init__(self):
        print('Hola, te estoy saludando desde el __init__() de la clase Saludo')
```

Ahora en el archivo `test.py` podríamos importar el módulo entero y hacer uso de la clase `Saludo` de la siguiente manera:

```python
import saludos

saludos.Saludo()
```
```bash
python3 test.py
Hola, te estoy saludando desde el __init__() de la clase Saludo
```

También podríamos importar solo la clase `Saludo` tal y como hemos visto antes:

```python
from saludos import Saludo

Saludo()
```
```bash
python3 test.py
Hola, te estoy saludando desde el __init__() de la clase Saludo
```

A continuación veremos algunos de los módulos integrados en Python más utilizados.

### Collections

El módulo integrado `collections` de una serie de colecciones muy interesantes que podremos utilzar para multitud de acciones bastante recurrentes. Para poder hacer uso de sus colecciones podemos importar la colección en cuestión de la siguiente manera:

```python
from collections import Counter
```

Por ejemplo, la colección `Counter` nos devolverá un diccionario con el número de veces que se repite cada uno de los elementos de una lista. Vamos a crear un archivo llamado `test_collections.py` para ver algunos ejemplos:

```python
l = [1, 2, 4, 3, 3, 5, 1, 3, 1, 1, 6]

print(Counter(l))
```
```bash
python3 test_collections.py
Counter({1: 4, 3: 3, 2: 1, 4: 1, 5: 1, 6: 1})
```

En este resultado se puede observar que el número `1` aparece cuatro veces, el número `3` tres veces, el número `2` una vez, etc.

Otro ejemplo en el uso de la colección `Counter` es contar las veces que aparece un carácter en una cadena de caracteres o *string*:

```python
p = 'Hola mundo!'

print(Counter(p))
```
```bash
python3 test_collections.py
Counter({'o': 2, 'H': 1, 'l': 1, 'a': 1, ' ': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1, '!': 1})
```

En este caso el programa nos dice que el carácter `'o'` aparece dos veces, el carácter `'H'` una vez, el caracter `'l'` una vez, etc.

Podría darse el caso en el que tenemos una cadena de caracteres con una varias palabras sepradas por un espacio, por ejemplo:

```python
s = 'rojo verde azul rojo morado rojo blanco blanco'
```

En este caso queremos saber cuántas veces aparece cada palabra, pero hay que precisar que esto no es una lista de palabras, sino una cadena de carácteres. Para resolverlo primero podemos pasar esta cadena de caracteres compuesta de palabras separadas por espacio a una lista, y para ello podemos usar la función integrada `split()`, al que si no le pasamos ningún argumento tomará el carácter espacio por defecto:

```python
print(s.split())
```
```bash
python3 test_collections.py
['rojo', 'verde', 'azul', 'rojo', 'morado', 'rojo', 'blanco', 'blanco']
```

Ahora que ya tenemos cada palabra como un elemento de una lista ya podemos utilizar la colección `Counter` del mismo modo que antes:

```python
print(Counter(s.split()))
```
```bash
python3 test_collections.py
Counter({'rojo': 3, 'blanco': 2, 'verde': 1, 'azul': 1, 'morado': 1})
```

De este modo obtendremos cuántas veces aparece cada palabra. Podríamos aprovechar este contador de elementos para utilizar otra función integrada llamada `most_common()`, a la que le hemos de pasar como argumento el número de elementos que queremos que nos diga que són los más comunes, por ejemplo `1`:

```python
n = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]

c = Counter(n)

print(c.most_common(1))
```
```bash
python3 test_collections.py
[(10, 4)]
```

Nos dice que el elemento más común es el número `10`, que aparece cuatro veces. Si a la función integrada `most_common()` le pasamos como argumento el númeor `2` nos devolverá los dos elementos más comunes:

```python
print(c.most_common(2))
```
```bash
python3 test_collections.py
[(10, 4), (20, 3)]
```

Otra colección del módulo `collections`muy interesante es `OrderedDict`. Los diccionarios son colecciones de datos que muestran sus elementos o indices desordenados. Con esta colección podremos mostrar los indices ordenados por la posición en la que se van añadiendo. Por ejemplo:

```python
from collections import OrderedDict

d = {'perro': 'dog', 'gato': 'cat', 'loro': 'parrot'}

print(OrderedDict(d))
```
```bash
python3 test_collections.py
OrderedDict([('perro', 'dog'), ('gato', 'cat'), ('loro', 'parrot')])
```

De este modo no se alterará el orden de los indices, siempre será el que se definió en su creación y los que se vayan añadiendo si la ocasión lo requiera. Una manera de comprobar esta ordenación es la siguiente:

```python
d1 = {'perro': 'dog', 'gato': 'cat'}
d2 = {'gato': 'cat', 'perro': 'dog'}

print(d1 == d2)
print(OrderedDict(d1) == OrderedDict(d2))
```

### Datetime

Uno de los módulos más interesantes sin duda es `datetime`, que nos servirá para manejar y trabajar con información relacionada con las fechas. Para trabajar sobre este punto vamos a crear un nuevo archivo llamado `test_datetime.py` y vamos a comenzar importando este módulo de la siguiente manera:

```python
import datetime
```

Ahora vamos a crear un objeto de tipo `datetime` en el que haremos uso del subpaquete `datetime` y su método `now()`.

```python
dt = datetime.datetime.now()

print(dt)
```
```bash
python3 test_datetime.py
2019-10-04 14:10:50.879112
```

De esta manera la variable `dt` nos devuelve la fecha y hora actual. También podemos acceder a cada uno de los atributos del objeto `dt`, como solo el año, el mes, día, hora, minuto, segundo o microsegundos, de la siguiente manera:

```python
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
```
```bash
python3  test_datetime.py
2019
10
4
14
25
45
315492
```

Ahora que ya sabemos cómo podemos acceder a cada uno de los elementos de los que se comone una fecha y hora podremos darle el formato que se prefiera, por ejemplo:

```python
print('{}/{}/{}'.format(dt.year, dt.month, dt.day))
print('{}:{}:{} {}'.format(dt.hour, dt.minute, dt.second, dt.microsecond))
```
```bash
python3 test_datetime.py
2019/10/5
8:14:11 307892
```

También podemos crear una fecha manualmente tal y como se muestra en el siguiente ejemplo:

```python
dt = datetime.datetime(2000, 1, 1, 0, 0)

print(dt)
```
```bash
python3 test_datetime.py
2000-01-01 00:00:00
```

En este tipo de dato `datetime` no se pueden sobreescribir los datos mediante la asignación de un nuevo valor de forma standard, ya que los datos se almacenan en una tupla, y las tuplas son inmutables. Por ejmplo, si queremos cambiar el año asignando un nuevo valor al atributo `year` de la siguiente forma nos daría el siguiente error:

```python
dt.year = 3000
```
```bash
python3 test_datetime.py
Traceback (most recent call last):
  File "test_datetime.py", line 5, in <module>
    dt.year = 3000
AttributeError: attribute 'year' of 'datetime.date' objects is not writable
```

Pero el módulo `datetime` dispone de un método propio llamado `replace()` para realizar este cambio, se haría de la siguiente manera:

```python
dt = dt.replace(year=3000)

print(dt)
```
```bash
python3 test_datetime.py
3000-01-01 00:00:00
```

En el módulo `datetime` existe un método llamado `isoformat()` que convierte el dato de tipo fecha a un *standard* ISO, por ejemplo:

```python
dt = datetime.datetime.now()

print(dt.isoformat())
```
```bash
python3 test_datetime.py
2019-10-07T19:46:08.409881
```

Otro método para darle formato personalizado a la fecha y hora es el método `strftime()`, por ejemplo:

```python
print(dt.strftime('%A %d %B %Y %I:%M'))
```
```bash
python3 test_datetime.py
Monday 07 October 2019 07:52
```

`%A` es el día de la semana escrito en inglés, `%d` es el número de día del mes, `%B` es el nombre del mes en inglés, `%Y` es el año con 4 cifras, `%I` es la hora (en formato 12h, para formato 24h es `%H`) y `%M` son los minutos.

Si queremos que las fechas se muestren en español primero habría que importar al inicio del código una librería llamada `locale` y configurar el lenguaje en el que trabajará Python de la siguiente manera:

```python
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')
```

Si ahora volvemos a ejectar el mismo programa aparecerá con el idioma cambiado:

```bash
python3 test_datetime.py
lunes 07 octubre 2019 19:58
```
Se pueden usar diferentes códigos de idioma, por ejemplo en Chino:

```python
locale.setlocale(locale.LC_ALL, 'zh_CN')
```
```bash
python3 test_datetime.py
星期一 07 十月 2019 20:01
```

### Math

El módulo `math` integra una serie de funciones y métodos que nos servirán para realizar algunas operaciones matemáticas de forma más sencilla. Al igual que otros modulos será necesario importarlo al inicio de nuestro código, así que vamos a hacerlo en un nuevo archivo llamado `test_math.py`:

```python
import math
```

Una vez importado el módulo `math` ya tendremos disponibles todos sus métodos. Veamos un ejemplo en el que trataremos de redondear un número decimal. Si utilizamos el método `round()` que viene integrado en Python se redondearán a la baja todos aquellos números decimales que sus decimales sean menores de `5`, por ejemplo:

```python
print(round(1.4))
```
```bash
python3 test_math.py
1
```

Pero se redondearán todos aquellos números decimales que sus decimales sean igual o mayor que 5, véase el ejemplo:

```python
print(round(1.5))
```
```bash
python3 test_math.py
2
```

Gracias al método `floor()` del módulo `math` podremos forzar que el redondeo sea siemrpe a la baja, por ejemplo:

```python
print(math.floor(1.3))
print(math.floor(1.5))
print(math.floor(1.9))
```
```bash
python3 test_math.py
1
1
1
```

Sin embargo, si lo que se quiere es forzar un redondeo al alza debemos utilizar el método `ceil()` del módulo `math`, por ejemplo:

```python
print(math.ceil(1.00001))
print(math.ceil(1.3))
print(math.ceil(1.8))
```
```bash
python3 test_math.py
2
2
2
```

Otra funcionalidad interesante del módulo `math` es el método `fsum()`, que es un sumatorio de una lista de números y que devuelve el resultado en formato *float*, por ejemplo:

```python
numeros = [1, 2, 3, 4, 5]

print(math.fsum(numeros))
```
```bash
python3 test_math.py
15.0
```

Si bien es cierto que existe un método integrado de Python llamado `sum()` que ya hace un sumatorio de una lista de números, esta no es igual de eficaz, ya que si se suman números enteros y flotantes tiene un comportamiento extraño, por ejemplo:

```python
numeros = [0.9999999, 1, 2, 3]

print(sum(numeros))
print(math.fsum(numeros))
```
```bash
python3 test_math.py
6.999999900000001
6.9999999
```

Como se puede ver el comportamiento en el caso de usar el método `sum()` no siempre es estable, en cambio el método `fsum()` que integra el módulo `math`lo resuelve correctamente.

También es interesante es el método `trunc()`, que trunca un número decimal y devuelve la parte entera, por ejemplo:

```python
print(math.trunc(3.14159265359))
```
```bash
python3 test_math.py
3
```

Ya sabíamos hacer potencias en Python con el doble asterisco (**) como operador, pero el módulo `math` integra un método llamado `pow()` al que se le han de pasar dos argumentos, el primero es la base y el segundo el expoenente, por ejemplo:

```python
print(math.pow(2, 3))
print(math.pow(5, 4))
```
```bash
python3 test_math.py
8.0
625.0
```

También tenemos el método `sqrt()` que nos permitirá realizar raíces cuadradas, por ejemplo:

```python
print(math.sqrt(9))
```
```bash
python3 test_math.py
3.0
```

Además de métodos también tiene algunos atributos como las constantes del múnero `pi` o el número `e`:

```python
print(math.pi)
print(math.e)
```
```bash
python3 test_math.py
3.141592653589793
2.718281828459045
```

En realidad el módulo `math`tiene una gran cantidad de funcionalidades y atributos, pero en este documento solo se explican las más utilizadas.

### Random

El módulo `random` es un módulo que contiene varias herramientas o funcionalidades para trabajar y generar números aleatorios. Se utiliza mucho en el desarrollo de videoujuegos o en desarrollos en los que se necesita cierto grado de seguridad. Veamos algunos ejemplos en un nuevo archivo llamado `test_random.py`. Lo primero que hay que hacer es importar el módulo `random` de la siguiente manera:

```python
import random
```

Ahora que ya tenemos el módulo importado podremos empezar a generar un número aleatorio de forma sencilla con el siguiente ejemplo:

```python
print(random.random())
print(random.random())
print(random.random())
```
```bash
python3 test_random.py
0.06823749155608883
0.9070119606268106
0.4445508707984924
```

De esta forma podremos generar números flotantes aleatorios menores o iguales que uno y mayores de cero. Si quisieramos números random entre un rango de dos números podríamos usar el método `uniform()` y solo tendríamos que pasar estos dos números como argumentos, por ejemplo números random entre uno y diez:

```python
print(random.uniform(1, 10))
print(random.uniform(1, 10))
print(random.uniform(1, 10))
```
```bash
python3 test_random.py
2.382198826548743
4.8697236381240865
3.8781201434396864
```

Otra manera de generar números enteros random entre cero y un número es utilizando el método `randrange()`, por ejemplo, entre cero y diez:

```python
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
```
```bash
python3 test_random.py
8
1
4
```

También podemos pasarle dos números como argumentos para que devuelva un número aleatorio entre esos números, por ejemplo:

```python
print(random.randrange(0, 100))
print(random.randrange(0, 100))
print(random.randrange(0, 100))
```
```bash
python3 test_random.py
95
52
91
```

Y si añadimos un número `2` como tercer argumento solo nos sacará números random pares entre cero y diez:

```python
print(random.randrange(0, 100, 2))
print(random.randrange(0, 100, 2))
print(random.randrange(0, 100, 2))
```
```bash
python3 test_random.py
94
46
32
```

Además de poder usar el módulo `random` con números también podremos usarlo con algunas colecciones como las cadenas de texto, en la que podremos escoger una letra de forma aleatoria. Esto se consigue con el método `choice()`, por ejemplo:

```python
cadena = 'Hola mundo!'

print(random.choice(cadena))
print(random.choice(cadena))
print(random.choice(cadena))
```
```bash
python3 test_random.py
n
u
o
```

El método `choice()` también nos vale para listas, en este caso se obtendría de forma aleatoria cualquiera de los elementos de la lista, por ejemplo:

```python
lista = [1, 2, 3, 4, 5]

print(random.choice(lista))
print(random.choice(lista))
print(random.choice(lista))
```
```bash
python3 test_random.py
4
5
3
```

Además del método `choice()` también podremos usar un método llamado `shuffle()` para desordenar los elementos de una lista y que permanezcan guardados de ese modo en la lista de origen, mezcla los elementros de forma aleatoria, por ejemplo:

```python
lista = [1, 2, 3, 4, 5]

print(lista)

random.shuffle(lista)

print(lista)
```
```bash
python3 test_random.py
[1, 2, 3, 4, 5]
[3, 4, 1, 2, 5]
```

Por último también podremos usar un método llamado `sample()` al que le podremos pasar una lista como argumento, y también un número de elementos que queremos que nos devuelva de forma aleatoria, por ejemplo, si quisieramos que nos devolviese tres elementos de la lista de forma aleatoria podríamos hacerlo de la siguiente manera:

```python
lista = [1, 2, 3, 4, 5]

print(random.sample(lista, 3))
print(random.sample(lista, 3))
print(random.sample(lista, 3))
```
```bash
python3 test_random.py
[4, 5, 1]
[4, 2, 5]
[3, 4, 2]
```

Existen infinidad de ejemplos y un montón de métodos disponibles más en el módulo `random`, estos solo son los más utilizados o los más conocidos.

## Paquetes

Utilizar paquetes nos ofrece varias ventajas. En primer lugar nos permite unificar  distintos módulos bajo un mismo número de paquetes. Así podemos utilzar   jerarquías de módulos o submódulos y también subpaquetes. Por otra parte nos permiten distribuir y manejar fácilmente nuestro código como si fueran librerías instalables de Python. De este modo se pueden utilizar como módulos standard desde el inérprete sin cargarlos previamente.

Para crear un paquete primero vamos a crear un nuevo directorio que tendrá por nombre el nombre del paquete, en este ejemplo lo llamaremos simplemente `paquete`. Dentro de este nuevo directorio vamos a crear un nuevo archivo llamado `__init__.py` sin ningún contenido, el archivo vacío. Por último vamos a copiar dentro del directorio `paquete` el archivo `saludos.py` que hicimos anteriormente.

Ahora fuera de la carpeta `paquete` trabajremos sobre el archivo `test.py` que tenemos del punto anterior. En este archivo `test.py` vamos a importar el paquete y sus módulos y clases de la siguiente manera:

```python
from paquete.saludos import *
```

Si queremos utilizar la función `saludar()` de nuestro módulo `slaudos` podemos hacerlo del siguiente modo:

```python
saludar()
```

Al ejecutar el programa obtendremos la siguiente salida por pantalla:

```bash
python3 test.py
Hola, te estoy saludando desde la función saludar del módulo saludos
```

Y si queremos acceder a la clase `Saludo` debemos hacerlo de la siguiente forma:

```python
Saludo()
```
```bash
python3 test.py
Hola, te estoy saludando desde el __init__() de la clase Saludo
```
