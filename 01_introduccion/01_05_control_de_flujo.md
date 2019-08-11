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

Como podemos comprobar el código de nuestra sentencia if cada vez se va haciendo más grande, en realidad ya empieza a coger forma y resulta que estamos haciendo un pequeño programa, esto empieza a ser un poco más complicado de manejar desde una consola de Python, así que lo mejor es que comencemos a escribir nuestro código dentro de un archivo al que llamaremos `mi_programa.py` de modo que quede de la siguiente manera:

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

Para ejecutar un programa Python contenido en un archivo se ha de hacer de la siguiente forma desde la consola:

```bash
python3 mi_programa.py
Saliendo del sistema ...
```

Como se puede comprobar funciona perfectamente, muestra el mensaje que tiene que mostrar.