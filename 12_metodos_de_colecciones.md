# Métodos de las colecciones

En este punto repasaremos algunos de los métodos más utilizados en los tipos de datos y colecciones que ya hemos visto anteriormente. Existen muchos más mátodos de los que se tratarán en este punto, pero se tratarán aquellos que son más relevantes o más usados por la mayoría de los usuarios.

Para que el estudio de estos métodos sea más ágil y eficaz trabajaremos desde la consola de Python en vez de escribir los ejemplos en un archivo. De este modo se podrá experimentar en tiempo real lo que sucede con los datos y al invocar los métodos que vayamos utilizando.

Para acceder a la consola de Python basta con abrir un terminal y escribir simplemente `python3`, por ejemplo:

```python
python3
Python 3.7.0 (default, Jun 28 2018, 07:39:16)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Tras los tres carácteres `>>>` ya podemos empezar a escribir código python. Para salir bastaría con escribir el método `exit()`.

```python
>>> exit()
```

A continuación se pondrán algunos breves ejemplos de cada tipo de dato o colección.

## Métodos en cadenas de texto

Todos los caracteres alfabeticos a mayúsculas:

```python
>>> 'Hola Mundo'.upper()
'HOLA MUNDO'
```

Todos los caracteres alfabeticos a minúsculas:

```python
>>> 'Hola Mundo'.lower()
'hola mundo'
```

Primera letra del texto en mayúscula:

```python
>>> 'hola mundo'.capitalize()
'Hola mundo'
```

Primera letra de cada palabra en mayúscula:

```python
>>> 'hola mundo'.title()
'Hola Mundo'
```

Contabilizar el número de veces que aparece una subcadena o carácter dentro de una cadena:

```python
>>> 'Hola mundo'.count('o')
2
```
```python
>>> 'Hola mundo'.count('mundo')
1
```

Buscar los índices de aparición de una subcadena, es decir, el lugar en el que aparecen:

```python
>>> 'Hola mundo'.find('mundo')
5
```

Buscar el índice de la última aparición de una subcadena:

```python
>>> 'Hola mundo mundo mundo'.rfind('mundo')
17
```

Comprobar si una cadena de texto está compuesta únicamente por números:

```python
>>> c = '100'
>>> c.isdigit()
True
```

Comprobar si una cadena de texto está compuesta por carácteres alfanuméricos:

```python
>>> c = 'abcd1234'
>>> c.isalnum()
True
```

Comprobar si una cadena de texto está compuesta únicamente por letras:

```python
>>> c = 'abcd'
>>> c.isalpha()
True
```
El espacio no en una letra.
```python
>>> c = 'Hola mundo'
>>> c.isalpha()
False
```

Comprobar si todos los carácteres son letras minúsculas:

```python
>>> c = 'hola mundo'
>>> c.islower()
True
```

Comprobar si todos los carácteres son letras mayúsculas:

```python
>>> c = 'HOLA MUNDO'
>>> c.isupper()
True
```

Comprobar si la primera letra de cada palabra es mayúscula:

```python
>>> c = 'Hola Mundo'
>>> c.istitle()
True
```

Comprobar si una cadena está compuesta por espacios o tabulaciones:

```python
>>> c = '   '
>>> c.isspace()
True
```

Comprobar si una cadena comienza por un carácter o subcadena concreta:

```python
>>> c ='Hola mundo'
>>> c.startswith('H')
True
>>> c.startswith('Hola')
True
```

Comprobar si una cadena termina con un carácter o subcadena concreta:

```python
>>> c.endswith('o')
True
>>> c.endswith('mundo')
True
```

Separar una cadena en una lista de subcadenas a partir un caracter que haga de delimitador, por ejemplo el espacio:

```python
>>> c ='Hola mundo mundo'
>>> c.split()
['Hola', 'mundo', 'mundo']
```

El mismo ejemplo pero con el carácter `;` como delimitador:

```python
>>> c ='aaa;bbb;ccc'
>>> c.split(';')
['aaa', 'bbb', 'ccc']
```

Añadir un carácter o subcadena entre cada carácter de una cadena, por ejemplo una coma o un guión bajo:

```python
>>> ','.join(c)
'H,o,l,a, ,m,u,n,d,o'
>>> '_'.join(c)
'H_o_l_a_ _m_u_n_d_o'
```

Eliminar todos los carácteres o subcadenas que aparezcan al inicio y al final de una cadena, por ejemplo espacios:

```python
>>> c ='     Hola mundo   '
>>> c.strip()
'Hola mundo'
```

O el mismo ejemplo con guiones medios:

```python
>>> c ='--------Hola mundo---'
>>> c.strip('-')
'Hola mundo'
```

Reemplazar un carácter o una subcadena de una cadena, por ejemplo, cambiar la letra `o` por ceros, o la palabra `mundo` por `Javier`:

```python
>>> c ='Hola mundo'
>>> c.replace('o', '0')
'H0la mund0'
>>> c.replace('mundo', 'Javier')
'Hola Javier'
```

También podemos eliminar un caracter o una subcadena un número de veces:

```python
>>> c ='Hola mundo mundo mundo mundo mundo'
>>> c.replace(' mundo', '', 3)
'Hola mundo mundo'
```

## Métodos en listas

Añadir elementos a una lista:

```python
>>> l = [1, 2, 3]
>>> l.append(4)
>>> l
[1, 2, 3, 4]
```

Eliminar todos los elementos de una lista:

```python
>>> l = [1, 2, 3]
>>> l.clear()
>>> l
[]
```

Unir los elementos de dos listas en una:

```python
>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> l1.extend(l2)
>>> l1
[1, 2, 3, 4, 5, 6]
```

Contar cuántas veces aparece un elemento en una lista:

```python
>>> l = ['Hola', 'mundo', 'mundo']
>>> l.count('mundo')
2
```

Mostrar la posición del índice en la que aparece por primera vez un elemento en una lista.

```python
>>> l = ['Hola', 'mundo', 'mundo']
>>> l.index('Hola')
0
>>> l.index('mundo')
1
```

Insertar un elemento dentro de una lista en una posición indicada:

```python
>>> l = [5, 10, 15, 25]
>>> l.insert(3, 20)
>>> l
[5, 10, 15, 20, 25]
```

Sacar un elemento en una posición indicada de una lista. Si no se indica ninguna posición sacará el último elemento.

```python
>>> l = [10, 20, 30, 40, 50]
>>> l.pop()
50
>>> l
[10, 20, 30, 40]
>>> l.pop(1)
20
>>> l
[10, 30, 40]
```

Brrar un elemento de la lista indicando el propio elemento. Si hay varios solo borra el primero:

```python
>>> l = ['uno', 'dos', 'tres']
>>> l
['uno', 'dos', 'tres']
>>> l.remove('dos')
>>> l
['uno', 'tres']
```

Invertir el orden de los elementos de una lista:

```python
>>> l = [1, 2, 3, 4, 5]
>>> l.reverse()
>>> l
[5, 4, 3, 2, 1]
>>> l = ['uno', 'dos', 'tres']
>>> l.reverse()
>>> l
['tres', 'dos', 'uno']
```

Ordenar elementos de una lista:

```python
>>> l = [3, -15, 27, -9, 0]
>>> l.sort()
>>> l
[-15, -9, 0, 3, 27]
>>> l = ['bbb', 'eee', 'ttt', 'ccc']
>>> l.sort()
>>> l
['bbb', 'ccc', 'eee', 'ttt']
```

## Métodos en conjuntos

Añadir elementos a un conjunto:

```python
>>> c = set()
>>> c.add(1)
>>> c.add(2)
>>> c.add(3)
>>> c
{1, 2, 3}
```

Descartar o borrar un elemento específico de un conjunto:

```python
>>> c = {1, 2, 3}
>>> c
{1, 2, 3}
>>> c.discard(2)
>>> c
{1, 3}
>>> c = {'uno', 'dos', 'tres'}
>>> c
{'dos', 'uno', 'tres'}
>>> c.discard('dos')
>>> c
{'uno', 'tres'}
```

Hacer una copia de un conjunto existente.

```python
>>> c1 = {1, 2, 3}
>>> c2 = c1.copy()
>>> c2.discard(2)
>>> c1
{1, 2, 3}
>>> c2
{1, 3}
```

Los conjuntos tienen un método integrado propio `copy()`, no confundir con el método `copy()` del módulo `copy` qie importábamos para hacer copias de objetos de clases.

Vaciar o eliminar por completo todos los elementos de un conjunto:

```python
>>> c = {1, 2, 3}
>>> c
{1, 2, 3}
>>> c.clear()
>>> c
set()
```

Comprobar que un conjunto es disjunto de otro, es decir, que no hay ningún elemento en común con otro conjunto:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {3, 4, 5}
>>> c3 = {-1, 99}
>>> c1.isdisjoint(c2)
False
>>> c1.isdisjoint(c3)
True
```

