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



```python

```
```bash
python3 
```



```python

```
```bash
python3 
```



```python

```
```bash
python3 
```

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
