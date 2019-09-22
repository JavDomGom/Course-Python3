# Clases y objetos

Con todo lo que conocemos hasta ahora ya podemos crear bastantes programas. Sin embargo no dejan de ser instrucciones estructuradas. Esto significa que cuando queremos solucionar un problema tenemos que pensar de arriba a abajo, y lo único que nos da un poco de juego son las funciones, las listas y los diccionarios. Así era la programación en el pasado, bastante aburrida, con mucho código, mucha gestión de recursos y muy difícil de mantener. Hasta que poco a poco fue tomando forma un paradigma de programación conocido como Programación Orientada a Objetos (POO).

Este paradigma o modelo de solución de problemas resultó muy útil para satisfacer las necesidades de un mundo cada vez más tecnificado, en el que cada vez más y más sectores se estaban informatizando y era necesario crear una forma más sencilla de poder trasladar los problemas del mundo real a la programación. La mejora fue muy importante, ya que las tediosas estructuras no solo se podían replicar fácilmente en clases y objetos mucho mejor ordenados, si no que estos además permitían manejar sus propios atributos y funciones internas, llamadas métodos.

En esta nueva sección vamos a aprender cómo trabajar con objetos, definiendo y manejando nuestras propias clases, descubriendo la herencia y repasando algunos métodos nativos de las colecciones, haciéndolos si cabe aún más potentes.

## Programación estructurada Vs. POO

En este punto plantearemos un ccaso de estudio y trataremos de solucionarlo mediante programación estructurada y luego con programación orientada a objetos. Es importante ver la diferencia entre ambos paradigmas.

El caso de estudio será el siguiente: Nos piden crear un registro para manejar los clientes de una empresa, con su nombre, sus apellidos y su DNI. El programa debe permitirnos mostrar los datos de los clientes o eliminarlos a partir de su DNI. En un primer momento podremos pensar que lo más razonable es trabajar con ficheros o bases de datos, pero todavía no hemos llegado a esa parte, de momento trabajaremos con almacenamiento de información en memoria, es decir durante la ejecución del programa.

Lo primero que debemos hacer es plasmar de alguna manera la información de los clientes, y para ello deberemos usar una combinación de dos colecciones como son las listas y los diccionarios. Para comenzar a trabajar en esta aplicación vamos a crear un archivo nuevo llamado `clientes.py` y empezaremos por crear una variable llamada `clientes` que tendrá por valor una lista. Esta lista contendrá dos elementos, y estos elementos serán diccionarios con tres indices, `nombre`, `apellidos` y `dni`. Los cumplimentemos con unos datos de ejemplo. Finalmente imprimimos la lista de diccionarios `clientes` para ver que se han registrado correctamente:

```python
clientes = [
    {'nombre': 'Richard', 'apellidos': 'Stallman', 'dni': '01234567A'},
    {'nombre': 'Aaron', 'apellidos': 'Swartz', 'dni': '98765432Z'}
]

print(clientes)
```
```bash
python3 clientes.py
[{'nombre': 'Richard', 'apellidos': 'Stallman', 'dni': '01234567A'},
{'nombre': 'Aaron', 'apellidos': 'Swartz', 'dni': '98765432Z'}]
```

Ahora que tenemos un par de clientes, la primera funcionalidad que debemos implementar en nuestro programa es la de mostrar la información de un cliente en base a su DNI. Para ello, primero borraremos el `print()` que habíamos puesto para mostrar el contenido de la lista `clientes` y a continuación crearemos una función que necesite recibir como argumentos la lista de clientes y el DNI del cliente a localizar dentro de la lista, por ejemplo:

```python
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if dni == c['dni']:
            print('{} {}'.format(c['nombre'], c['apellidos']))
            return  # Si se encuentra el cliente se sale de la iteración.

    print('Clente no encontrado.')
```

Ahora solo queda invocar la función de la siguiente manera y ejecutar el programa:

```python
mostrar_cliente(clientes, '01234567A')
```
```bash
python3 clientes.py
Richard Stallman
```

