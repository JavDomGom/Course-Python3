# Operadores y expresiones

## Operadores relacionales
Son aquellos operadores que se utilizan para realizar comparaciones.  Por ejemlo, el operador "igual qué" se escribe con el símbolo igual dos veces seguidas `==`, se utiliza de la siguiente manera:

```python
>>> 'a' == 'a'
True
>>> 7 == 9
False
```

Por lo contrario, el operador "distinto de" se utiliza para comprobar si dos o elementos son diferentes, se escribe con el símbolo de exclamación seguido de un igual `!=`, véase el ejemplo:

```python
>>> 'Hola' != 'hola'
True
>>> 8 != 27
True
>>> 3 != 3
False
```

El operador "mayor qué" se escribe con el símbolo `>` y sirve para comprobar si el primer elemento es mayor que el segundo, por ejemplo:

```python
>>> 3 > 7
False
>>> 9 > 0
True
```

Existe otro operador "mayor o igual qué", se escribe `>=` y sirve para comprobar si el primier elemento es mayor o igual qué el segundo, por ejemplo:

```python
>>> 3 >= 5
False
>>> 3 >= 3
True
>>> 3 >= 2
True
```

El operador "menor qué" se escribe con el símbolo `<` y sirve para comprobar si el primer elemento es menor que el segundo, por ejemplo:

```python
>>> 21 < 15
False
>>> -15 < -7
True
```

Por último hay también un operador "menor o igual qué", se escribe `<=` y sirve para comprobar si el primier elemento es menor o igual qué el segundo, por ejemplo:

```python
>>> -25 <= 128
True
>>> 17 <= 17
True
>>> 17 <= 16
False
```

Una vez explicados los operadores relacionales se pueden utilizar para realizar algunas comprobaciones más complejas, por ejemplo, se puede comparar si el resultado de una operación aritmética es igual a un número concreto:

```python
>>> 2 + 3 == 7
False
>>> 7 - 2 == 5
True
```

O si dos listas son iguales:

```python
>>> lista_1 = [0, 1, 2]
>>> lista_2 = [2, 3, 4]
>>> lista_1 == lista_2
False
```

En este caso devuelve un `False` por que evidentemente no son iguales, tienen elementos diferentes, pero ¿y si comprobamos la igualdad entre el último elemento de la primera lista y el primero de la segunda lista?

```python
>>> lista_1[-1] == lista_2[0]
True
```

También podemos comprobar la igualdad entre la longitud de la primera lista y la longitud de la segunda lista:

```python
>>> len(lista_1) == len(lista_2)
True
```

## Operadores lógicos

La Lógica es una rama de la matemática que sirve para modelizar un problema, proporcionar su solución y nos ayuda a saber si esa solución es verdadera o falsa. En lógica existen conectivas u operadores como en las matemáticas, pero en este caso se llaman de otra manera y evalúan los enunciados o proposiciones de ambos lados de forma distinta. En Python, los dos operadores lógicos principales son la conjunción `and` (símbolo en lógica `∧`) y la diyunción `or` (símbolo en lógica `∨`). Se puede consultar la siguiente tabla de la verdad para saber qué valor se obtiene como resultado al utilizar cualquiera de los dos operadores `and` u `or` entre dos predicados como `p` y `q`:

![alt Tabla de la verdad](../img/01_tabla_de_la_verdad.png)

Véase algunos ejemplos:

```python
>>> p = True
>>> q = False
>>> p and q
False
>>> p or q
True
```

No solo podremos hacer operaciones lógicas con los valores `True` y `False`, también podremos hacerlo con expresiones algebráicas o comparaciones que terminarán devolviendo un valor booleano igualmente, por ejemplo:

```python
>>> 3 + 3 > 2
True
>>> 3 + 3 > 27
False
```

También con datosde tipo `string` o cadena de carácteres:

```python
>>> 'Hola' == 'hola' and 'b' != 'f'
False
```

En este caso el resultado es `False` ya que en una conjunción `and` para que el resultado sea `True` ambos predicados deben ser verdaderos, y en este ejemplo la cadena `'Hola'` no es igual a la cadena `'hola'`, ya que una comienza por mayúscula y la otra por minúscula.

También podemos comprobar si una cadena de caracteres tiene una longitud concreta y si esta comienza por una letra determinada, véase el ejemplo:

```python
>>> cadena = 'Hola'
>>> len(cadena) >= 4 and cadena[0] == 'H'
True
```

En el caso de la disyunción `or` basta con que uno de los dos predicados sea verdadero para que el resultado sea `True`, véase el siguiente ejemplo.

