# Manejo de excepciones

En programación muchas veces podríamos tener un error de retorno a la hora de evaluar una expresión o de invocar a un método, función, procedimiento o clase, tanto de nuestro propio código como integrado en el lenguaje, tal y como ya hemos visto en el punto  anterior. Para poder tener un control más exhaustivo sobre el comportamiento de nuestro programa es muy importante hacer uso de las excepciones que el lenguaje nos permita, de ese modo podremos indicarle al programa qué hacer cuando algo no suceda como se espera. En este punto veremos cómo identificar los errores y cómo gestionarlos mediante excepciones.

# Errores

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
