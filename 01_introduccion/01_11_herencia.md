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