Muestra el nombre y apellidos del cliente que coincide con el DNI `01234567A`. Vamos a modificar el DNI que estamos poniendo a la hora de invocar la función `mostrar_cliente` poniendo un DNI que no exista en nuestra lista `clientes`, por ejemplo:

```python
mostrar_cliente(clientes, '00000000B')
```
```bash
python3 clientes.py
Clente no encontrado.
```

El bucle `for` completó todas las iteraciones buscando algún cliente con el DNI `00000000B` y como no se encontró ningun resultado se muestra por pantalla el mensaje correspondiente. Se puede decir que ya tenemos una aplicación con una funcionalidad o método muy rudimentario que se encarga de buscar clientes dentro de una lista. Hagamos una nueva funcionalidad que se encargue de borrar un cliente de la lista, para ello haremos una nueva función llamada `borrar_cliente` que reciba también dos argumentos, la lista de clientes y el DNI del cliente que se quiere borrar, por ejemplo:

```python
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if dni == c['dni']:
            del clientes[i]
            print(str(c), '--> Borrado')
            return   # Si se encuentra el cliente se sale de la iteración.

    print('Clente no encontrado.')
```

En esta ocasión recorreremos la lista con un bucle `for` en el que iremos registrando no solo cada elmento iterable mediante la variable local `c` si no también el índice que ocupa en la lista mediante la variable `i` que obtendremos al recorrer la lista dentro del método `enumerate()` de Python. Por cada iteración se comprueba si el DNI proporcionado como argumento coincide con el DNI de cada cliente en cada iteración. Si coinciden se ejecutará la sentencia `del`, que eliminará ese elemento (diccionario) de l a lista de clientes, imrpmirá un mensaje e interrumpirá la iteración.

Después de la definición de la función `borrar_cliente` vamos a añadir un `print()` para imprimir la lista de clientes antes de eliminar uno, a continuación una llamada a la función `borrar_cliente` con un DNI de uno de los clientes, y finalmente otro `print()` para imprimir la lista de clientes de nuevo y poder ver que se ha borrado el cliente que coincidía con el DNI:

```python
print(clientes)
borrar_cliente(clientes, '01234567A')
print(clientes)
```

Al ejecutar el programa tendremos el siguiente resultado:

```bash
python3 clientes.py
[{'nombre': 'Richard', 'apellidos': 'Stallman', 'dni': '01234567A'},
{'nombre': 'Aaron', 'apellidos': 'Swartz', 'dni': '98765432Z'}]
{'nombre': 'Richard', 'apellidos': 'Stallman', 'dni': '01234567A'} --> Borrado
[{'nombre': 'Aaron', 'apellidos': 'Swartz', 'dni': '98765432Z'}]
```

Ya tendríamos un programa con dos funcionalidades, las de mostrar y eliminar clientes de una lista. Pero podríamos crear más funcionalidades como la de editar los datos de un cliente o añadir más campos a los diccionarios. Con esto nos basta para ver un ejemplo de cómo sería un programa de gestión de clientes hecho con programación tradicional y estructurada, y funciona bien, atiende a las necesidades del programa tal y como nos lo han pedido. Lo malo de este tipo de programación es que a la larga se hace muy confuso porque se generaría mucho código y esto es dificil de mantener. Además, como hemos visto, tendríamos que estar moviendo constantemente la lista de clientes de un lado a otro para poder manejarla y ejecutar acciones sobre ella, esto no es muy práctico.

Vamos a ver la misma implementación de este programa utilizando el paradigma de la programación orientada a objetos. Vamos a crear un archivo nuevo llamado `clientes_poo.py` con el siguiente código:

```python
class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print('Cliente no encontrado')

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), '--> Borrado')
                return
        print('Cliente no encontrado')
```

No es necesario que se comprenda en este momento todo el contenido del código, se irá viendo poco a poco e iremos haciendo uso de cada parte con la correspondiente explicación.

