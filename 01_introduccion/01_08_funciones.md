## Funciones

Las funciones son fragmentos de código que se pueden invocar o ejecutar varias veces gracias a un nombre único que las identifica. Estas pueden recibir y devolver información para comunicarse con el programa principal. Crearemos un archivo llamado `funciones.py` en el que iremos añadiendo código a medida que vayamos aprendiendo los conceptos y el funcionamiento de las funciones en Python.


## Definición de funciones

Para definir una función primero debemos utilizar la palabra rservada `def`, a continuación el nombre que le queramos poner a la función, después apertura y cierre de paréntesis sin nada en su interior `()` y finalmente dos puntos `:`. En la linea siguiente debemos dejar una identación o tabulación a la izquierda y a continuación el código que queremos que se ejecute al invocar a esta función, por ejemplo:

```python
def saludo():
    print('Hola mundo!')
```

Hasta aquí ya tenemos el código de una función. Pero ahora debemos añadir la línea de código para ivocarla, bastaría con escribir simplemente el nombre de la función y los paréntesis, por ejemplo:

```python
def saludo():
    print('Hola mundo!')

saludo()
```

Si ejecutamos nuestro programa `funciones.py` se obtendrá la siguiente salida por pantalla:

```bash
python3 funciones.py
Hola mundo!
```

Al igual que con las variables, es recomendable utilizar nombres en minúsculas, sin acentos ni carácteres que no sean alfanuméricos y el guión bajo `_`. También se puede usar *camelcase*, es decir, poner nombres compuestos por varias palabras sin guiones bajos ni espacios y poniendo en mayúscula solo la primera letra de cada palabra menos la primera, por ejemplo `miFuncionParaSaludar` o `cerrarPrograma`.

Vamos a crear un ejemplo un poco más complicado que un simple saludo, por ejemplo una función que muestre por pantalla la tabla de multiplicar del número 5:

```python
def tabla_de_multiplicar_del_5():
    for i in range(10):
        print('5 * {} = {}'.format(i, i*5))

tabla_de_multiplicar_del_5()
```
```bash
python3 funciones.py
5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
```

En este caso hemos utilzado un bucle `for()` para iterar a través de todos los valores comprendidos entre `0` y `9`, esto lo conseguimos mediante `range(10)`, y cada valor del rango en la iteración lo almacenaremos en la variable temporal `i`. Después se añadre dentro del cuerpo del bucle `for()` un `print()` de un mensaje que contiene dos referencias, la primera mostrará el valor de `i` en ese momento y la segunda mostrará el resultado de multplicar `i` por `5`.

Dentro del cuerpo de una función podremos crear nuevas variables y utilizar cualquier sentencia de las ya vistas, e incluso llamar a otras funciones. Es muy importante tener en cuenta que cuando se define una variable nueva dentro del cuerpo de una función, esta variable solo estará disponible y visible dentro del cuerpo de la función, no fuera. Veamos un ejemplo en el que provocaremos un error al tratar de utilizar fuera de la función una variable definida dentro de la función:

```python
def mi_funcion():
    nombre = 'Frank'

print(nombre)
```
```bash
python3 funciones.py
Traceback (most recent call last):
  File "funciones.py", line 4, in <module>
    print(nombre)
NameError: name 'nombre' is not defined
```

El error dice que la variable `nombre` que quiero utilizar en la línea 4 de mi programa no existe. Sin embargo dentro de la función se ha creado, lo que sucede es que esta función la hemos creado en un ámbito local, lo que quiere decir que no estará disponible fuera de la función.

Veamos otro ejemplo en el que definimos una variable `nombre` fuera de la función, al inicio de nuestro código, y después en la función vamos a hacer uso de esa variable. Finalmente invocaremos la función:

```python
nombre = 'Frank'

def mi_funcion():
    print(nombre)

mi_funcion()
```
```bash
python3 funciones.py
Frank
```

En este caso si tenemos la variable `nombre` disponible dentro de la función porque es una variable definida en un ámbito global. El único requisito que necesita una variable global para ser utilizada en funciones es que esta variable debe estar definida antes de la llamada a la función, si no daría un error indicando que se está utilizando una variable que no existe.

## Retorno de valores

Hemos visto que una variable dentro de una función no tiene alcance fuera de ella. Para conectar la función con el exterior podemos devolver valores al programa principal. Esto se realiza con la palabra reservada `return` en el cuerp de la función. Veamos un ejemplo en el que la función `mi_funcion` devuelve una cadena de texto al ser ejecutada, en este caso se ejecutará dentro de un `print()`:

```python
def mi_funcion():
    return 'Una cadena de texto'

print(mi_funcion())
```
```bash
python3 funciones.py
Una cadena de texto
```

También podemos asignar a una variable el valor devuelto por la función para poder utilizarlo varias veces en el programa principal sin necesidad de invocar a la función cada vez que se quiera utilizar es valor, por ejemplo:

```python
def mi_funcion():
    return 'Hola mundo!'

saludo = mi_funcion()

print(saludo)
print(saludo)
print(saludo)
```
```bash
python3 funciones.py
Hola mundo!
Hola mundo!
Hola mundo!
```

La función se ha invocado una sola vez, se ha almacenado su retorno en la variable `saludo` y luego hemos utilizado varias veces la variable. Hay que tener en cuenta que cuando en una función se ejecuta una línea que contiene un `return` esta devuelve el dato que tenga que devolver y finaliza la ejecución de la función, no ejecutaría las líneas que pudiera tener por debajo.

Las funciones pueden devolver cualquier tipo de dato de los disponibles en Python y que hemos visto al principio. Veamos un ejemplo en el que la función devuelve un dato de tipo `lista`, y veamos también cómo podemos utilizar índices y *slicing* con el valor devuelto.

```python
def mi_funcion():
    return [1, 2, 3, 4, 5]

print(mi_funcion())       # La lista entera
print(mi_funcion()[0])    # Solo el primer elemento
print(mi_funcion()[-1])   # Solo el último elemento
print(mi_funcion()[1:4])  # Solo desde el segundo hasta el cuarto
```
```bash
python3 funciones.py
[1, 2, 3, 4, 5]
1
5
[2, 3, 4]
```

En este ejemplo estamos ejecutando la función 4 veces, esto complica un poco la ejecución del programa, por lo que es recomendable asignar a una variable el valor que devuelve la función, tal y como hemos visto antes con una cadena de texto, y utilizar la variable. De ese modo solo se ejecutaría la función una vez y el resultado sería el mismo.

```python
def mi_funcion():
    return [1, 2, 3, 4, 5]

lista_numeros = mi_funcion()

print(lista_numeros)
print(lista_numeros[0])
print(lista_numeros[-1])
print(lista_numeros[1:4])
```
```bash
python3 funciones.py
[1, 2, 3, 4, 5]
1
5
[2, 3, 4]
```

Las funciones en Python no tienen por que devolver solo un dato, pueden devolver varios datos separados por coma, y estos no tienen por qué ser del mismo tipo. Veamos un ejemplo en el que nuestra función devuelve tres datos diferentes, una cadena de texto, un número y una lista:

```python
def mi_funcion():
    return 'Hola', 77, [1, 2, 3]

resultado = mi_funcion()

print(resultado)
```
```bash
python3 funciones.py
('Hola', 77, [1, 2, 3])
```

El valor que de devuelve es una colección de tipo `tupla` como las que ya hemos visto anteriormente, y como ya sabemos, las tuplas son colecciones inalterables y que pueden contener datos de diferentes tipos.

Podemos aprovechar este retorno de varios datos (del mismo tipo o no) para asignar cada valor devuelto a diferentes variables en una sola línea de la siguiente manera:

```python
def mi_funcion():
    return 'Hola', 77, [1, 2, 3]

cadena, numero, lista = mi_funcion()

print(cadena)
print(numero)
print(lista)
```
```bash
python3 funciones.py
Hola
77
[1, 2, 3]
```

Como se puede ver, se asignará cada valor devuelto, del tipo que sea, a cada variable, siguiendo el mismo orden separadas por comas.

## Enviando valores

Ya hemos visto cómo las funciones pueden devolver información desde su interior al programa principal, pero también pueden recibir información desde el programa principal a su interior. Esto se consigue mediante argumentos. Para ello vamos a crear un nuevo archivo llamado `suma_de_numeros.py` y dentro escribiremos el código de un simple programa python que utilice una función que sume dos números. Estos dos números que sumará serán números que podrá recibir como parámetros:

```python
def suma(a, b):
    return a + b

print(suma(1, 2))
print(suma(27, -14))
```
```bash
python3 suma_de_numeros.py
3
13
```

En este caso si que nos interesa ejecutar la misma función tres veces. El código de la función que se va a ejecutar cada vez es exactamente el mismo, lo único que cambia son los argumentos que pasamos a la hora de llamar a la función, a veces pasamos los valores `1` y `2`, y otras veces pasamos los valores `27` y `-14`. No importa qué números pasemos, la función devolverá mediante la instrucción `return` el resultado de lo que pasemos como `a` más lo que pasemos como `b`.

## Argumentos y parámetros

Los parámetros son aquellas claves que se definen dentro de los paréntesis a la hora de definir una función, en este caso los parámetros son `a` y `b`:

```python
def suma(a, b):
```

Y los argumentos son aquellos valores que introducimos dentro de los paréntesis cuando hacemos uso de la función, en este ejemplo los argumentos son `1` y `2` o `27` y `-14`:

```python
print(suma(1, 2))
print(suma(27, -14))
```

Es importante tener en cuenta que el mero hecho de definir parámetros dentro de los paréntesis de la función cuando definimos esta con `def` estamos creando variables locales, es decir, nombres de variables que solo estarán disponibles en el cuerpo de la función, en este caso las variables serán `a` y `b`.

```python

```
```bash

```



```python

```
```bash

```



```python

```
```bash

```