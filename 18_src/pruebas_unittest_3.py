import unittest

'''
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isistance(a, b)
'''

def doblar(a): return a*2

class PruebaTestFixture(unittest.TestCase):

    def setUp(self):
        print('Preparando el contexto')
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print('Realizando una prueba')
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 11])

    def tearDown(self):
        print('Destruyendo el contexto')
        del(self.numeros)

if __name__ == '__main__':
    unittest.main()