Aquí podemos encontrar un objeto nuevo llamado clase, se identifica con la plalabra reservada `class` seguida del nombre que tendrá la clase. Los nombres de las clases se suelen escribir con la primera letra en mayúscula. en este caso hemos creado dos clases, una `Cliente` y otra `Empresa`. Ambas clases tienen en su cuerpo una función interna llamada `__init__()`. Se trata de una función especial, es el contructor de la clase, es decir, donde se va a otorgar valores a los atributos de la clase. En el caso de la clase `Cliente` existen tres atributos, que son el `dni`, `nombre` y `apellidos`. Para indicar que son atributos de la clase deben llevar el prefijo `self.`. En el caso de la clase `Empresa` solo hay un atributo `clientes`. Si este no se especifica tendrá como valor por defecto una lista vacía.

En lugar de trabajar con funciones, como era el caso de la programación estructurada, aquí cambia la sintaxis, cada clase tendrá sus propios métodos. Lo primero que tenemos que hacer a continuación del código anterior es crear un cliente en memoria, esto se realiza de la siguiente manera:

```python
javier = Cliente(nombre='Javier', apellidos='Dominguez', dni='00000000A')
```

Hemos creado una variable llamada `javier` que tiene como valor un objeto o instancia de la clase `Cliente`, y además se le ha indicado que el atributo `nombre` debe tener por valor `Javier`, el atributo `apellidos` el valor `Dominguez` y el atributo `dni` el valor `00000000A`.

Vamos a crear otro cliente pero esta vez sin especificar el nombre de los atributos, solo respetando el orden en el que la clase `Cliente` espera recibir los argumentos, que son `dni`, `nombre` y `apellidos`:

```python
beatriz = Cliente('11111111B', 'Beatriz', 'Gimenez')
```

Con estas dos nuevas líneas hebremos creado dos instancias u objetos de la clase `Cliente`, cada una con sus atributos personalizados.

Ahora vamos a crear una instacia u objeto de la clase `Empresa`, esta clase necesita recibir como argumento una lista, lo haremos de la siguiente manera:

```python
empresa = Empresa(clientes=[javier, beatriz])
```

Vamos a añadir una línea más para imprimir el atributo `clientes` de la instancia de la clase Empresa que hemos llamado `empresa`:

```python
print(empresa.clientes)
```

Si guardamos el contenido del programa y lo ejecutamos tendremos la siguente salida (los códigos hexadecimales que hacen referencia al la dirección de memoria usada pueden variar):

```bash
python3 clientes_poo.py
[<__main__.Cliente object at 0x7fad555e9940>,
<__main__.Cliente object at 0x7fad555e9978>]
```

Lo que se imprime por pantalla es el atributo `clientes` del objeto `empresa`, es decir, una lista de dos elementos de tipo `object`, son objetos de una clase, en este caso concreto de la clase `Cliente`. Pero de esta manera no podremos ver más que la dirección de memoria hexadecimal en la que fueron alojados sendos objetos, ¿cómo podríamos acceder a su atributos? Como por ejemplo el nombre, apellidos o el dni. La clase `Empresa` tiene un método llamado `mostrar_cliente` que recibe por parámetro el `dni` de un cliente.

Para hacer uso de un método de una clase debemos poner el nombre del objeto seguido de un punto (`.`) y el nombre del método con paréntesis y los valores que correspondand dentro de los paréntesis, por ejemplo:

```python
empresa.mostrar_cliente(dni='00000000A')
```

En este caso no hace falta meterlo dentro de la función `print()` ya que el propio método hace uso de la función `print()` para imprimir por pantalla los datos del cliente, véase un ejemplo de ejecución:

```bash
python3 clientes_poo.py
[<__main__.Cliente object at 0x7f3b32aaf9b0>,
<__main__.Cliente object at 0x7f3b32aaf9e8>]
Javier Dominguez
```

