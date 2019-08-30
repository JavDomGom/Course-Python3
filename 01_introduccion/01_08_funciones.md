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