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

class PruebasMetodosCadenas(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('hola'.isupper())

    def test_split(self):
        s = 'Hola mundo!'
        self.assertEqual(s.split(' '), ['Hola', 'mundo!'])

if __name__ == '__main__':
    unittest.main()