Ahora vamos a borrar un cliente, para ello escribiremos el nombre del objeto `empresa`, seguido de un punto y el nombre del método de esa clase que queremos invocar, en este caso el método `borrar_cliente()`, entre los paréntesis debemos especificar el DNI del cliente que queremos borrar. Y finalmente imprimimos el atributo `clientes` del objeto `emrpesas`, para que nos imprima la lista actual de clientes y poder verificar que ya no está más el cliente recien borrado:

```python
empresa.borrar_cliente(dni='11111111B')
print(empresa.clientes)
```
```bash
python3 clientes_poo.py
[<__main__.Cliente object at 0x7f3b32aaf9b0>,
<__main__.Cliente object at 0x7f3b32aaf9e8>]
Javier Dominguez
Beatriz Gimenez --> Borrado
[<__main__.Cliente object at 0x7f3b32aaf9b0>]
```

En este punto puede que no tengamos muy claro que está sucediendo por detrás durante la ejecución del programa, pero podemos notar una sintaxis más clara y auto explicativa que nos ayuda a comprender el programa. Tanto la empresa como los clientes tienen su propia clase con sus atributos y sus funciones. Podemos rellenar la lista de clientes de la empresa con objetos de la clase cliente, cada uno con sus propios atributos y podemos hacer que interaccionen unos objetos con otros entre clases. En resumen podríamos decir que la programación orientada a objetos se basa en determinar las entidades con nombres propios en lugar de crear estructuras y diccionarios para representar la información.

## Clases y objetos

En cualquier lenguaje de programación si hablamos de objetos es necesario hablar también de clases. De hecho sin clases no habría objetos, ya que las clases son los moldes de los objetos, en cierto modo como lo son un molde de galletas y las propias galletas. Para ver algunos ejemplos vamos a crear un nuevo archivo llamado `clases_y_objetos.py` y vamos a crear la siguiente clase llamada `Galleta` que no contendrá nada, es una clase vacía, para ello usamos la instrucción `pass`:

```python
class Galleta:
    pass
```

A continuación vamos a escribir estas dos líneas para crear dos objetos de esta clase:

```python
galleta_1 = Galleta()
galleta_2 = Galleta()
```

Se podría secir que hemos creado dos galletas `galleta_1` y `galleta_2` a partir del molde `Galleta`. Cada vez que creamos un objeto de una clase lo que estamos haciendo es instanciar un objeto. El concepto de instancia es muy importante, ya que hace referencia a algo que existe en la memoria del ordenador, pero solo mientras el programa se está ejecutando. Cuando elprograma finaliza toda esta información se libera de la memoria y desaparece. es lo contrario a una base de datos, en cuyo caso la información permanecerá almacenada en la base de datos e incluso si el programa finaliza, es lo que se denomina como persistencia de datos. Hablaremos de ello más adelante.

Podemos saber la clase de un objeto gracias a la función integrada `type()` a la que debemos pasarle un objeto como argumento, por ejemplo

```python
print(type(galleta_1))
```
```bash
python3 clases_y_objetos.py
<class '__main__.Galleta'>
```

Como podemos ver, a través de la función integrada `type()` podemos acceder a la información que nos dice de qué tipo es este objeto, y en este caos nos indica que se trata de un objeto de la clase `Galleta`. Pero podríamos usar el método `type()` con otro tipo de objetos que ya conocemos, y siempre nos devolverá el tipo de dato u objeto que se trata, veamos varios ejemplos:

```python
print(type(10))
print(type(3.14))
print(type('Hola'))
print(type([]))
print(type({}))
print(type(True))

def hola():
    pass

print(type(hola))
```
```bash
python3 clases_y_objetos.py
<class '__main__.Galleta'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'dict'>
<class 'bool'>
<class 'function'>
```

