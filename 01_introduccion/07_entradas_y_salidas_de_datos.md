# Entradas y salidas de datos

En esta sección vamos a aprender acerca de la entrada y salida de datos en un programa Python, entendiendo por entrada la forma de capturar información desde fuera del programa y por salida la forma de exponer los datos o la información.

La primera forma de capturar información en nuestro programa Python ya la conocemos, es mediante la función `input()`, que toma los datos que el usuario introduce a través del teclado y lo hace como cadenas de texto o **strings**, pero tambien podemos transformar los datos introducidos para poder trabajar con ellos o manipularlos.

## Entrada de datos por teclado

Para trabajar la entrada de datos por teclado vamos a crear un nuevo archivo llamado `entrada_por_teclado.py` y vamos a ir añadiendo código para su estudio. Por ejemplo, vamos a hacer un pequeño programa que pida al usuario introducir un número decimal (`float`), y para ello vamos a usar en primera instancia la función `input()`. Una vez que el usuario introduzca un número decimal este se imprimirá por pantalla:

```python
decimal = input('Introduce un número decimal: ')
print(decimal)
```
```bash
python3 entrada_por_teclado.py
Introduce un número decimal: 3.14
3.14
```

Aparentemente lo ha hecho todo correctamente, y así es, ha impreso por pantalla el valor que hemos introducido. Pero es posible que no sea el tipo de dato que queremos para luego trabajar con él, en este caso el tipo de dato que se muestra es de tipo cadena de carácteres o **string**. Podemos ver el tipo de dato que tenemos almacenado en la variable `decimal` de la siguiente manera:

```python
print(type(decimal))
```
```bash
python3 entrada_por_teclado.py
Introduce un número decimal: 3.14
3.14
<class 'str'>
```

Quizás nos interese que cuando el usuario introduzca el número decimal este se convierta en un tipo **float**, para ello tendremos que indicarlo usando la función `float()` y englobando el `input()` dentro:

```python
decimal = float(input('Introduce un número decimal: '))
print(decimal)
print(type(decimal))
```
```bash
python3 entrada_por_teclado.py
Introduce un número decimal: 3.14
3.14
<class 'float'>
```

Otra manera de pedir datos por teclado varias veces seguidas puede ser usando un bucle for que realice 3 iteraciones. Por ejemplo, creamos una variable `valores` de tipo lista vacía:

```python
valores = []
```

A continuación creamos un bucle `for` que itere 3 veces y en el cuerpo del bucle invocaremos al método `.append()` sobre la lista `valores` y le añadiremos lo que el usuario introduzca por teclado. Al finalizar el bucle de 3 iteraciones se imprimirá el valor de la lista `valores`:

```python
for x in range(3):
    valores.append(input('Introduce un valor cualquiera: '))

print(valores)
```
```bash
python3 entrada_por_teclado.py
Introduce un valor cualquiera: abcd
Introduce un valor cualquiera: Hola
Introduce un valor cualquiera: 1234
['abcd', 'Hola', '1234']
```

Como se puede ver, hemos introducido varios valores dentro de una lista, hemos completado una colección introduciendo datos por teclado varias veces.

Esta manera de introducir datos no es la más común, solo cuando se estan ejecutando programas o scripts Python en una terminal, normalmente los datos se suelen obtener mediante la lectura de datos en ficheros o bases de datos o mediante interfactes gráficas en los que los usuarios completan formularios de datos.

## Entrada de datos por argumentos

Otra posibilidad de pasar datos externos a un programa en Python es a través de argumentos. Se trata de una serie de datos que se han de escribir a la hora de ejecutar el programa, separados por espacios y siempre a continuación del nombre del archivo que contiene el código Python, y que podremos utilizar dentro del programa:

```bash
python3 nombre_del_programa.py argumento1 argumento2 argumentoN
```

Es importante aclarar que si se quiere pasar como argumento una cadena de carácteres que contiene espacio, por ejemplo una frase corriente, esta debe ir siempre englobada entre comillas simples o dobles, de lo contrario entenderá cada palabra de la frase como un argumento diferente. Para poder ver un ejemplo crearemos el archivo `entrada_por_argumentos.py` y añadiremos el siguiente código de ejemplo:

```python
import sys

print(sys.argv)
```

Para poder pasarle al programa argumentos será necesario importar al inicio del código la librería interna de python llamada `sys`. A continuación imprimiremos todos los argumentos que se le pasan al programa Python mediante la instrucción `sys.argv`, que imprmirá todos los argumentos como elementos de una lista:

```bash
python3 entrada_por_argumentos.py 'Todo esto es un argumento' 3.14 -27
['entrada_por_argumentos.py', 'Todo esto es un argumento', '3.14', '-27']
```

Nótese que el propio nombre del programa es en sí un argumento, el primer argumento de la lista, el que está en la posición `0`. Todos los demás argumentos se han convertido a formato **string** automáticamente y cada uno está en una posición del índice de la lista, respetando el mismo orden que se empleó a la hora de escribirlos al ejecutar el programa.

