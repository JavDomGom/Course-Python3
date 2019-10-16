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



```python

```
```bash
python3 test_ficheros.py

```



```python

```
```bash
python3 test_ficheros.py

```