Si nos fijamos en cada caso nos devuelve el nombre de la clase a la que pertenece, y es que en Python en realidad todo son objetos de diferentes clases. Cuando definimos el valor `10`, o el valor `'Hola'` en realidad estamos creando objetos de las clases `int` y `str`. esa es la razón de que algunas de las clases que manejamos en Python tengan sus propios métodos. Todas las clases en Python tienen unos método en común, pero algunas clases como las cadenas de carácteres, las listas o los diccionarios tienen su propios métodos que podremos utilizar para manipularlas de forma más cómoda. Todos eso métodos propios de estas clases vienen definidos en la propia definición de clase de cada tipo de dato en el lenguaje Python.

## Atributos y métodos de clase

Para estudiar este punto seguiremos con el ejemplo del molde de galletas y las galletas que salen de él, no todas serán iguales. Siguiendo con la metáfora, todas las galletas compartirán la misma forma y tamaño, pero pueden hacerse de diferentes colores, sabores o ingredientes. He ahí el que sus atributos tengan diferentes valores y que cada galleta sea única.

La gracia de la programación orientada a objetos es que los objetos puedan tener sus propios atributos, una especie de variables internas a las que nos podremos referir con un puntito después del nombre del objeto y a continuación el nombre del atributo. Estos atributos se pueden definir fuera de la clase y se crearían automáticamente solo para esa instancia. Para poder verlo vamos a crear un nuevo archivo llamado `galletas.py` con el siguiente código:

```python
class Galleta:
    pass

g = Galleta()
g.sabor = 'salada'
g.color = 'amarillo'

print('Esta galleta es de color {} y sabe {}'.format(g.color, g.sabor))
```
```bash
python3 galletas.py
Esta galleta es de color amarillo y sabe salada
```

Al objeto `g` de la clase `Galleta` acabamos de asignarle dos atributos que no tenía cuando fue creado. No es una manera muy recomendable de hacerlo, ya que si creamos un nuevo objeto de la clase `Galleta` este no tendría esos atributos por defecto y tendríamos que gestionar si queremos que todas las galletas los tengan o no, aunque tengan diferentes valores. Para ello es mejor definir los atributos en el cuerpo de la clase, de modo que todos los objetos creados de esta clase tendrán los mismos atributos, por ejemplo:

```python
class Galleta:
    sabor = 'salada'
    color = 'amarillo'

g1 = Galleta()
g2 = Galleta()

print('La galleta 1 es de color {} y sabe {}'.format(g1.color, g1.sabor))
print('La galleta 2 es de color {} y sabe {}'.format(g2.color, g2.sabor))
```
```bash
python3 galletas.py
La galleta 1 es de color amarillo y sabe salada
La galleta 2 es de color amarillo y sabe salada
```

Como podemos ver, no es necesario asignar atributos cada vez que se crea un objeto de la clase `Galleta`, ya se definen en la propia clase. Lo malo de este método es que todas tendrán los mismos valores por defecto, por lo que si saldrían todas las galletas iguales.

Para que cada objeto tenga sus propios valores de atributos lo mejor es definirlos en el momento que se crea el objeto, para ello es necesario conocer dos conceptos nuevos de las clases, uno es el método especial llamdo `__init__()`, y el otro es la palabra reservada `self`. Vamos a desarrollar de nuevo la clase introduciendo estos dos nuevos conceptos.

```python
class Galleta:

    def __init__(self, sabor, color):        
        self.sabor = sabor
        self.color = color
```

El método especial `__init()__` también se conoce como constructor de la clase, es el método que se va a ejecutar siempre que instanciemos un objeto de la misma, sin que sea necesario invocarlo. La palabra reservada `self` la tienen todos los métodos de todas las clases y hace referencia al propio objeto y sirve para diferencias entre el ámbito de la clase y el de un método. Es un requisito implícito en todos los métodos ya que por defecto al llamar a un método se pasa automáticamente al propio objeto. Esto ocurre de forma transparente en la llamada, pero es obligatorio en la definición.

Ahora debemos crear dos objetos de la clase `Galleta`, pero esta vez deberemos indicar entre paréntesis los atributos que espera recibir obligatoriamente el constructor de la clase, que en este caso son `sabor` y `color`.