Comprobar si un conjunto es un subconjunto de otro:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {1, 2, 3, 4}
>>> c1.issubset(c2)
True
```

Comprobar si un conjunto es un superconjunto de un subconjunto:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {1, 2, 3, 4}
>>> c2.issuperset(c1)
True
```

Unión de dos conjuntos. Si hay elementos repetidos estos no se añaden varias veces:

```python
>>> c1 = {1, 2, 3, 4, 5}
>>> c2 = {3, 4, 5, 6, 7}
>>> c1.union(c2)
{1, 2, 3, 4, 5, 6, 7}
```

Pero esto no actualiza el valor de ningún conjunto, solo muestra por pantalla el resultado de la unión. Si vemos lo que contienen los conjuntos `c1` y `c2` veremos que no han mutado:


```python
>>> c1
{1, 2, 3, 4, 5}
>>> c2
{3, 4, 5, 6, 7}
```

Para que se actualice el valor del primer conjunto con la unión de ambos conjuntos como valor se ha de usar el método `update()` de la siguiente manera:


```python
>>> c1 = {1, 2, 3, 4, 5}
>>> c2 = {3, 4, 5, 6, 7}
>>> c1.update(c2)
>>> c1
{1, 2, 3, 4, 5, 6, 7}
```

Encontrar elementos que no son comunes o que son distintos entre dos conjuntos:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {3, 4, 5}
>>> c1.difference(c2)
{1, 2}
>>> c2.difference(c1)
{4, 5}
```

Actualizar los elementos de un conjunto con los no comunes de un segundo conjunto:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {3, 4, 5}
>>> c1.difference_update(c2)
>>> c1
{1, 2}
```

