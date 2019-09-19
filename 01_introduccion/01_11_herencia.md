# Herencia

Una de las funcionalidades clásicas de la Programación Orienteda a Objetos (POO) es la Herencia, la capacidad que tiene una clase de heredar atributos y métodos de otra, además de agregar los suyos propios o modificar los heredados. De ahí la relación de *Clases madre* y *Clases hijas*, donde a las primeras se las suele llamar **Superclases** y a la segundas **Subclases**. En esta sección vamos a aprender cómo desarrollar la herencia de clases, cómo se gestionan los atributos y métodos heredados, y otras peculiaridades.

Para verlo en un ejemplo vamos a crear una aplicación para la gestión de una tienda en la que se venderán diferentes productos. Nuestro programa estará compuesta por varios archivos con código fuente Python en el que vamos a ir añadiendo diferente código. Empecemos por crear un archivo llamado `producto.py`, aquí definiremos la clase `Producto` donde definiremos todos los campos posibles relativos a los típos de producto que podamos crear, tales como alimentos o libros.

```python
class Producto:

    def __init__(self, referencia, tipo, nombre, pvp, descripcion, productor=None, distribuidor=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.autor = autor
```

Este sería un buen comienzo para crear productos, de momento una clase llamada `Producto` que solo tiene un método constructor `__init__()` en el que se definirá el valor de unos atributos obligatorios, como `referencia`, `tipo`, `nombre`, `pvp` y `descripcion`, y luego otros atributos opcionales, como `productor`, `distribuidor` y `autor`.

Los atributos obligatorios son aquellos que tendremos que especificar siempre que definamos una instancia u objetos de la clase, en este caso porque son todos los atributos que todos los productos tendrán en común. Sin embargo los opcionales podremos especificarlos o no, dependerá del tipo de producto que queremos instanciar. En los casos en los que no especifiquemos estos atributos opcionales se le asignará un valor por defecto `None`.

Vamos a crear un producto instancioando un objeto de esta clase, por ejemplo:

```python
adorno = Producto('000A', 'Adorno', 'Jarrón', 15, 'Jarrón de porcelana con dibujos')
```

Si queremos imprimir por pantalla el tipo y la descripción del adorno podremos hacerlo llamando a los atributos `tipo` y `descripcion` de la siguiente manera:

```python
print(adorno.tipo)
print(adorno.descripcion)
```
```bash
python3 producto.py
Adorno
Jarrón de porcelana con dibujos
```

De momento tenemos algo que podría servirnos, pero no tiene mucho sentido mezclar tantos atributos tan diferentes como `isbn` y `productor`. Además, al crear un producto de cualquier tipo tendremos que recorrer y establecer valor a todos los atributos. Esto es poco eficiente, por lo que necesitaremos establecer de alguna manera una jerarquía y poner orden. La herencia de clases nos puede servir en estos casos, para ello tendremos que dividir el código en una Superclase y diferentes Subclases. En una Superclase agruparemos todos los atributos que sean comunes para todos los productos, por ejemplo en la clase `Producto`:

```python
class Producto:

    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
```

A esta clase `Producto` podemos añadirle el método especial `__str__()` para que devuelva una descripción del producto, por ejemplo:

```python
    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)
```

Luego tendríamos que hacer tres Subclases, por ejemplo `Adorno`, `Libro` y `Alimento`, y cada clase con su atributos, pero inicialmente hagamos las calses sin contenido, solo con la palabra reservada `pass`. Empecemos por la sublcase `Adorno`. Para indicarle que es una sublcase de la clase `Producto` tenemos que añadirle el nombre de la clase madre entre paréntesis:

```python
class Adorno(Producto):
    pass
```

Ahora crearemos un objeto o instancia de la clase `Adorno`, automáticamente heredará todos los atributos y métodos de la clase madre `Producto`, veamos algun ejemplo:

```python
ad = Adorno('00000', 'Jarrón', 15.50, 'Jarrón de porcelana con dibujos')

print(ad)
```
```bash
python3 producto.py
        REFERENCIA	    00000
        NOMBRE		    Jarrón
        PVP		        15.5
        DESCRIPCIÓN     Jarrón de porcelana con dibujos
```

Vamos a crear la clase `Alimento`, esta clase a diferencia de la anterior si tiene un par de atributos propios, estos los definiremos sin constructor. Al estar fuera de un método de clase no es necesario indicar el prefijo `self`. Los definiremos con valores vacíos de la siguiente manera:

```python
class Alimento(Producto):
    productor = ''
    distribuidor = ''
```

Creamos una instancia de la clase `Alimento` pasándole solo los argumentos obligatorios:

```python
al = Alimento('00001', 'Aceite de Oliva', 5, 'Botella de aceite de oliva virgen extra')
```

Añadimos valor a sus dos atributos e imprimimos el objeto:

```python
al.productor = 'La aceitera'
al.distribuidor = 'Distribuciones S.A.'

print(al)
```
```bash
python3 producto.py
        REFERENCIA	    00001
        NOMBRE		    Aceite de Oliva
        PVP		        5
        DESCRIPCIÓN     Botella de aceite de oliva virgen extra
```

Si nos fijamos bien se imprmien solo los datos que se indican en la función especial `__str__()` de la clase madre `Producto`, y este método especial no incluye los atributos propios de cada subclase. Para solucionar esto podremos redefinir el método especial `__str__()` en cada sublclase, por ejemplo en el caso de la subclase `Alimento` lo haríamos de la siguiente manera:

```python
    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)
```

Si ejecutamos el programa de nuevo veremos que el método especial `__str__()` de la subclase ha sobreescrito el de la superclase:

```bash
python3 producto.py
        REFERENCIA	    00001
        NOMBRE		    Aceite de Oliva
        PVP		        5
        DESCRIPCIÓN	    Botella de aceite de oliva virgen extra
        PRODUCTOR	    La aceitera
        DISTRIBUIDOR	Distribuciones S.A.
```

Por último vamos a crear la subclase `Libro` que herede de la superclase `Producto`. La vamos a crear basándonos en la clase anterior, con sus propios atributos y su propio método especial `__str__()`:

```python
class Libro(Producto):
    isbn = ''
    autor = ''

    def __str__(self):
        return """\
        REFERENCIA\t{}
        NOMBRE\t\t{}
        PVP\t\t{}
        DESCRIPCIÓN\t{}
        PRODUCTOR\t{}
        DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)
```

Creamos un nuevo objeto o instancia de la subclase `Libro`, añadimos valor a sus dos atributos propios e imprimimos el objeto:

```python
li = Libro('00002', 'El enemigo conoce el sistema', 17.90, 'Libro sobre redes de hiper vigilancia')
li.isbn = '8417636390'
li.autor = 'Marta Peirano'
```
```bash
python3 producto.py
        REFERENCIA	    00002
        NOMBRE		    El enemigo conoce el sistema
        PVP		        17.9
        DESCRIPCIÓN	    Libro sobre redes de hiper vigilancia
        PRODUCTOR	    8417636390
        DISTRIBUIDOR	Marta Peirano
```

## Clases heredadas y poliformismo

En el punto anterior hemos creado una superclase y tres subclases, de modo que ahora disponemos de una jerarquía que nos permite poder trabajar con cierta comodidad en nuestra tienda de productos. Sin embargo, para poder manejar los productos necesitaremos agruparlos de alguna manera, por ejemplo en luna colección como una lista de productos. Podríamos añadir todos los productos a una lista sin importar que sean de subclases distintas, por ejemplo podríamos crear la lista `productos` y añadir dentro los productos de tipo `Alimento` y `Libro` creados anteriormente `al` y `li`:

```python
productos = [al, li]
```

A esta lista podremos añadirle otros objetos que vayamos creando o que ya hemos creado, por ejemplo el objeto de tipo `Adorno` que creamos al principio:

```python
productos.append(ad)
```

Si imprmimimos la lista obtendremos la siguiente salida por pantalla:

```bash
python3 producto.py
[<__main__.Alimento object at 0x10b341eb8>,
 <__main__.Libro object at 0x10b341ef0>,
 <__main__.Adorno object at 0x10b341e80>]
```

Ahora podremos recorrer esta lista cómodamente con un bucle `for`, por ejemplo:

```python
for p in productos:
    print(p, '\n')
```

Se ha añadido un salto de línea (`\n`) para tener un espacio entre productos y que se pueda visualizar un poco mejor:

```bash
python3 producto.py
        REFERENCIA	    00001
        NOMBRE		    Aceite de Oliva
        PVP		        5
        DESCRIPCIÓN	    Botella de aceite de oliva virgen extra
        PRODUCTOR	    La aceitera
        DISTRIBUIDOR	Distribuciones S.A.

        REFERENCIA	    00002
        NOMBRE		    El enemigo conoce el sistema
        PVP		        17.9
        DESCRIPCIÓN	    Libro sobre redes de hiper vigilancia
        PRODUCTOR	    8417636390
        DISTRIBUIDOR	Marta Peirano

        REFERENCIA	    00000
        NOMBRE		    Jarrón
        PVP		        15.5
        DESCRIPCIÓN	    Jarrón de porcelana con dibujos
```

Podemos modificar la manera de imprimir los datos en el bucle `for` de la siguiente manera para que solo imprima algunos atributos comunes de los productos:

```python
for p in productos:
    print(p.referencia, p.nombre, '\n')
```
```bash
python3 producto.py
00001 Aceite de Oliva

00002 El enemigo conoce el sistema

00000 Jarrón
```