```python
g1 = Galleta('salada', 'amarilla')
g2 = Galleta('dulce', 'verde')
```

Añadimos dos líneas para imprimir un mensaje por pantalla donde se puedan ver los atributos de las instancias `g1` y `g2`, para acceder al dato escribiremos a continuación del nombre del objeto un punto y el nombre del atributo de ese objeto.

```python
print('La galleta 1 es de color {} y sabe {}'.format(g1.color, g1.sabor))
print('La galleta 2 es de color {} y sabe {}'.format(g2.color, g2.sabor))
```

Al ejecutar el programa obtendremos la siguiente salida:

```bash
python galletas.py
La galleta 1 es de color amarilla y sabe salada
La galleta 2 es de color verde y sabe dulce
```

Vamos a crear nuestros propios métodos de clase, por ejemplo un método llamado `chocolatear()` y otro método que se llame `tiene_chocolate()` con el siguiente código:

```python
class Galleta:

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        self.chocolate = False

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if self.chocolate:
            print('Si tiene chocolate')
        else:
            print('No tiene chocolate')
```

Se ha tenido que añadir un nuevo atributo llamado `chocolate` al constructor con un valor por defecto `False`. Si en algún momento del programa se invoca al método `chocolatear()` el valor del atributo `chocolate` se cambiará a `True`, si no permanecerá el valor por defecto. Y si se invoca al método `tiene_chocolate()` se comprobará el valor del atributo `chocolate` antes de imprimir un mensaje por pantalla diciendo si la galleta tiene o no tiene chocolate. Veamos un ejemplo de las líneas de código con algunas invocaciones y el resultaod de su ejecución:

```python
g1 = Galleta('salada', 'amarilla')
g2 = Galleta('dulce', 'verde')

print('\nEstado actual de las galletas')
g1.tiene_chocolate()
g2.tiene_chocolate()

print('\nAñado chocolate a la primera galleta ...')
g1.chocolatear()

print('\nEstado actual de las galletas')
g1.tiene_chocolate()
g2.tiene_chocolate()
```
```bash
python galletas.py

Estado actual de las galletas
No tiene chocolate
No tiene chocolate

Añado chocolate a la primera galleta ...

Estado actual de las galletas
Si tiene chocolate
No tiene chocolate
```

Como se puede comprobar, ahora tenemos clases, objetos, atributos y métodos de clase que nos sirven para poder tener un control sobre el estado de las cosas de una manera mucho más sencilla.

## Métodos especiales

Aparte del método `__init__()` existen muchos otros métodos especiales en Python. Para poder ver algunos ejemplos vamos a crear un nuevo archivo llamado `peliculas.py` con el siguiente código en el que volveremos a ver el constructor de la clase con tres atributos, `titulo`, `duracion` y `lanzamiento`.

```python
class Pelicula:

    # Contructor de clase.
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película {}'. format(self.titulo))
```

Ahora crearemos un objeto de esta clase pasándole como argumentos los valores que espera recibir el constructor para sus atributos:

```python
p = Pelicula('El padrino', 175, 1972)
```

Si ejecutamos el programa obtendremos la siguiente salida:

```bash
python peliculas.py
Se ha creado la película El padrino
```

Ya conocemos el método que hace de constructor de la clase, pero veamos otro método especial que hace de destructor, es un método llamado `__del__()` y únicamente se ejecutará cuando se borre una instancia.

```python
    # Destructor de la clase
    def __del__(self):
        print('Se está borrando la película {}'.format(self.titulo))
```

Ahora creamos el objeto `p` de la clase `Pelicula` y a continuación borramos el objeto mediante el método integrado `del()`.

```python
p = Pelicula('El padrino', 175, 1972)

del(p)
```

Al ejecutar el programa obtendremos la siguiente salida por pantalla.

```bash
python peliculas.py
Se ha creado la película El padrino
Se está borrando la película El padrino
```

