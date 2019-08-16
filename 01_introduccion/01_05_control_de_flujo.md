# Control de flujo

El flujo de un programa es la sucesión de accines que se irán ejecutando en un programa. Veremos los diferentes controles de flujo que tenemos disponibles en Python como el control de flujo `condicional` en el que se podrá elegir la ejecución de una acción u otra, o el control de flujo `iterativo`, que repetirá un bloque de instrucciones hasta que se cumpla una condición específica.

## Sentencia if

Se trata de una sentencia disponible en la mayoria de los lenguajes de programación, y cómo no también en Python. Permite dividir el flujo en diferentes caminos. La manera de escribir un bloque de código que contenga una sentencia `if` es la siguiente:

```python
if True:
    print('Hello world!')
```

Comienza con la palabra reservada `if`, seguido de una expresión. Python evaluará si esa expresión devuelve `True` o `False`, y solo ejecutará el bloque de código que viene a continuación si la evaluación de la expresión resulta `True`. A continuación de la expresión se han de escribir el símbolo de los dos puntos `:` para indicar que el fin de la expresión a evaluar. En Python es imprescindible que el código que venga a continuación de un condicional `if` esté indentado, es decir, que tenga una tabulación por delante, en este caso se imprimirá el mensaje "`Hello world!`" única y exclusivamente si al evaluar la expresión del condicional `if` resulta `True`, pero como hemos puesto una expresión lógica `True` sin más siempre será verdadero, por lo tanto se imprimirá siempre el mensaje.

Veamos otro ejemplo de condicional `if` con otra expresión diferente:

```python
>>> if 3 > 1:
...     print('Esta expresión es verdadera.')
...
Esta sentencia es verdadera.
```

En esta ocasión la expresión a evaluar es si se cuple que el número `3` es mayor que el número `1`, y como sí lo es se imprimirá el mensaje "`Esta expresión es verdadera.`".

Veamos otro tipo de expresiones que también se pueden evaluar, por ejemplo expresiones con operadores relacionales como `==`, `!=`, `<`, `<=`, `>` o `>=`, :

```python
>>> if 3 + 2 == 5:
...     print('Es verdadero.')
...
Es verdadero.
```

```python
>>> saludo = 'Hola'
>>> if len(saludo) >= 7:
...     print('saludo tiene una longitud mayor o igual que 7.')
...
```

En este caso la variable `saludo`, que tiene una longitud de `4`, no cumple la condición de que su logitud sea mayor o igual a `7`, por lo tanto no se imprimirá ningún mensaje.

Veamos una condición en la que se evalúan expresiones anidadas mediante una conjunción `and`:

```python
>>> a = 5
>>> b = 17
>>> if a < b and a * 4 > b:
...     print('Esta expresión es verdadera.')
...
Esta sentencias es verdadera.
```

En este caso si se imprime el mensaje porque tanto la expresión `a < b` como la expresión `a * 4 > b` son verdaderas. Veamos otro ejemplo con una disyunción `or`:

```python
>>> a = 0
>>> b = 5
>>> if a > b or 25 % b == 0:
...     print('Esta expresión es verdadera.')
...
Esta expresión es verdadera.
```

En este caso también se imprime el mensaje, a pesar de que la expresión `a > b` sea `False`, la segunda expresión `25 % b == 0` es `True`, y en una disyunción basta con que al menos una de las expresiones sea verdadera.

En todos estos ejemplos estamos viendo que el código que se ha de ejecutar en caso de que la expresión sea `True` no es más que una simple llamada a la función `print()` con un mensaje, pero podemos poner cualquier otro bloque de código, como por ejemplo otro condicional `if` anidado uno dentro de otro, véase el ejemplo:

```python
>>> a = 5
>>> b = 10
>>> if a == 5:
...     print('a vale', a)
...     if b == 10:
...             print('b vale', b)
...
a vale 5
b vale 10
```

Es muy importante respetar el indentado en todo momento.

Hasta ahora hemos visto cómo hacer que se ejecute un bloque de código cuando se cumple una condición, pero también podemos ejecutar código cuando la condición no se cumple. Para ello está la palabra reservada `else` y se utiliza de la siguiente manera:


```python
>>> n = 10
>>> if n > 20:
...     print('n es mayor que 20.')
... else:
...     print('n no es mayor que 20.')
...
n no es mayor que 20.
```

Además de la palabra reservada `else` también existe la palabra reservada `elif`. Funciona de forma similar a `else` solo que avalúa una expresión adicional. Se suele usar para la creación de menús interactivos, por ejemplo:

```python
>>> comando = 'SALIR'
>>> if comando == 'ENTRAR':
...     print('Bienvenido al sistema!')
... elif comando == 'SALUDAR':
...     print('Hola!')
... elif comando == 'SALIR':
...     print('Saliendo del sistema ...')
... else:
...     print('Este comando no se reconoce.')
...
Saliendo del sistema ...
```

Como podemos comprobar el código de nuestra sentencia if cada vez se va haciendo más grande, en realidad ya empieza a coger forma y resulta que estamos haciendo un pequeño programa, esto empieza a ser un poco más complicado de manejar desde una consola de Python, así que lo mejor es que comencemos a escribir nuestro código dentro de un archivo al que llamaremos `mi_primer_programa.py` de modo que quede de la siguiente manera:

```python
comando = 'SALIR'

if comando == 'ENTRAR':
    print('Bienvenido al sistema!')
elif comando == 'SALUDAR':
    print('Hola!')
elif comando == 'SALIR':
    print('Saliendo del sistema ...')
else:
    print('Este comando no se reconoce.')
```

En realidad el archivo puede tener cualquier otro nombre, este solo es uno de ejemplo. Para ejecutar un programa Python contenido en un archivo se ha de hacer de la siguiente forma desde la consola:

```bash
python3 mi_primer_programa.py
Saliendo del sistema ...
```

Como se puede comprobar funciona perfectamente, muestra el mensaje que tiene que mostrar en función del valor que tiene su variable, definido en el própio código. A partir de este momento vamos a trabajar siempre con archivos en los que escribiremos el código fuente de nuestros programas.

Vamos a desarrollar un pequeño programa en el que podamos utilizar de nuevo una sentencia `if` con `elif` y `else`, solo que esta vez incluiremos una nueva función `input()` para pedirle al usuario que introduzca un dato al ejecutar el programa. Para ello escribiremos el siguiente fragmento de código en un archivo al que llamaremos `calcular_nota.py`, será un pequeño programa que le pedirá al usuario introducir una calificación, es decir, un número cualquiera.

```python
nota = float(input('Introduce la nota: '))

if nota >= 9:
    print('Sobresaliente')
elif nota >= 7:
    print('Notable')
elif nota >= 6:
    print('Bien')
elif nota >= 5:
    print('Suficiente')
else:
    print('Insuficiente')
```

Si ejecutamos el programa podremos introducir cualquier número, automáticamente lo convertirá en un entero de coma flotante ya que lo estamos forzando así con la función `float()`. Es decir, si el usuario introduce un número `5` elprograma lo convertirá automáticamente en el número `5.0`, y si introduce un `10` lo convertirá en un `10.0`. Aquí tenemos algunas ejecuciones de nuestro programa con diferentes *inputs* de entrada, se puede ver cómo imprime un mensaje diferente en cada caso.

```bash
python3 calcular_nota.py
Introduce la nota: 10
Sobresaliente
```
```bash
python3 01_introduccion/01_05_src/calcular_nota.py
Introduce la nota: 7.5
Notable
```
```bash
python3 01_introduccion/01_05_src/calcular_nota.py
Introduce la nota: 6.9
Bien
```
```bash
python3 01_introduccion/01_05_src/calcular_nota.py
Introduce la nota: 5
Suficiente
```
```bash
python3 01_introduccion/01_05_src/calcular_nota.py
Introduce la nota: 4.9
Insuficiente
```

## Sentencia while

En esta sección trataremos la sentencia `wile`, nos servirá para realizar iteraciones. Un iteración no es más que la ejecución de una acción una o más veces, en este caso siempre y cuando cumpla como verdadera una expresión relacional o lógica. Solo finalizará cuando esa condición devuelva un valor `False`. Veamos algunos ejemplos, para ello crearemos un nuevo archivo llamado `bucle_while.py` y escribiremos en él nuestro código:

```python
c = 0

while c <= 5:
    c += 1
    print('c vale', c)
```

En este simple programa comenzamos por iniciar una variable `c` con valor `0`. A continuación iniciamos un bucle `while` que ejecutará el código que contiene en su cuerpo solo si se cumple la condición en la que se evaluará si la variable `c` en ese momento tiene un valor menor o igual que `5`. La primera vez la variable `c` vale `0`, por lo que esta expresión devolverá `True`, así que el bucle `wile` ejecutará el código con contiene. Lo primero que hace es incrementar en `1` el valor actual de `c`, por lo que en este momento, tras ejecutar esta línea `c` àsaría a valer `1`. A continuación imprime un mensaje que dice "`c vale 1`" y entonces es cuando vuelve a evaluar de nuevo la expresión inicial, solo que ahora `c` ya no vale `0`, ha pasado a valer `1`.

En esta segunda iteración se vuelve a complir que `c`sea menor o igual que `5`, por lo que repetirá el código que hay dentro del bucle `while`. Una vez más incrementará en `1`el valor de `c`, por lo que a partir de ese momento la variable `c` pasa a valer `2`. Después imprime el mensaje "`c vale 2`" y vuelve de nuevo a evaluar la expresión inicial.

Este proceso se repetirá varias veces, hasta que en una de las iteraciones el valor de `c` se incremente hasta valer `6`, en cuyo caso, al volver a evaluar la expresión inicial devolverá un `False`, pues `6`no es menor o igual que `5`. En ese momento el bucle ya no ejecutará más veces el código que contiene. A continuación un ejemplo de cómo sería la ejecución de nuestro programa con este bucle `while` que hemos escrito.

```python
python3 bucle_while.py
c vale 1
c vale 2
c vale 3
c vale 4
c vale 5
c vale 6
```

Una particularidad que tiene el bucle `wile` en Python es que puede usar la palabra reservada `else` para ejecutar una acción tras finalizar el bucle, véase el siguiente ejemplo:

```python
c = 0

while c <= 5:
    c += 1
    print('c vale', c)
else:
    print('Saliendo del bucle')
```

Si ejecutamos de nuevo nuestro programa con esta inclusión de la palabra reservada `else` veremos que el resultado es el mismo y además añade el mensaje "`Saliendo del bucle`" al finalizar este.

```bash
python3 bucle_while.py
c vale 1
c vale 2
c vale 3
c vale 4
c vale 5
c vale 6
Saliendo del bucle
```

Al igual que en otros lenguajes de programación también podemos interrumpir la ejecución del bucle `wile` con una palabra reservada llamada `break`. Por ejemplo, en nuestro programa queremos que el bucle se corte cuando la variable `c` tenga por valor `3`, para ello debemos modificar el código de nuestro progrma añadiendo un condicional `if` y utilizaremos la sentencia `break` de la siguiente manera:

```python
c = 0

while c <= 5:
    c += 1

    if c == 3:
        print('Se corta la iteración cuando c vale', c)
        break

    print('c vale', c)
else:
    print('Saliendo del bucle')

```

Se ha añadido el condicional justo debajo de el incremento de la variable `c`, y dentro del condicional se imprime un mensaje y se hace una llamada a la sentencia `break`, que finalizará las iteraciones del bucle. Veamos el resultado de la ejecución:

```bash
python3 bucle_while.py
c vale 1
c vale 2
Se corta la iteración cuando c vale 3
```

Ni siquiera llega a imprimir el mensaje que tenemos en la sentencia `else`, interrumpe el bucle `wile` del todo.

Otra sentencia que podemos utilizar en un bucle `wile` es `continue`, que a diferencia de `break` en vez de romper la ejecución simplemente se salta la iteración en la por ejemplo que se cumpla una condición. Vamos a modificar el código de nuestro programa de la siguiente manera:

```python
c = 0

while c <= 5:
    c += 1

    if c == 3:
        continue

    print('c vale', c)
else:
    print('Saliendo del bucle')

```

Solo hemos borrado el mensaje que se imprimiría en el condicional `if` cuando `c` valga `3`, y hemos sustituído la sentencia `break` por `continue`. Este sería el resultado de la ejecución de nuestro programa:

```bash
python3 bucle_while.py
c vale 1
c vale 2
c vale 4
c vale 5
c vale 6
Saliendo del bucle
```

Si nos fijamos bien, ha impreso el mensaje en el que va indicando el valor actual de la variable `c` en todo momento menos en la iteración en la que `c` vale `3`, y finalmente ha impreso el mensaje indicado en la sentencia `else`.

Antes de terminar este apartado vamos a crear un nuevo programa en el que usaremos la sentencia `wile` para crear un menú interactivo desde la consola, el programa pedirá al usuario que introduzca un valor y en función de lo que el usuario introduzca ejecutará una acción u otra. También tendrá una opción para finalizar el programa. Para ello crearemos un nuvo archivo llamado `menu.py`, el código es el siguiente:

```python
print('\n MENU \n======\n')

while True:
    print('Selecciona una opción:\n')
    print('1: Saludar')
    print('2: Sumar dos números')
    print('3: Salir\n')

    user_choice = input()

    if user_choice == '1':
        print('Hola, qué tal?')
    elif user_choice == '2':
        n1 = float(input('Introduce el primer número: '))
        n2 = float(input('Introduce el segundo número: '))
        print('El resultado de la suma es:', n1 + n2)
    elif user_choice == '3':
        print('Saliendo del programa!')
        break
    else:
        print('Opción no válida, vuelve a intentarlo.\n')
```

## Sentencia for

La sentencia `for` nos permite realizar iteraciones de una manera muy similar a la sentencia `while`, solo que reduce considerablemente la complejidad, puesto que no es necesario crear variables previamente con indices ni necesitaremos hacer incrementos con operadores de incremento. Normalmente se utiliza para iterar sobre listas o elementos compuestos en los que puede ser necesario recorrer cada uno de esos elementos. Veamos un ejemplo muy simple, crearemos un archivo nuevo llamado `bucle_for.py` y en él escribiremos el siguiente código:

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

En este simple programa creamos primero una variable llamada `numeros` de tipo lista, y como valor le asignamos una lista de números enteros del `1` al `5`. A continuación usamos la palabra reservada `for`, luefo escribimos el nombre de la variable temporal que usaremos dentro del bucle para referirnos a cada elemento por el que iteraremos, en este caso `numero`, luego la palabra reservada `in` y finalmente el nombre de la variable que contiene la información por la que realizaremos las iteraciones, en este caso nuestra lista `numeros`. A contunación vendría el cuerpo del bucle, siempre identado con una tabulación, en este caso imprimir el valor de la variable temporal `numero` que en cada iteración tendrá por valor cada uno de los elementos de la lista `numeros`.

Veamos un ejemplo de ejecución de este pequeño programa:

```bash
python3 bucle_for.py
1
2
3
4
5
```

Podemos comprobar que en cada iteración imprime el valor de la variable `numero`. Tal y como hemos escrito el código de nuestro programa no ha hecho falta acceder a cada elemento de la variable `numeros` mediante un índice, como por ejemplo `numeros[0]` o `numeros[1]`, ni tampoco ha hecho falta crear una variable a modo de contador para usarla como indice, simplemente itera de uno en uno a través de todos los elementos, desde el primero hasta el último.

Si quisiéramos tenerun control de cada elemento mediante un índice se puede realizar de varias maneras, pero Python dispone de un método llamado `enumerate()` que podremos utilizar para facilitar el proceso. Vamos a reemplazar el código de nuestro archivo `bucle_for.py` con el siguiente código de ejemplo:

```python
numeros = [1, 2, 3, 4, 5]

for indice, numero in enumerate(numeros):
    print(numeros[indice], numero)
```

Después de la sentencia `for` hemos iniciado dos variables temporales, es decir, variables que solo estarán disponibles dentro del cuerpo del bucle `for` hasta que este termine, estas variables son `indice` y `numero`. Dentro del cuerpo del bucle imprimimos cada elemento de la lista de las dos maneras disponibles que tenemos, una es mediante la propia lista `numeros` a la que accedemos a su índice mediante la variable `indice`y la otra es mediante la variable `numero`. A continuación un ejemplo de la ejecución del programa:

```bash
python3 bucle_for.py
1 1
2 2
3 3
4 4
5 5
```