Ahora vamos a cambiar el código de nuestro programa para que imprima una frase un número de veces. Haremos que la frase a imprimir sea el primer argumento (entre comillas simples o dobles) y el número de veces que se imprimirá será el segundo argumento:

```python
import sys

texto = sys.argv[1]
repeticiones = int(sys.argv[2])

for r in range(repeticiones):
    print(texto)
```
```bash
python3 entrada_por_argumentos.py 'Hola mundo!' 3
Hola mundo!
Hola mundo!
Hola mundo!
```

Como se puede ver, el programa ha impreso el primer argumento `'Hola mundo!'` tantas veces como indica el número del segundo argumento.

Ta y como está hecho este simple programa podría fallas si no se le pasan los argumentos esperados. Para ello es recomendable añadir un pequeño control sobre los argumentos al inicio, por ejemplo:

```python
import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(texto)
else:
    print('Error, introduce los argumentos correctamente.')
    print('Ejemplo: ' + sys.argv[0] + ' \'Texto cualquiera\' 3')
```
```bash
python3 entrada_por_argumentos.py 'Hola mundo!'
Error, introduce los argumentos correctamente.
Ejemplo: entrada_por_argumentos.py 'Texto cualquiera' 3
```

En esta ocasión el programa devuelve un error por que no se cumple la condición que hemps establecido, es decir, que el programa tenga 3 argumentos, contando como el nombre del archivo del propio programa como primer argumento.

## Salida de datos

Para manejarse ágilmente en Python es necesario conocer bien cómo manejar las salidas de datos. Hasta ahora hemos visto cómo mostrar por pantalla cadenas de texto o variables de diferentes tipos. Veamos un ejemplo creando un nuevo archivo `salida_por_pantalla.py`:

```python
a = 'me llamo Javier'
b = 3

print('Hola', a, ', mi número favorito es el', b)
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier, mi número favorito es el 3
```

Esta es una manera muy simple de imprmimir cadenas de texto mezcladas con variables de diferentes tipos, pero si queremos tener un mayor control sobre las variables que queremos imprimir debemos comenzar a usar un formato de escritura de las cadenas de carácteres, en Python se hace con el método `.format()`, por ejemplo:

```python
a = 'me llamo Javier'
b = 3

print('Hola {}, mi número favorito es {}'.format(a, b))
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier, mi número favorito es 3
```

Como se puede ver, hemos creado todo el contenido a imprimir dentro de la función `print()` y hemos añadido unas referencias mediante llaves `{}` donde irá el valor de las variables que se declaran dentro del método `.format()`, respetando el mismo orden y separadas por coma. Al ejecutar el programa el resultado es el mismo.

Existe una manera más precisa de indicar que qué referencia va qué variable, y esto se consigue mediante el número del índice en el que aparece una variable ubicada dentro del método `.format()`, solo habría que poner ese índice dentro de l referencia, por ejemplo:

```python
a = 'me llamo Javier'
b = 3

print('Hola {0}, mi número favorito es {1}'.format(a, b))
print('Hola {1}, mi número favorito es {0}'.format(a, b))
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier, mi número favorito es 3
Hola 3, mi número favorito es me llamo Javier
```

En este último ejemplo se ha ejecutado el mismo `print()` con las mismas variables dos veces, en el primero se ha indicado primero el valor la variable `texto` mediante la referencia `'{0}'`, y a continuación la variable `numero` mediante la referencia `'{1}'`. Pero en la segunda ejecución del `print()` hemos especificado primero la referencia `'{1}'`, que imprimirá el valor de la segunda variable (`b`) y a continuación la referencia `'{0}'`, que imprimirá el valor de la primera variable (`a`). E incluso se puede usar varias veces una variable indicando tantas veces como se desee la referencia a la misma, por ejemplo:

```python
a = 'me llamo Javier'
b = 3

print('Hola {0}, mi número favorito es {1} y tengo {1} mascotas.'.format(a, b))
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier, mi número favorito es 3 y tengo 3 mascotas.
```

De esta forma ya no tenemos que preocuparnos del orden de las referencias, solo importa el índice que tengan dentro, y además se pueden usar repetidas veces. Pero todavía dependeríamos del orden en el que están declaradas las variables dentro del método `.format()`. Existe una manera para poder asociar las variables a una clave, por ejemplo asocial la variable `a` con la clave `texto` y la variable `b` con la clave `numero`, de modo que se pueda hacer referencia a la clave en vez de al índice o posición de las varaibles, por ejemplo:

```python
a = 'me llamo Javier'
b = 3

print('Hola {texto}, mi número favorito es {numero}.'.format(numero=b, texto=a))
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier, mi número favorito es 3.
```

El método `.format()` permite también alinear a la izquierda, derecha o centrar un texto, pero lo hará dentro de un espacio con un tamaño definido por el usuario. Por ejemplo, vamos a mostrar una palabra en un espacio con un tamaño de 20 carácteres, y además queremos alinearla a la derecha:

