# Manejo de ficheros

Hasta ahora todo lo que hemos visto son pequeños programas o *scripts* que funcionaban almacenando información como variables, constantes u objetos en tiempo de ejecución, es decir, que solo existen mientras el programa se está ejecutando. Pero hemos llegado a un punto en el que probablemente nos interese almacenar algunos de los datos con los que hemos aprendido a trabajar en algún fichero, de modo que al cerrar o apagar el programa estos queden persistentemente en un archivo que luego podría volver a cargarse al ejecutar el programa de nuevo, de ese modo no se perdería la información.

Python nos permite realizar las siguientes operaciones con ficheros:

* Creación
* Apertura
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

En este ejemplo hemos creaod una variable llamada `texto` con el las líneas de texto que vamos a escribir en el fichero, y otra variablem llamada `fichero` a la que le hemos asignado como valor un objeto de tipo `open()` al que le hemos pasado dos argumentos, el primero es el nombre del fichero con el que vamos a trabajar, y el segundo argumento es la modalidad que vamos a utilizar, que en este caso es `w` de escritura en inglés (*write*).

A continuación se invoca a al método `write()` del objeto `fichero` al que le pasaremos como argumento nuestra variable `texto`, de este modo se escribirá en el archivo que hemos especificado. Finalmente invocamos al método `close()` del objeto `fichero` para cerrar el archivo una vez hemos terminado de escribir en él.

Si ejecutamos el programa veremos que no hay salida por pantalla alguna, pero si listamos los archivos que se encuentran en el directorio actual podremos ver que se ha creado un archivo nuevo llamado `fichero.txt`, el cual podremos abrir para ver que contiene, y podremos comprobar que en su interior aparece nuestras líneas de texto de la variable `texto`.

```bash
python3 test_ficheros.py
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



```python

```
```bash
python3 test_ficheros.py

```
