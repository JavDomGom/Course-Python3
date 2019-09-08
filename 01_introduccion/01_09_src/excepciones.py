try:
        a = float(input('Introduce un número: '))
        b = 3

        print('{}/{} = {}'.format(b, a, b/a))
except TypeError:
        print('No se puede dividir una cadena de texto entre un número.')
except ValueError:
        print('Debes introducir un número.')
except ZeroDivisionError:
        print('No se puede dividir por cero.')
except Exception as e:
        print(type(e).__name__)
