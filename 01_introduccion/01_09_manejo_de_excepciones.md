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

En este caso hemos eliminado el cierra de paréntesis a la hora de usar la función integrada `print()`, lo que ha provocado el correspondiente error de sintáxis.

```python

```
```bash
python3 
```



```python

```
```bash
python3 
```



```python

```
```bash
python3 
```