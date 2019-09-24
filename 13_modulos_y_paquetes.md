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

Tambiñén podríamos importar solo la clase `Saludo` tal y como hemos visto antes:

```python
from saludos import Saludo

Saludo()
```
```bash
python3 test.py
Hola, te estoy saludando desde el __init__() de la clase Saludo
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
