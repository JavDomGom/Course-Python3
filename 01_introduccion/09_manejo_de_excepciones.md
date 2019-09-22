# Manejo de excepciones

En programación muchas veces podríamos tener un error de retorno a la hora de evaluar una expresión o de invocar a un método, función, procedimiento o clase, tanto de nuestro propio código como integrado en el lenguaje, tal y como ya hemos visto en el punto  anterior. Para poder tener un control más exhaustivo sobre el comportamiento de nuestro programa es muy importante hacer uso de las excepciones que el lenguaje nos permita, de ese modo podremos indicarle al programa qué hacer cuando algo no suceda como se espera. En este punto veremos cómo identificar los errores y cómo gestionarlos mediante excepciones.

## Errores

Cuando ejecutamos un programa podemos encontrarnos errores de diferentes tipos, por ejemplo errores sintácticos, que son aquellos que tienen que ver con la propia escritura del código, tales como un bloque de código mal indentado, un paréntesis sin cerrar, un carácter de más, la ausencia de un argumento cuando debería ser obligatorio, etc.

En el siguiente ejemplo vamos a provocar algún error de sitaxis para poder verlos en detalle. Para ello crearemos un nuevo archivo llamado `excepciones.py` con el siguiente código:

```python
print('Hola mundo!'
```
```bash
python3 excepciones.py
  File "excepciones.py", line 2

                       ^
SyntaxError: unexpected EOF while parsing
```

En este caso hemos eliminado el cierra de paréntesis a la hora de usar la función integrada `print()`, lo que ha provocado el correspondiente error de sintáxis. La mayoría de los entornos de desarrollo nos suelen avisar de los errores de sintaxis como el que acabamos de ver, suele aparecer el error subrallado e incluso aparecer un mensaje emergente que indica en qué nos hemos equivocado.

Sin embargo, no todos los errores en el código son tan fáciles de dentificar, como pasa con los errores semánticos. Estos errores son los que están ligados al uso de los recursos que tenemos disponibles para utilizar en nuestro código. Por ejemplo, algo que para nosotros debería ser correcto en la mayoría de situaciones, pero que bajo una determinada circunstancia podría no funcionar como se espera. Estos son los errores más difíciles de identificar.

Veamos un ejemplo en el que tenemos una lista de varios elementos, invocaremos varias veces al método `pop()` para ir eliminando de la lista uno a uno todos los elementos, y finalmente veremos qué error nos devuelve el programa cuando queremos sacar elementos de una lista que ya está vacía. Dicho de otra manera, vamos a sacar 4 elementos de una lista que solo contiene 3 elementos:

```python
lista = [1, 2, 3]   # Lista con 3 elementos

lista.pop()         # Sacamos el primer elemento
lista.pop()         # Sacamos el segundo elemento
lista.pop()         # Sacamos el tercer elemento
lista.pop()         # Sacamos un cuarto elemento que no existe
```
```bash
python3 excepciones.py
Traceback (most recent call last):
  File "excepciones.py", line 6, in <module>
    lista.pop()         # Sacamos un cuarto elemento que no existe
IndexError: pop from empty list
```

Nos ha dado un error semántico, es decir, no hemos ejecutado nada que estuviera mal escrito o incompleto, solo hemos usado una instrucción correcta en una situación en la que ya no se debería usar, ya que no hay más elementos en la lista. ¿Cómo podemos controlar este tipo de errores para que no falle el programa?

Podríamos hacerlo de diferentes maneras, pero una buena idea sería comprobar la longitud de la lista (número de elementos) antes de sacar un elemento, de modo que si la longitud es `0` no sería necesario sacar más elementos. Veamos cómo en el siguiente ejemplo:

```python
lista = [1, 2, 3]

print(lista)

if len(lista) > 0: # True
    lista.pop()    # Saca elemento de lista
    print(lista)   # Se imprime valor de lista actualizado

if len(lista) > 0: # True
    lista.pop()    # Saca elemento de lista
    print(lista)   # Se imprime valor de lista actualizado

if len(lista) > 0: # True
    lista.pop()    # Saca elemento de lista
    print(lista)   # Se imprime valor de lista actualizado

if len(lista) > 0: # False
    lista.pop()    # Esta línea no se ejecutará
    print(lista)   # No se imprimirá valor de lista
```
```bash
python3 excepciones.py
[1, 2, 3]
[1, 2]
[1]
[]
```

En este ejemplo aparece una parte del código que se repite varias veces, para optimizarlo lo modificaremos para usar una función recursiva que ejecute una acción tantas veces como sea necesario hasta que se cumpla la condición de que la lista tenga una longitud igual a `0`:

```python
lista = [1, 2, 3]

def comprueba_lista(l):
    print(l)
    if len(l) > 0:
        l.pop()
        comprueba_lista(l)

comprueba_lista(lista)
```
```bash
python3 excepciones.py
[1, 2, 3]
[1, 2]
[1]
[]
```

Al ejecutar el programa obtendremos el mismo resultado, pero habremos optimizado mucho la ejecución mediante el uso de una función recursiva.

Otro erro bastante común es cuando leemos un valor por teclado e intentamos realizar una operación matemática con ese valor. Todos los valores que se introducen por teclado son de tipo *string* a no ser que hagamos un *casting* y lo convirtamos en otro tipo diferente. A continuación un ejemplo en el que se reproduce el error que devuelve el programa al no convertir los datos introducidos por teclado a un número entero (`int`) o de coma flotante (`float`):

```python
a = input('Introduce un número: ')
b = 3

print('{}/{} = {}'.format(a, b, a/b))
```
```bash
python3 excepciones.py
Introduce un número: 15
Traceback (most recent call last):
  File "excepciones.py", line 5, in <module>
    print('{}/{} = {}'.format(a, b, a/b))
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

Como se ha comentado antes, para solventar este error bastaría con hacer un *casting* del `input`, en este caso a número de coma flotante o `float` de la siguiente manera:

```python
a = float(input('Introduce un número: '))
b = 3

print('{}/{} = {}'.format(a, b, a/b))
```
```bash
python3 excepciones.py
Introduce un número: 15
15.0/3 = 5.0
```

Ahora ya no devuelve un error, hace el cálculo correctamente. Pero, ¿y si el usuario introducen unas letras en vez de un número? Obtedríamos el siguiente error:

```bash
python3 excepciones.py
Introduce un número: abc
Traceback (most recent call last):
  File "excepciones.py", line 1, in <module>
    a = float(input('Introduce un número: '))
ValueError: could not convert string to float: 'abc'
```

Esto sucede porque no se puede convertir una cadena de texto a un número `float`. ¿Cómo entonces podremos asegurarnos que el usuario va a introducir un número y cómo se puede controlar el programa en caso de que este no lo haga correctamente? Para ello existen las excepciones, las cuales trataremos en el siguiente punto.

## Excepciones

Una excepción es un bloque de código excepcional que nos permitirá continuar con la ejecución del programa aunque ocurra un error. En el punto anterior hemos visto un programa que pide introducir un número, pero no estábamos controlando el caso de error en el que el usuario introduzca por teclado algo diferente de un número. Vamos a crear una excepción para este caso. Para ello debemos colocar todo el código propenso a errores dentro del cuerpo de una sentencia llamada `try`. A continuación se creará otro bloque llamado `except` y este contendrá en su cuerpo aquel código que queremos que se ejecute cuando exista algún error en el código que hay dentro de `try`, veamos el código:

```python
try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(a, b, a/b))
except:
        print('Ha ocurrido un error, introduce bien el número.')
```
```bash
python3 excepciones.py
Introduce un número: abc
Ha ocurrido un error, introduce bien el número.
```

Como se puede ver, el programa intenta capturar un número por teclado, pero si el usuario no introduce un número el programa no falla, simplemente ejecuta el código que hay dentro de `except`, en este caso solo un printo con un mensaje personalizado de error. Solo hay una pega, tal y como está hecho el programa ahora mismo, en caso de error solo se imprime un mensaje y el programa finaliza. Podría interesarnos que además de mostrar ese mensaje que volviera a pedir introducir un número de forma indefinida hasta que el usuario intoduzca un valor correctamente. Esto lo podemos conseguir introduciéndo el código actual dentro del cuerpo de un bucle while, por ejemplo:

```python
while True:
        try:
                a = float(input('Introduce un número: '))
                b = 3

                print('{}/{} = {}'.format(a, b, a/b))
                break   # Si todo ha ido bien se interrumpe el bucle.
        except:
                print('Ha ocurrido un error, introduce bien el número.')
```
```bash
python3 excepciones.py
Introduce un número: abc
Ha ocurrido un error, introduce bien el número.
Introduce un número: wgr
Ha ocurrido un error, introduce bien el número.
Introduce un número: 27
27.0/3 = 9.0
```

Tras dos intentos fallidos hemos introducido un número correctamente y el programa ejecuta el código que hay en el cuerpor de l bloque `try` finalizando así las iteraciones del bucle y saliendo del programa con éxito.

De este modo ya estaríamos haciendo uso de las excepciones de Python, pero las excepciones abarcan mucho más que esto. En primer lugar permite añadir un bloque de código `else` para ejecutar un código en caso de que todo vaya correctamente, y ese es el lugar idóneo para poner la sentencia `break` que hemos añadido antes dentre del bloque `try`, veamos cómo mejorarlo:

```python
while True:
        try:
                a = float(input('Introduce un número: '))
                b = 3

                print('{}/{} = {}'.format(a, b, a/b))
        except:
                print('Ha ocurrido un error, introduce bien el número.')
        else:
            print('Todo ha ido bien, saliendo del programa.')
            break   # Si todo ha ido bien se interrumpe el bucle.