Encontrar los elementos comunes entre dos conjuntos:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {3, 4, 5}
>>> c1.intersection(c2)
{3}
```

Al igual que antes con el método `difference()` este solo devuelve un resultado, pero no actualiza el valor de ningún conjunto.

```python
>>> c1
{1, 2, 3}
>>> c2
{3, 4, 5}
```

Actualizar los elementos de un conjunto con los elementos comunes de un segundo conjunto:

```python
>>> c1 = {1, 2, 3}
>>> c2 = {3, 4, 5}
>>> c1.intersection_update(c2)
>>> c1
{3}
```

## Métodos en diccionarios

Obtener un valor por defecto cuando queremos acceder a una clave que no existe en un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.get('amarillo', 'No se encuentra')
'yellow'
>>> colores.get('negro', 'No se encuentra')
'No se encuentra'
```

Obtener una lista con las claves de un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.keys()
dict_keys(['amarillo', 'azul', 'verde'])
```

Obtener una lista con los valores de las claves de un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.values()
dict_values(['yellow', 'blue', 'green'])
```

Obtener una lista de tuplas con la clave y valor de cada elemento de un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.items()
dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
```

Sustraer o eliminar una clave y su valor de un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.pop('amarillo')
'yellow'
>>> colores
{'azul': 'blue', 'verde': 'green'}
```

Si quisieramos extraer de un diccionario un elemento o registro que no existe, por ejemplo `negro`, podríamos añadir al método `pop()` un texto a mostrar en este caso:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.pop('negro', 'No se encuentra')
'No se encuentra'
```

Vaciar o eliminar todos los elementos de un diccionario:

```python
>>> colores = {'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores
{'amarillo': 'yellow', 'azul': 'blue', 'verde': 'green'}
>>> colores.clear()
>>> colores
{}
```
