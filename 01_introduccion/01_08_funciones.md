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

Hemos visto que podemos especificar una serie de parámetros en la definición de una función y luego pasarle valores como argumentos a la hora de hacer uso de la función, pero tal y como lo hemos visto habrá una correlación entre los argumentos y los parámteros siguiendo estrictamente el orden en el que estñan definidos. Ahora vamos a ver cómo podemos usar argumentos con nombres o claves que hagan referencia a los nombres de los parámetros, de ese modo ya no importará el orden en el que se coloquen los argumentos, véase el siguiente ejemplo en un nuevo archivo llamado `resta_de_numeros.py`:

```python
def resta(a, b):
    return a - b

print(resta(b=2, a=1))
```
```bash
python3 resta_de_numeros.py
-1
```

A la hora de hacer uso de la función `resta()` le estamos diciendo que el parámtero `b` va a valer `2` y el parámetro `a` va a valer 1. Están desordenados, pero el resultado es el que se espera.

En los parámetros de una función también podemos especificar valores por defecto, por ejemplo al parámetro `b` le vamos a asignar un valor por defecto de `5`. Esto quiere decir que ya no sería obligatorio especificar un valor para el parámetro `b`, y si no se especifica un valor para dicho su valor será siempre `5`.

```python
def resta(a, b=5):
    return a - b

print(resta(2))
```
```bash
python3 resta_de_numeros.py
-3
```

Si se especificara un valor para el parámetro `b` siempre tendrá preferencia el valor especificado, el valor por defecto se ignoraría:

```python
def resta(a, b=5):
    return a - b

print(resta(7, 3))
```
```bash
python3 resta_de_numeros.py
4
```

## Pasar información por valor y por freferencia

Cuando enviamos información a una función generalmente se suele hacer como hemos visto hasta ahora, que es un envío de información por valor. Esto significa que se crea una copia de la información que enviamos en sus propias variables, variables locales. Pero hay un caso excepcional, las colecciones, listas, diccionarios y conjuntos, estos datos se envían por referencia. Eso significa que en lugar de manejar una copia del dato dentro de la función estaremos manejando el dato original, por lo que si le realizamos alguna modificación los cambios se verán reflejados en el exterior, porque hacen referencia a la variable externa.

Veamos un ejemplo en el que pasamos información a una función por valor, para ello crearemos un nuevo archivo llamado `valor_y_referencia.py` y aquí añadiremos el siguiente código:

```python
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)

print(n)
```
```bash
python3 valor_y_referencia.py
10
```

En este caso tenemos una función llamada `doblar_valor()` que recibe un parámetro llamado `numero`, lo que hace esta función es doblar el valor del número que se le pase como argumento, como su nombre bien indica. Pero una vez definida la función, en el programa principal creamos una variable llamada `n` con valor `10`, y luego invocamos a la función `doblar_valor()` pasándole el valor de `n` como argumento. Finalmente imprimimos el valor de `n` después de haber ejecutado la función que dobla su valor. Si nos fijamos en el resultado de la ejecución del programa podremos ver que cuando imprimimos el valor de `n` no se ha doblado. Esto es correcto, la variable `n` sigue valiendo `10` después de pasarla como argumento a la función `doblar_valor()`, ya que el valor de `n` solo se copia en el interior de la función bajo una nueva variable local llamada `numero` y es esta y solo esta variable la que se dobla.

Ahora vamos a ver un ejemplo en el que vamos a pasar información a una función por referencia. El ejemplo va a ser muy parecido al anterior, solo que en este caso en vez de pasar como argumento un número entero vamos a pasar una lista. Vamos a crear una función llamada `doblar_valores()` y en su cuerpo recorreremos todos los elementos de la lista iterando a traves de ellos mediante un bucle `for`. Además de los elementos nos quedaremos con la posición de cada uno mediante el uso de `enumerate()`, finalmente a cada elemento le vamos a doblar su valor actual. En el programa principal crearemos una variable llamada `ns` con una lista de números, después se ejecuta la función `doblar_valores()` a la que se le pasará la lista `ns` como argumento y finalmente se imprime el valor de la lista `ns` en ese momento, tras ejecutar la función.

