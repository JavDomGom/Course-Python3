# Manejo de ficheros

Hasta ahora todo lo que hemos visto son pequeños programas o *scripts* que funcionaban almacenando información como variables, constantes u objetos en tiempo de ejecución, es decir, que solo existen mientras el programa se está ejecutando. Pero hemos llegado a un punto en el que probablemente nos interese almacenar algunos de los datos con los que hemos aprendido a trabajar en algún fichero, de modo que al cerrar o apagar el programa estos queden persistentemente en un archivo que luego podría volver a cargarse al ejecutar el programa de nuevo, de ese modo no se perdería la información.

Python nos permite realizar las siguientes operaciones con ficheros:

* Creación
* Apertura o lectura
* Modificación
* Cierre

Para poder trabajar con ficheros debemos importar el paquete `open` de la librería `io` (*input/output*) al inicio de nuestros programas de la siguiente manera:

```python
from io import open
```

## Creación

Una vez importado el paquete `open` de la librería `io` podemos comenzar con la creación de un programa que escriba una línea de texto en un archivo, de modo que si el archivo no existe lo cree. Para ello será necesario crear una nuevo archivo llamado `test_ficheros.py` con el siguiente código:

```python
texto = 'Esta es una línea de texto.\nY esta es otra línea de texto.\n'

fichero = open('fichero.txt', 'w')
fichero.write(texto)
fichero.close()
```

En este ejemplo hemos creado una variable llamada `texto` con el las líneas de texto que vamos a escribir en el fichero, y otra variable llamada `fichero` a la que le hemos asignado como valor un objeto de tipo `open()` al que le hemos pasado dos argumentos, el primero es el nombre del fichero con el que vamos a trabajar, y el segundo argumento es la modalidad que vamos a utilizar, que en este caso es `w` de escritura en inglés (*write*). Esta modalidad creará el archivo si no existe y escribirá el texto dentro. Si el archivo existiera lo sobrescribiría.

A continuación se invoca a al método `write()` del objeto `fichero` al que le pasaremos como argumento nuestra variable `texto`, de este modo se escribirá en el archivo que hemos especificado. Finalmente invocamos al método `close()` del objeto `fichero` para cerrar el archivo una vez hemos terminado de escribir en él.

Si ejecutamos el programa veremos que no hay salida por pantalla alguna, pero si listamos los archivos que se encuentran en el directorio actual podremos ver que se ha creado un archivo nuevo llamado `fichero.txt`, el cual podremos abrir para ver que contiene, y podremos comprobar que en su interior aparece nuestras líneas de texto de la variable `texto`.

## Apertura o lectura

Para abrir un fichero ya existente y leer su contenido se puede hacer de la siguiente manera:

```python
fichero = open('fichero.txt', 'r')
```

Con esta modalidad `'r'` estaríamos abriendo el fichero en modo lectura (*read*). Ahora podríamos almacenar en una variable llamada `texto` el contenido del fichero, cerrar el fichero e imprimir el contenido de la variable `texto` de la siguiente manera:

```python
texto = fichero.read()
fichero.close()

print(texto)
```
```bash
python3 test_ficheros.py
Esta es una línea de texto.
Y esta es otra línea de texto.
```

Como se puede ver, estaríamos almacenando en la variable `texto` el contenido del fichero. Podemos hacer la prueba de editar "a mano" el contenido del fichero y volver a ejecutar el programa, igualmente se leeran todas las lineas del fichero.

Una manera de leer un archivo línea a línea es almacenando cada línea en una lista. Esto se puede hacer con un método llamado `readlines()` que tienen los objetos de tipo archivo, por ejemplo:

```python
fichero = open('fichero.txt', 'r')

lineas = fichero.readlines()

print(lineas)

fichero.close()
```
```bash
python3 test_ficheros.py
['Esta es una línea de texto.\n', 'Y esta es otra línea de texto.\n']
```

## Modificación

Además de abrir un fichero y escribir en él un texto o leero, también podemos abrir un fichero existente y añadir nuevas líneas. Esto se consigue mediante una modalidad `'a'` que añade líneas al final (*append*), por ejemplo:

```python
fichero = open('fichero.txt', 'a')

fichero.write('Esta en una línea nueva.\n')
fichero.close()
```

Esta modalidad no solo sirve para añadir líneas al final del archivo, si no que también lo crea si este no existe. Si abrimos el fichero `fichero.txt` veremos que ha añadido al final de este una nueva línea con un texto.

Existe una manera un poco más óptima de leer el contenido de un fichero, esta es mediante la sentencia `with`, veamos un ejemplo:

```python
with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)
```
```bash
python3 test_ficheros.py
Esta es una línea de texto.

Y esta es otra línea de texto.

Esta en una línea nueva.

```