Acceder a los elementos de una lista mediante un índice nos va a permitir tener un mayor control de cada elemento por el que iteramos, por ejemplo para poder editar el valor de ese elemento y que permanezca ese nuevo valor en la lista una vez termine el bucle `for`, por ejemplo, vamos a modificar el código de nuestro programa para que el tercer elemento adquiera un valor nuevo, por ejemplo su propio valor multiplicado por 3:

```python
numeros = [1, 2, 3, 4, 5]

for indice, numero in enumerate(numeros):
    if indice == 2:
        numeros[indice] *= 3

    print(numeros[indice])

print(numeros)
```

Hemos incluído al final del programa una línea qu eimprima todos los elementos de la lista, fuera del bucle `for`, pero comprobar que el cambio de valor en el tercer elemento prevalece en el valor de la lista. Si ejecutamos el programa de nuevo veremos el siguiente resultado:

```bash
python3 bucle_for.py
1
2
9
4
5
[1, 2, 9, 4, 5]
```

El tercer elemento que antes era `3` ahora es su propio valor multiplicado or 3, es decir, `9`.

La sentencia `for` no solo sirve para recorrer os elementos de una lista, también tiene otras utilidades interesantes como por ejemplo la de recorrer todos los carácteres de una variable de tipo **string** o cadena de texto, por ejemplo, modifiquemos el código de nuestro programa en el archivo `bucle_for.py` con el siguiente código:

```python
cadena = 'Hola qué tal'

for caracter in cadena:
    print(caracter)
```

Primero hemos creado una variable de tipo **string** con el mensaje "`Hola qué tal`" y luego hemos creado un bucle `for` en el que hemos creado la variable `caracter` para iterar por cada carácter de la variable `cadena`. Si ejecutamos el programa se imprimirán todos los caracteres uno a uno, incluído los espacios, que también son un carácter:

```bash
python3 bucle_for.py
H
o
l
a

q
u
é

t
a
l
```

También podemos utilizar la función `enumerate()` como en el ejemplo anterior para acceder a cada carácter de la cadena de carácteres. Veamos cómo podemos usar la función `enumerate` para acceder a cada carácter:

```python
cadena = 'Hola qué tal'

for i, c in enumerate(cadena):
    print(cadena[i], c)
```

Si ejecutamos el programa obtendremos el siguiente resultado:

```bash
python3 bucle_for.py
H H
o o
l l
a a

q q
u u
é é

t t
a a
l l
```

Como podemos ver, funciona igual que cuando usábamos el bucle `for` en el ejemplo anterior. Probemos a modificar el primer carácter "`H`" por "`X`" y veamos qué sucede en este caso:

```python
cadena = 'Hola qué tal'

for i, c in enumerate(cadena):
    if i == 0:
        cadena[i] = 'X'

    print(cadena[i], c)

print(cadena)
```

Si ejecutamos el programa nos devolverá el siguiente error:

```bash
python3 bucle_for.py
Traceback (most recent call last):
  File "01_introduccion/01_05_src/bucle_for.py", line 5, in <module>
    cadena[i] = 'X'
TypeError: 'str' object does not support item assignment
```

Esto sucede porque las variables de tipo **string** son inmutables, así que en esta ocasión no podremos modificar el valor de nungún caracter.

En un bucle `for` también podemos utilizar la función `range()`, que generará una lista entre un rango numérico, por ejemplo, si queremos imprimir los 10 primeros números utilizando la función `range()` tendríamos que editar el archivo `bucle_for.py` con el siguiente código:

```python
for numero in range(10):
    print(numero)
```

Si ejecutamos el programa obtendremos el siguiente resultado:

```bash
python3 bucle_for.py
0
1
2
3
4
5
6
7
8
9
```

La función `range()` permite introducir dos valores separados por coma entre sus paréntesis, por ejemplo si queremos obtener un rango numérico entre el número `27` y el número `31` tendríamos que escribir `range(27, 31)`, modifiquemos nuestro código para verlo:

```python
for numero in range(27, 31):
    print(numero)
```

Si ejecutamos d enuevo el programa obtendremos este otro resultado:

```bash
python3 bucle_for.py
27
28
29
30
```