```python
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns)

print(ns)
```
```bash
python3 valor_y_referencia.py
[20, 100, 200]
```

Como se puede ver, en este caso si se ha doblado el valor inicial de cada elemento de la lista. Esto sucede por que tal y como se explicaba el inicio de este punto, las colecciones, listas, diccionarios y conjuntos se pasan a las funciones por referencia, en vez de una copia local dentro de la función se accede a los elementos que contiene el objeto original.

Si quisieramos modificar el valor de una variable de tipo entero (`int`) que se encuentra fuera de la función tendríamos que hacer un pequeño truco y modificar ligeramente el código del primer ejemplo de la siguiente manera:

```python
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)

print(n)
```
```bash
python3 valor_y_referencia.py
20
```

En este caso si se ha doblado el valor de la variable `n` tras ejecutar la función `doblar_valor()`, pero hemos tenido que añadir un `return` del valor multiplicado por dos en la función y por otro lado hemos tenido que reasignar este `return` de la función como nuevo valor de la variable `n`.

En el caso de una colección podríamos evitar que se modifique su valor haciendo otro truco y modificando ligeramente el código del segundo ejemplo. Tendríamos que pasar como argumento una copia de la lista en vez de la lista original. En Python esto se consigue mediante el *slicing* `[:]`, por ejemplo:

```python
def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2

ns = [10, 50, 100]
doblar_valores(ns[:])

print(ns)
```
```bash
python3 valor_y_referencia.py
[10, 50, 100]
```

En este caso se ha pasado como referencia una copia de la lista `ns` no la lista original, por lo que la función ha duplicado el valor de cada elemento solo de en la copia, la variable `ns` contiene una lista intacta.

## Argumentos indeterminados

Hasta ahora hemos visto dos maneras de pasar información a una función en Python, una es mediante una serie de argumentos que luego debe coincidir en número y posición con los parámetros definids en la función, y otra manera que hemos visto es mediante nombres en los parámetros, sonde ya no importa el orden. Pero ¿y si queremos pasar un número indeterminado de argumentos?

Para ver un ejemplo de cómo se puede hacer crearemos un nuevo archivo llamado `indeterminados_posicion.py` y escribiremos el siguiente código:

```python
def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5, 'Hola mundo!', [1, 2, 3])
indeterminados_posicion('aaa', 'bbb')
indeterminados_posicion(1, -15, 27, 'My name is Bobby Brown', 3.14)
```
```bash
indeterminados_posicion.py
(5, 'Hola mundo!', [1, 2, 3])
('aaa', 'bbb')
(1, -15, 27, 'My name is Bobby Brown', 3.14)
```

En la definición de la función hemos tenido que añadir `*args` (se puede llamar como se quiera, pero es el nombre más común) como parámetro, lo que quiere decir que se almacenará en una variable local `args` todos los argumentos, sean los que sean. En cada ejecución de la función `indeterminados_posicion()` se ha pasado una cantidad diferente de argumentos y de diferentes tipos. El resultado en todos los casos es una `tupla` con todos los elementos en el orden en el que fueron pasados. Recordemos que las tuplas son colecciones inalterables, no se puede modificar su contenido. En este ejemplo los argumentos que se pasen en un orden tendrán ese mismo orden dentro de la función como parámetros.

Pero si quisieramos pasar un número indeterminado de parámetros mediante una serie de nombres también podemos hacerlo. Para ello vamos a crear un nuevo archivo llamado `indeterminados_nombre.py` y escribiremos en él el siguiente código:

```python
def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n=5, c='Hola mundo!', l=[1, 2, 3])
```
```bash
python3 indeterminados_nombre.py
{'n': 5, 'c': 'Hola mundo!', 'l': [1, 2, 3]}
```

## Funciones recursivas