## Manejo del puntero

Cuando abrimos un fichero, el puntero es la posición en la que estaremos posicionados para comenzar a leer, escribir o modificar. Dependiendo de la modalidad que estemos empleando, el puntero estará por defecto al inicio del fichero (archivo nuevo) o al final (añadir líneas nuevas). Pero existe un método llamado `seek()` que nos permitirá mover el puntero a una posición que nosotros queramos, por ejemplo, al décimo caracter de la primera línea:

```python
fichero = open('fichero.txt', 'r')
fichero.seek(10)

texto = fichero.read()

fichero.close()

print(texto)
```
```bash
python3 test_ficheros.py
a línea de texto.
Y esta es otra línea de texto.
Esta en una línea nueva.
```

El propio método `read()` que usamos para leer el contenido del fichero desde la posición del fichero también tiene la posibilidad de recibir un argumento para indicarle el número de carácteres que queremos leer o desplazar el puntero, por ejemplo:

```python
fichero = open('fichero.txt', 'r')

texto = fichero.read(6)

fichero.close()

print(texto)
```
```bash
python3 test_ficheros.py
Esta e
```

Existe una modalidad que nos permite leer el archivo y además escribir en él, pero ubicando el puntero en la primera posición, esta modalidad se define mediante `'r+'` de la siguiente manera:

```python
fichero = open('fichero.txt', 'r+')
fichero.write('Incluyo esta linea al principio del fichero.\n')

texto = fichero.read()

fichero.close()

print(texto)
```

Esta modalidad lo que hace realmente es sobreescribir los primeros carácteres que se encuentre desde la primera posición del puntero con los carácteres de la nuevalínea de texto que estamos añadiendo. Si abrimos el archivo después de ejecutar nuestro programa Python veremos el cambio.

Si quisiéramos modificar el contenido de una línea en especial, por ejemplo de la tercera línea, podríamos hacerlo de la siguiente manera:

```python
fichero = open('fichero.txt', 'r+')

lineas = fichero.readlines()
lineas[2] = 'Linea modificada.'

fichero.seek(0)
fichero.writelines(lineas)
fichero.seek(0)

texto = fichero.read()

fichero.close()

print(texto)
```

Si abrimos el archivo de texto para ver los cambios veremos que se ha posicionado en la tercera línea y la ha modificado sobreescribiemdo los caracteres existentes por los nuevos.

```bash
Esta es una línea de texto.
Y esta es otra línea de texto.
Linea modificada.a nueva.
```

## Ficheros y objetos con Pickle

Pickle es un módulo de Python que nos permite trabajar con ficheros binarios en los que podremos guardar objetos y estructuras de datos complejas como colecciones, y luego poder recuperarlos para trabajar con ellos. Lo primero que hay que hacer para comenzar a utilizarlo es importar el módulo `pickle` en un nuevo archivo llamado `test_pickle.py`:

```python
import pickle
```

A continuación crearemos una lista con unos números y al igual que antes creamos una variable llamada `fichero` que tendrá por valor el objeto de un fichero abierto al que llamaremos `lista.bin` y lo haremos en modalidad de escritura binaria `'wb'`, por ejemplo:

```python
lista = [1, 2, 3, 4, 5]

fichero = open('lista.bin', 'wb')
```

Ahora hacemos un volcado de la lista al fichero binario mediante una llamada al método `dump()` del módulo `pickle` y finalmente cerramos el archivo de la siguiente manera:

```python
pickle.dump(lista, fichero)

fichero.close()
```

Si ejecutamos el programa veremos que se ha creado un nuevo archivo `lista.bin`. Si tratamos de abrirlo con un editor de texto veremos carácteres extraños. Esto es porque es un archivo binario, no de texto plano, pero el contenido del fichero es correcto, contiene nuestra lista.

Ahora veremos cómo podemos hacer para leer el fichero una vez lo hemos generado y cómo poder recuperar nuestra lista. Primero abrimos el fichero en modo lectura binaria (`'rb'`) y luego creamos una variable llamada `lista` que tenga por valor una llamada al método `load()` del módulo `pickle` al que le pasamos el fichero como argumento. Cerramos el fichero e imprimimos el contenido de lista:

```python
fichero = open('lista.bin', 'rb')

lista = pickle.load(fichero)

fichero.close()

print(lista)
```
```bash
python3 test_ficheros.py
[1, 2, 3, 4, 5]
```

Como se puede comprobar hemos recuperado la lista que teníamos guardada en un archivo binario. De este modo podríamos almacenar cualquier tipo de objeto, sea una lista o un diccionario o un objeto de una clase, y tendríamos persistencia de datos.
