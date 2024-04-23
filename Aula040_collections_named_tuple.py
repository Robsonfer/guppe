"""
Módulo Collections - Named Tuple

São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros.

Documentação: https://docs.python.org/3/library/collections.html#collections.namedtuple
"""

# Recapitulando Tuplas:
tupla = (1, 2, 3)
print(tupla[1])

# Fazendo o import
from collections import namedtuple

# Definindo nome e parâmetros.

# Forma 1 - Declarando a Named Tuple:
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declarando a Named Tuple:
cachorro1 = namedtuple('cachorro1', 'idade, raca, nome')

# Forma 3 - Declarando a Named Tuple:
cachorro2 = namedtuple('cachorro2', ['idade', 'raca', 'nome'])

# Depois de declarar as named tuples como usar as  named tuples:
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

bob = cachorro1(idade=5, raca='Pastor Alemão', nome='Bob')
print(bob)

jack = cachorro2(idade=10, raca='Pincher', nome='Jack')
print(jack)

# Acessando os dados das named tuples:

# Forma 1:
print(f'O nome do meu cachorro é {ray[2]}')
print(f'A idade do {ray[2]} é de {ray[0]} anos')
print(f'A raça do {ray[2]} é {ray[1]}')

# Forma 2 (melhor forma):
print(f'O nome do meu cachorro é {bob.nome}')
print(f'A idade do {bob.nome} é de {bob.idade} anos')
print(f'A raça do {bob.nome} é {bob.raca}')

# Perguntando o índice pelo dado (já conhecemos):
print(f'Qual é o índice da tupla na posição do nome do cachorro Jack? {jack.index('Jack')}')

# Contando os dados (já conhecemos):
print(f'Quantas vezes aparece o nome Jack nessa tupla? {jack.count('Jack')}')
