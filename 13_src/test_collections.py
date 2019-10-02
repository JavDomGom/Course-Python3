from collections import OrderedDict

d1 = {'perro': 'dog', 'gato': 'cat'}
d2 = {'gato': 'cat', 'perro': 'dog'}

print(d1 == d2)     # True
print(OrderedDict(d1) == OrderedDict(d2))   # False

