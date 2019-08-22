from collections import deque

cola = deque()
print(cola)

cola.append('Javier')
print(cola)

cola.append('Bob')
cola.append('Alice')
print(cola)

cola.popleft()
print(cola)