```python
palabra = 'Hola'
print('{0:>20}'.format(palabra))
```
```bash
python3 salida_por_pantalla.py
                Hola
```

Analicemos la referencia `{0:>20}`. El `0` hace referencia a la posición del índice de la variable que queremos usar, como en este caso solo tenemos una variable dentro del método `.format()` pondremos el `0`. También se puede dejar vacío o usar claves, tal y como hemos visto antes. Los dos puntos es solo un separador. Para alinear el valor de la variable `palabra` a la derecha se ha utilizado el símbolo `>` y finalmente se indica el tamaño que tendrá el espacio de carácteres, en este caso 20 carácteres.

Si se quiere alinear a la izquierda bastaría con eliminar el símbolo `>` de la referencia:

```python
palabra = 'Hola'
print('{0:20}'.format(palabra))
```
```bash
python3 salida_por_pantalla.py
Hola                
```

En este caso no se aprecia directamente los 16 espacios que hay a la derecha de la palabra `Hola`, pero están ahí. Veamos de qué manera se puede centrar un texto.

```python
palabra = 'Hola'
print('{0:^20}'.format(palabra))
```
```bash
python3 salida_por_pantalla.py
        Hola        
```

Aquí se pueden apreciar los 8 espacios que hay por la izquerda, luego los 4 carácteres que tiene la palabra `Hola` y después los otros 8 espacios restantes, en total suman 20 carácteres.

Otra posibilidad que nos ofrece el método `.format()` es la de truncar una cadena de caracteres, por ejemplo, vamos a truncar la palabra `Hola` mostrando solo los tres primeros carácteres:

```python
palabra = 'Hola'
print('{0:.3}'.format(palabra))
```
```bash
python3 salida_por_pantalla.py
Hol
```

También se puede combinar un truncamiento con una alineación, por ejemplo:

```python
palabra = 'Hola'
print('{0:>10.3}'.format(palabra))
```
```bash
python3 salida_por_pantalla.py
       Hol
```

El método `.format()` no solo da formato a cadenas de texto, también e números, y esto puede resultar muy útil, ya que podríamos necesitar alinear números de diferentes longitudes en columnas, redondear números decimales o rellenarlos con ceros o espacios por la izquierda o derecha. Por ejemplo, vamos a formatear los números enteros `1000`, `100` y `10` para que queden alineados a la derecha rellenándolos con espacios:

```python
print('{:4d}'.format(10))
print('{:4d}'.format(100))
print('{:4d}'.format(1000))
```
```bash
python3 salida_por_pantalla.py
  10
 100
1000
```

En la referencia `{:4d}` el `4` es el espacio de caracteres que vamos a usar para completar la cadena de carácteres que se quiere imprimir, y la letra `d` es para indicar que es un número (*digit*), por defecto se añadirán tantos espacios por la izquierda como sean necesarios para que el total de caracteres sea `4`.

Si en lugar de rellenar con espacios por la izquierda queremos que se rellenen con ceros solo tendremos que añadir un `0` por delante de `4d`, quedando de la siguiente manera:

```python
print('{:04d}'.format(10))
print('{:04d}'.format(100))
print('{:04d}'.format(1000))
```
```bash
python3 salida_por_pantalla.py
0010
0100
1000
```

Veamos un ejemplo con números decimales o de coma flotante. Por ejemplo, si tenemos el número *pi* con nueve decimales, es decir `3.141592653`, y queremos mostrar solo los dos primeros decimales:

```python
print('{:.2f}'.format(3.141592653))
```
```bash
python3 salida_por_pantalla.py
3.14
```
En este caso en la referencia `{:.2f}` el `.2` indica el número de decimales a mostrar, y la `f` que el dato es de coma flotante (*float*).

Ahora vamos a añadir otro número decimal, por ejemplo `153.21`, y vamos a alinear tanto la parte entera, como la coma y tres decimales:

```python
print('{:7.3f}'.format(3.141592653))
print('{:7.3f}'.format(153.21))
```
```bash
python3 salida_por_pantalla.py
  3.142
153.210
```

Al querer imprimir tres decimales debemos contar esos tres carácteres mas el carácter del punto (`.`) y los tres carácteres que representan la parte entera más grande de los dos número decimales, en total hacen 7 carácteres. Así pues, en la referencia `{:7.3f}` el 7 es la cantidad de carácteres que se van a mostrar, el `.3` la cantidad de decimales, y si el número no tiene esa cantidad de decimales por defecto rellenará con ceros por la derecha, y finalmente la letra `f` para indicar que se trata de números de coma flotante (*float*).

Si se quisiera rellenar con ceros por la izquerda en vez de espacios hay que hacer lo mismo que en el ejemplo anterior, añadir en la referencia un `0` delante del número de caracteres que ocupará la cadena:

```python
print('{:07.3f}'.format(3.141592653))
print('{:07.3f}'.format(153.21))
```
```bash
python3 salida_por_pantalla.py
003.142
153.210
```