```
```bash
python3 excepciones.py
Introduce un número: wadf
Ha ocurrido un error, introduce bien el número.
Introduce un número: drgb
Ha ocurrido un error, introduce bien el número.
Introduce un número: 39
39.0/3 = 13.0
Todo ha ido bien, saliendo del programa.
```

## Múltiples excepciones

Python permite crear múltiples excepciones medinate identificadores. Pero para poder usar el identificador correcto primer debemos saber qué identificadores tenemos que usar en cada caso. Podríamos saberlo de antemano, pero es interesante ver cómo obtener el nombre del identificador para cada caso. Por ejemplo, vamos a reproducir el primer error que hemos visto en este capítulo, en el que no hacíamos *casting* del valor introducido por teclado y daba un error al no poder usar una cadena de caracteres para realizar un cálculo como la división. Para obtener el identificador debemos escribir el siguiente codigo:

```python
try:
        a = input('Introduce un número: ')
        b = 3

        print('{}/{} = {}'.format(a, b, a/b))
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: 15
TypeError
```

En este caso obtenemos el identificador `TypeError` para este tipo de excepciones. Una vez que ya sabemos el identificador podemos hacer una excepción exclusiva con un mensaje personalizado para cuando nuestro programa dé un error de este tipo, por ejemplo:

```python
try:
        a = input('Introduce un número: ')
        b = 3

        print('{}/{} = {}'.format(a, b, a/b))
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: 15
No se puede dividir una cadena de texto entre un número.
```

Solventaremos el error del mismo modo que lo hicimos anteriormente, introduciendo un *casting* para convertir el valor introducido por teclado a un dato de tipo `float`, pero volveremos a ejecutar el programa introduciendo por teclado una cadena de caracteres, así averiguaremos el identificador de este nuevo tipo de error:

```python
try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(a, b, a/b))
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: abc
ValueError
```

Este nuevo error que da cuando intentas convertir a `float` una cadena de texto, tiene un identificador llamdo `ValueError`, así que ya podemos hacer otra excepción personalizada para cuando nuestro programa tenga este tipo de errores, por ejemplo:

```python
try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(a, b, a/b))
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except ValueError:
        print('Debes introducir un número.')
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: abc
Debes introducir un número.
```

Ahora nuestro programa controla dos tipos de errores mediante los identificadores `TypeError` y `ValueError`, y además tenemos una tercera excepción que nos devuelve el nombre del identificador en caso de que se trate de un error de tipo distinto a los dos anteriores. Veamos qué pasa si ejecutamos nuestro programa indicando el número `0` por teclado y el número introducido es el divisor:

```python
try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(b, a, b/a))   # Orden cambiado.
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except ValueError:
        print('Debes introducir un número.')
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: 0
ZeroDivisionError
```

Obtenemos un nuevo identificador para las excepciones en las que se trata de dividir un número por cero, es algo que no está permitido, pues la división por cero es infinito. Hagamos una excpeción personalizada para este tipo de errores:

```python
try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(b, a, b/a))
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except ValueError:
        print('Debes introducir un número.')
except ZeroDivisionError:
        print('No se puede dividir por cero.')
except Exception as e:
        print(type(e).__name__)
```
```bash
python3 excepciones.py
Introduce un número: 0
No se puede dividir por cero.
```

## Invocación de excepciones

Sin duda las excepciones nos ayudan a optimizar nuestros programas y tener un control más exaustivo sobre los errores. En este punto veremos cómo se peude llamar o invocar a una excepción más allá de las maneras que ya hemos visto.

Vamos a definir una función que reciba un valor, pero si este valor es un valor especial, por ejemplo un valor nulo, llamaremos a una excepción de tipo `ValueError` que ya vimos anteriormente mediante una intrucción llamada `raise` seguida del identificador o tipo de error:

```python
def mi_funcion(algo=None):
        if algo is None:
                raise ValueError('Error, no se permite un valor nulo.')

mi_funcion()
```
```bash
python3 excepciones.py
Traceback (most recent call last):
  File "excepciones.py", line 5, in <module>
    mi_funcion()
  File "excepciones.py", line 3, in mi_funcion
    raise ValueError('Error, no se permite un valor nulo.')
ValueError: Error, no se permite un valor nulo.
```

Este es la manera en la que se puede invocar a una excepción directamente, haciendo uso de la instrucción `raise`, pero lo más común es que el programador personalice cada posible error utilizando las intrucciones `try` y `exception`, normalmente no se suelen invocar excepciones de esta manera.