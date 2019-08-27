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
texto = 'me llamo Javier'
numero = 3

print('Hola,', texto, 'y mi número favorito es el', numero)
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier y mi número favorito es el 3
```

Esta es una manera muy simple de imprmimir cadenas de texto mezcladas con variables de diferentes tipos, pero si queremos tener un mayor control sobre las variables que queremos imprimir debemos comenzar a usar un formato de escritura de las cadenas de carácteres, en Python se hace con el método `.format()`, por ejemplo:

```python
texto = 'me llamo Javier'
numero = 3

print('Hola, {} y mi número favorito es el {}'.format(texto, numero))
```
```bash
python salida_por_pantalla.py
Hola me llamo Javier y mi número favorito es el 3
```

Como se puede ver, hemos creado todo el contenido a imprimir dentro de la función `print()` y hemos añadido unas referencias mediante llaves `{}` donde irá el valor de las variables que se declaran dentro del método `.format()`, respetando el mismo orden y separadas por coma. Al ejecutar el programa el resultado es el mismo.

