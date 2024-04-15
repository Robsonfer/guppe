"""
Módulo Collections - Ordered Dict

É um dicionário que nos garante a ordem de inserção dos elementos.

Documentação: https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""

# Em um dicionário, a ordem de inserção dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

print('Imprimindo os valores sem o Ordered Dict:')
for chave, valor in dicionario.items():
    print(f'chave = {chave} | valor = {valor}')

# fazendo o import
from collections import OrderedDict

dicio = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, })

print('Imprimindo os valores ordenados com Ordered Dict:')
for chave, valor in dicio.items():
    print((f'chave = {chave} | valor = {valor}'))

# Entendendo a diferença entre dict e ordered dict:

# Dicionários comuns:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(f'Como dicionário comum, o dict1 é igual ao dict2? {dict1 == dict2}')

# Dicionários ordenados:
dict3 = OrderedDict({'c': 3, 'd': 4})
dict4 = OrderedDict({'d': 4, 'c': 3})
print(f'Como dicionário comum, o dict3 é igual ao dict4? {dict3 == dict4}')

"""
A primeira comparação retorna como True porque a ordem não importa nos dicionários comuns,
mas a segunda comparação retorna como False porque a ordem importa nos dicionários ordenados! 
"""
