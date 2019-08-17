# Colecciones

En Python, además de las listas también tenemos un tipo especial de dato llamado colecciones, y a que a su vez se divide en varias estructuras de datos que veremos en detalle en esta sección:

- Tuplas
- Conjuntos
- Diccionarios

## Tuplas
Las tuplas son unas colecciones parecidas a las listas, con la diferencia de que las tuplas son inmutables. Se suelen utilizar para asegurarnos de que determinados datos no se puedan modificar. Python utiliza tuplas en alguna de sus funciones para devolver resultados inmutables. La manera de definir un dato de tipo tupla es parecido a las listas, solo que en vez de usar corchetes `[]` se utilizan paréntesis `()`. Dentro de los paréntesis se incluyen los elementos como si fueran una lista. Para poder ver un ejemplo práctico vamos a crear un archivo llamado `tupla.py` y dentro vamos a incluír el siguiente código:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla)
```
Si ejecutamos el programa obtendremos el siguiente resultado:

```bash
python3 tupla.py
(100, 'Hola', [1, 2, 3], 3.14)
```

Las tuplas, al igual que las listas aceptan indexación y **slicing**. Por ejemplo, podremos consultar el primer elemento con el índice `[0]` o el último elemento de la tupla con el índice `[-1]`:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[0])
print(tupla[-1])
```

Al ejecutarlo obtendremos el siguiente resultado:

```bash
python3 tupla.py
100
3.14
```

Y también podremos imprimir todos los elementos desde el tercero hasta el final con el **slicing** `[2:]`:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[2:])
```

```bash
python3 tupla.py
([1, 2, 3], 3.14)
```

En este caso, uno de los elementos de la tupla es una lista, también podremos acceder a uno de los elementos internos de esa lista tal y como lo hacíamos cuando teníamos listas dentro de listas, con dobles índices, por ejemplo:

```python
tupla = (100, 'Hola', [1, 2, 3], 3.14)

print(tupla[2][1])
```

```bash
python3 tupla.py
2
```