```python
>>> 'Hola' == 'hola' or 'b' != 'f'
True
```

En este ejemplo `'Hola'` sigue sin ser igual a la cadena `'hola'`, pero al menos el segundo predicado es verdadero, pues el carácter `'b'` no es igual que el carácter `'f'`, por lo tanto se obtiene un resultado `True`.

Además de los operadores `and`y `or`también existe el operador `not`. Es una negación lógica o un inversor, es decir, a un valor booleano (`True` o `False`) lo convierte en el contrario, véase el siguiente ejemplo:

```python
>>> not True
False
>>> not False
True
```

## Expresiones anidadas

Podemos combinar los diferentes operadores que ya hemos visto, tales como el operador sua `+`, resta `-`, multiplicación `*`, división `/`, módulo `%` o potencias `**` y podemos combianrlos con los demás operadores relacionales como `<`, `>`, `<=`, `>=`, `==` o `!=`, los operadores lógicos como las conjunciones `and` y disyunciones `or`, e incluso podemos englobar algunas de ellas entre paréntesis `()`, pero para realizar las operaciones correctamente es importante conocer las normas de precedencia en estos casos de expresiones combinadas o anidadas. Véase el siguiente ejemplo en el que se mezclan diferentes expresiones:

```python
>>> a = 3
>>> b = 5
>>> a * b - 2**b >= 20 and not (a % b) != 0
False
```

En todo caso, las normas de precedencia a la hora de realizar operaciones combinadas o anidadas son las siguientes.

1. Las operaciones que se encuentren entre préntesis, sean del tipo que sean, aritméticas, relacionales o lógicas.
2. Después los exponentes y raíces, siempre de izquierda a derecha.
3. A contiuación las multiplicaciones, divisiones y módulo, siempre de izquierda a derecha.
4. Luego las sumas y restas, siempre de izquierda a derecha.
5. Después se han de realizar las operaciones relacionales, siempre de izquierda a derecha.
6. Finalmente las operaciones lógicas, donde el operador `not` o inversor tiene preferencia ante la conjución `and` y la disyunción `or`, el resto siempre se ha de calcular de izquierda a derecha.

Sabiendo el orden de preferencia podemos comenzar a resolver paso a paso esta expresión anidada con varias operaciones de varios tipos diferentes. El primer lugar tenemos la expresión entre paréntesis `(a % b)`, donde `a = 3` y `b = 5`, por lo tanto:

```python
>>> (a % b)
3
```

El resultado es `3` porque es el resto de vividir `3` entre `5`. Vamos a ir actualizando la expresión con los cálculos según los vayamos resolviendo, de momento se queda así:

```python
a * b - 2**b >= 20 and not 3 != 0
```

Continuamos, ahora vendrían los exponentes y las raíces. En este caso no hay raices, pero si un exponente 2**b, que es lo mismo que `2` elevado a `5`:

```python
>>> 2**5
32
```

Actualizamos la expresión:

```python
a * b - 32 >= 20 and not 3 != 0
```

Ahora vendrían las multiplicaciones y divisiones. En este caso no hay divisiones, pero si la multiplicación `a * b`, que es lo mismo que `3 * 5`:

```python
>>> a * b
15
```

Actualizamos la expresión:

```python
15 - 32 >= 20 and not 3 != 0
```

Sigamos con las sumas y restas. En este ejemplo no hay sumas, pero si la resta `15 - 32`:

```python
>>> 15 - 32
-17
```

Actualizamos la expresión:

```python
-17 >= 20 and not 3 != 0
```

En este momento ya no quedan operaciones aritéticas en la expresión, solo operaciones realcionales y lógicas. Siguiendo el orden de precedencia debemos resolver primero las operaciones relacionales, siempre de izquierda a derecha, y lo primero que tenemos por la izquierda es la operación relacional `-17 >= 20`.

```python
>>> -17 >= 20
False
```

El resultado de esta operación es `False`, puesto que el número `-17` no es mayor o igual que `20`. Sigamos con la siguiente operación relacional `3 != 0`.

```python
>>> 3 != 0
True
```

El resultado es `True` puesto que el número `3` es diferente del número `0`. Actualizamos la expresión:

```python
False and not True
```

Ahora nos queda una expresión únicamente lógica. Si seguimos las normas de precedencia debemos tener en cuenta primero el operador `not`, en este caso la operación es `not True`.

```python
>>> not True
False
```

Actualizamos la expresión:

```python
False and False
```

Finalmente calculamos esta operación lógica en la que hay una conjunción `and`.

```python
>>> False and False
False
```
