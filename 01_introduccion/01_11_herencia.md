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

Ahora crearemos una instancia de la clase `Adorno`, automáticamente heredará todos los atributos y métodos de la clase madre `Producto`, veamos algun ejemplo:

```python
a = Adorno('00000', 'Jarrón', 15.50, 'Jarrón de porcelana con dibujos')

print(a)
```
```bash
python3 producto.py
        REFERENCIA	00000
        NOMBRE		Jarrón
        PVP		15.5
        DESCRIPCIÓN	Jarrón de porcelana con dibujos
```