Una función recursiva es una función que se puede ejecutar a si misma varias veces. Tienen un comportamiento muy similar a las de las sentencias iterativas que hemos ido aprendiendo. Vamos a crear un nuevo archivo llamado `funcion_recursiva.py` y vamos a escribir el sigueinte código en el que podremos ver una función que realiza una cuenta atrás recursivamente y al finalizar muestra un mensaje.

```python
def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print('Despegue!')

cuenta_atras(5)
```
```bash
python3 funcion_recursiva.py
4
3
2
1
Despegue!
```

Simplemente recibe un número como parámetro, le resta una unidad y a continuación comprueba si el nuevo valor de este numero es mayor que `0`, en cuyo caso lo imprime por pantalla y se vuelve a ejecutar a si misma. Lo más importante en una función recursiva es que esta deje de invocarse a si misma en algún momento, por lo que tenemos que meter un sistema de control en el que si se da una circunstancia que pueda parar. En este caso, en un momento dado la variable local `num` valdrá `0`, no se cumplirá la condición y el condicional saldrá por la sentencia `else` imprimiendo el mensaje y finalizando el programa.

Vamos a ver otro ejemplo clásico de función recursiva, el cálculo del factorial de un número. El factorial de un número es el entero que corresponde a ese mismo número mulptiplicado por todos los números que van antes de él hasta el 1, por ejemplo, el factorial de `5` en 120, y se calcula de la siguiente manera:

```
5! = 1 x 2 x 3 x 4 x 5 = 120
```

Vamos a implementar esta función recursiva mediante el siguiente código:

```python
def factorial(num):
    if num > 1:
        num *= factorial(num - 1)
    return num

print(factorial(5))
```
```bash
python3 funcion_recursiva.py
120
```

En este ejemplo se va multiplicando el número `5` por si mismo menos uno, hasta llegar a `1`, entonces para. Como resultado da `120`, que es el factorial de `5`.

## Funciones integradas en Python

Existen una serie de funciones que vienen integradas en el lenguaje Python. Muchas de ellas ya las estamos utilizando desde el comienzo de esta documentación, por ejemplo la función `print()` para imprmir información por pantalla, la función `format()` para darle formato a la información, las funciones `range()` y `enumerate()` para hacer más fáciles las ieraciones de algunos datos, etc. Pero existen muchas otras, en este punto veremos algunas de ellas, y para ello vamos a crear el archivo `funcion_integrada.py`.

Por ejemplo, existen algunas funciones, que también hemos utilizado anteriormente, que sirven para convertir información de un tipo a otro, esto se conoce como *casting* , como es el caso de las funciones `int()`, `float()`, `str()`, `list()`, etc.

Veamos un ejemplo en el que tenemos una variable de tipo cadena de texto o *string* y mediante la función `int()` vamos a convertirla en una variable con un dato de tipo entero o *integer*:

```python
numero = '3'
print('Aquí la variable numero tiene un valor de {} de tipo {}'.format(numero, type(numero)))

numero = int('3')
print('Aquí la variable numero tiene un valor de {} de tipo {}'.format(numero, type(numero)))
```
```bash
python3 funcion_integrada.py
Aquí la variable numero tiene un valor de 3 de tipo <class 'str'>
Aquí la variable numero tiene un valor de 3 de tipo <class 'int'>
```

Lo mismo con los números de coma flotante o *float*, podremos usar la función `float()` para hacer el *casting* de un valor de tipo cadena de texto o *string* a un dato de tipo *float* de la siguiente manera:

```python
numero = '3.14'
print('Aquí la variable numero tiene un valor de {} de tipo {}'.format(numero, type(numero)))

numero = float('3.14')
print('Aquí la variable numero tiene un valor de {} de tipo {}'.format(numero, type(numero)))
```
```bash
python3 funcion_integrada.py
Aquí la variable numero tiene un valor de 3.14 de tipo <class 'str'>
Aquí la variable numero tiene un valor de 3.14 de tipo <class 'float'>
```