Otro método especial es el método llamado `__str__()` que serivirá para aquellas ocasiones en las que se pasa el nombre del objeto por la función integrada `str()` de Python, en cuyo caso ya no se mostrará una cadena con la dirección de memoria en la que está almacenado el objeto, si no un mensaje personalizado. Por ejemplo:

```python
    # Redefinimos el método string
    def __str__(self):
        return '{} lanzada en {} con una duración de {} minutos'.format(self.titulo, self.lanzamiento, self.duracion)
```

Ahora eliminamos la línea que escribimos anteriormente con la función integrada `del()` y ponemos una línea nueva invocando a la función integrada `str()` a la que le pasaremos el nombre de nuestro objeto `p`, por ejemplo:

```python
p = Pelicula('El padrino', 175, 1972)

print(str(p))
```

Al ejecutar el programa obtendremos la siguiente salida por pantalla.

```bash
python peliculas.py
Se ha creado la película El padrino
El padrino lanzada en 1972 con una duración de 175 minutos
Se está borrando la película El padrino
```

Si nos fijamos bien, se imprimern tres mensajes, el primero es el que se ejecuta en el contructor, el segundo es nuestra instrucción de imprimir el objeto en formato *string* y el tercero es el que se ejecuta al destruír el objeto. ¿Por qué se ejecuta el tercer mensaje? Porque aunque no indiquemos en el código del programa que queremos destruír el objeto, este se destruirá al finalizar el programa, por lo tanto siempre se ejecutará. Existen muchos otros métodos especiales, pero estos tres son los más utilizados.

## Objetos dentro de objetos

En Python podemos crear objetos que tengan  atributos cuyo valor pueden ser objetos de otras clases. Al principio de esta sección hemos visto un ejemplo en el que usábamos la clase `Cliente` y la clase `Empresa`. En ese ejemplo el objeto de la clase `Empresa` contenía una lista de objetos de la clase `Cliente`. Ahora vamos a hacer un catálogo para poder manejar las películas del ejemplo anterior. Modifiquemos ligeramente la clase `Pelicula` que teníamos definida en el archivo `peliculas.py` del punto anterior. Eliminemos el método especial destructor y cambiemos el mensaje que devuelve el método especial `__str__()`, por ejemplo:

```python
class Pelicula:

    # Contructor de clase.
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película {}'.format(self.titulo))

    # Redefinimos el método string
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
```

Hagamos a continuación una nueva clase llamada `Catalogo`, esta clase tendrá un atributo llamado `peliculas` y tendrá por valor una lista vacía. Además tendrá un método constructor que inicializa la lista de películas vacía si no se le especifica ninguna lista o con una ya existente si se especificara como argumento a la hora de instanciar el objeto de la clase `Catalogo`. También tendrá dos métodos, el método `agregar()` que simplemente hace un `append` a la lista `peliculas` de la película que se le pase como argumento, y el método `mostrar()`, que simplemente hace un `print()` del objeto película.

```python
class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)
```

Ahora vamos a crear una película instanciando un objeto de la clase `Pelicula`, para ello añadiremos a nuestro código la siguiente línea:

```python
p = Pelicula('El padrino', 175, 1972)
```

Además crearemos una instancia de la clase `Catalogo` pasándole como argumento una lista con nuestra películ `p` anteriormente creada:

```python
c = Catalogo([p1])
```

Esta es una manera de crear una instancia u objeto de la clase `Catalogo` y meter una instancia u objeto de la clase `Película` dentro. Pero también podemos hacerlo de una forma en la que no sea necesario crear la instancia previamente, si no directamente, por ejemplo, vamos a añadir una segunda película al catálogo `c` invocando al método `agregar()` de nuestro catálogo:

```python
c.agregar(Pelicula('El padrino II', 202, 1974))
```

Finalmente vamos invocar al método `mostrar()` de la clase `Catalogo` y ejecutaremos el programa para ver que ha registrado correctamente las dos películas.

```python
c.mostrar()
```
```bash
python peliculas.py
Se ha creado la película El padrino
Se ha creado la película El padrino II
El padrino (1972)
El padrino II (1974)
```

