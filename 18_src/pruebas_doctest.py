def suma(a, b):
    '''
    La función suma(a, b) recibe dos parámetros a y b.
    Devuelve la suma de ambos.

    >>> suma(5, 10)
    15

    >>> suma(0, 0)
    1

    >>> suma(-5, 7)
    2

    '''
    return a+b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
