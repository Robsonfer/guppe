"""
Módulo Collections - Deque

Podemos dizer que o Deque é uma lista de alta performance.

Documentação: https://docs.python.org/3/library/collections.html#collections.deque
"""

# Fazendo o import:
from collections import deque

# Criando deques:
deq = deque('geek')
print(deq)

# Adicionando elementos no final do deque:
deq.append('y')
print(deq)

# Adicionando elementos no início do deque:
deq.appendleft('k')
print(deq)

# Removendo o último elemento do deque:
print(deq.pop())
print(deq)
# Usando o print no deq.pop(), podemos ver que ele retorna o elemento removido, mas podemos remover diretamente.

# Removendo o primeiro elemento do deque:
print(deq.popleft())
print(deq)
# Da mesma forma que o anteior, podemos ver que ele também retorna o item removido.