Podemos mejorar nuestro programa añadiendo métodos adicionales a la clase `Catalogo` por ejemplo para borrar películas o modificar las que ya existen.

## Encapsulación de atributos

Hasta ahora hemos visto cómo en Python se puede acceder a los atributos y métodos de una clase de una manera muy sencilla. Esto es por que tal y como los hemos visto tienen un acceso público, pero en algunas ocasiones podría interesarnos que no fuera así, y que estos no se puedan ejecutar desde fuera, en cuyo caso tendrían un acceso privado, que permanezcan encapsulados.

La encapsulación es una funcionalidad que tienen muchos lenguajes de programación para impedir acceso externo a atributos y métodos. Pero Python no ofrece esta funcionalidad de base, aún así, se puede simular un comportamiento parecido precediendo el nombre de estos atributos o métodos con dos guiones bajos (__). Para poder ver algun ejemplo vamos a crear un nuevo archivo llamado `encapsulacion.py` en el que vamos a crear una clase `Ejemplo` con un atributo privado llamado `__atributo_privado` y un método privado llamado `__metodo_privado()`:

```python
class Ejemplo:
    __atributo_privado = 'Soy un atributo inalcanzable desde fuera.'

    def __metodo_privado(self):
        print('Soy un método inalcanzable desde fuera.')
```

Ahora vamos a crear una instancia de esta clase y vamos a intentar acceder a su atributo `__atributo_privado` desde fuera:

```python
print(e.__atributo_privado)
```

Si ejecutamos el programa ahora obtendremos el siguiente error:

```bash
python3 encapsulacion.py
Traceback (most recent call last):
  File "encapsulacion.py", line 9, in <module>
    print(e.__atributo_privado)
AttributeError: 'Ejemplo' object has no attribute '__atributo_privado'
```

El error indica que no existe el atributo `__atributo_privado`, pero en realidad no es así, si existe, solo que solo se puede invocar o utilizar dentro de la clase, no desde un objeto ya instanciado, es decir, desde fuera. Borremos esta última línea en la que invocábamos desde fuera al atributo y probemos ahora a invocar al método `__metodo_privado()` desde fuera también:

```python
e.__metodo_privado()
```

El ejecutarlo obtenemos este otro error:

```bash
encapsulacion.py
Traceback (most recent call last):
  File "01_introduccion/01_10_src/encapsulacion.py", line 9, in <module>
    e.__metodo_privado()
AttributeError: 'Ejemplo' object has no attribute '__metodo_privado'
```

El error es del mismo tipo, indica que no existe el método `__metodo_privado()`, pero si existe, solo que es privado y también es solo accesible desde dentro de la clase.

Para poder hacer uso de los atributos y métodos privados desde fuera tendremos que crear un nuevo método público que haga de puente y que sea él el que tiene acceso a los elementos privados desde dentro de la clase, por ejemplo:

```python
def mostrar_atributo(self):
        return self.__atributo_privado
```

Eliminamos la anterior línea en la que intentábamos acceder al atributo o el método privado y escribimos la siguiente línea en la que llamamos al método público `mostrar_atributo()`:

```python
print(e.mostrar_atributo())
```

Si ejecutamos de nuevo el programa obtendremos el valor del atributo privado correctamente:

```bash
python3 encapsulacion.py
Soy un atributo inalcanzable desde fuera.
```

Aplicando la misma técnica al método podremos acceder también al método privado creando una nuevo método público `mostrar_metodo()` que haga de puente, por ejemplo:

```python
def mostrar_metodo(self):
        return self.__metodo_privado()
```

Ahora invocamos a este nuevo método público mediante la siguiente línea:

```python
e.mostrar_metodo()
```

Al ejecutar el programa de nuevo obtendremos la información del método privado `__metodo_privado()` pasando por el método público `mostrar_metodo()`:

```bash
python3 encapsulacion.py
Soy un método inalcanzable desde fuera.
```