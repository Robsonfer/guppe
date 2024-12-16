"""
Aula 176 - Otimizações
"""

import collections
from timeit import timeit

# Criando uma classe usando collections.namedtuple():
Pessoa = collections.namedtuple('Pessoa', 'nome email')

# Instanciando um objeto chamado felicity:
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

# Provando que foi criada uma classe:
print(type(felicity))

# Imprimindo a classe:
print(felicity)

# Provando a otimização depois do Python 3.8 (50% de melhoria no tempo):
print(timeit('felicity.email', globals=globals()))

# Mostrando quem é o globals e que a nossa classe faz parte dele após criada:
print(globals())


# Outra melhoria no gerenciamento de memória:
import sys

# Melhoria no tempo de leitura e criação da informação abaixo:
print(sys.getsizeof(list(range(15122024))))
