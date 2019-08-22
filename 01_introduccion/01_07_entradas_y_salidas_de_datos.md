# Entradas y salidas de datos

En esta sección vamos a aprender acerca de la entrada y salida de datos en un programa Python, entendiendo por entrada la forma de capturar información desde fuera del programa y por salida la forma de exponer los datos o la información.

La primera forma de capturar información en nuestro programa Python ya la conocemos, es mediante la función `input()`, que toma los datos que el usuario introduce a través del teclado y lo hace como cadenas de texto o **strings**, pero tambien podemos transformar los datos introducidos para poder trabajar con ellos o manipularlos.

## Entradas

Para trabajar la entrada de datos vamos a crear un nuevo archivo llamado `entrada.py` y vamos a ir añadiendo código para su estudio. Por ejemplo, vamos a hacer un pequeño programa que pida al usuario introducir un número decimal (`float`), y para ello vamos a usar en primera instancia la función `input()`. Una vez que el usuario introduzca un número decimal este se imprimirá por pantalla:

```python
decimal = input('Introduce un número decimal: ')
print(decimal)
```
```bash
python3 entrada.py
Introduce un número decimal: 3.14
3.14
```

Aparentemente lo ha hecho todo correctamente, y así es, ha impreso por pantalla el valor que hemos introducido. Pero es posible que no sea el tipo de dato que queremos para luego trabajar con él, en este caso el tipo de dato que se muestra es de tipo cadena de carácteres o **string**. Podemos ver el tipo de dato que tenemos almacenado en la variable `decimal` de la siguiente manera:

```python
print(type(decimal))
```
```bash
python3 entrada.py
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
python3 entrada.py
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
python3 entrada.py
Introduce un valor cualquiera: abcd
Introduce un valor cualquiera: Hola
Introduce un valor cualquiera: 1234
['abcd', 'Hola', '1234']
```

Como se puede ver, hemos introducido varios valores dentro de una lista, hemos completado una colección introduciendo datos por teclado varias veces.

Esta manera de introducir datos no es la más común, solo cuando se estan ejecutando programas o scripts Python en una terminal, normalmente los datos se suelen obtener mediante la lectura de datos en ficheros o bases de datos o mediante interfactes gráficas en los que los usuarios completan formularios de datos.