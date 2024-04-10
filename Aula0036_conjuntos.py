"""
AULA 36 - CONJUNTOS

- Conjuntos em qualquer linguagem de programação, é uma referência à teoria dos conjuntos da matemática.

- Em Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática, os Sets (conjuntos):
    - Não possuem valores duplicados;
    - Não possuem valores ordenados;
    - Os elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Desta forma, conjuntos são bem utilizados quando precisamos armazenar elementos e:
    - Não precisamos nos preocupar com a ordenação deles;
    - Não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Pyton com chaves {}

A diferença entre Conjutos (Set) e Mapas (Dicionários) em Python é que um dicionário tem chave/valor enquanto um conjunto tem apenas valores.
"""

# Definindo um conjunto:

# Forma 1:
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3} # Repare que em "s" temos valores repetidos.
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não fará parte do conjunto.
set
"""
Forma 2 (mais comum): A forma 2 e mais comumente usada é na verdade a forma 1.
Pelo que eu compreendi, a forma 1: s = set({1, 2, 3}) o Pycharm não aceita mais.
Todas as vezes que eu tentei fazer o editor corrigiu para a forma correta.
"""

# Podemos verificar se determinado elemento está contido no conjunto:
if 3 in s:
    print(f'Temos o número 3 em {s}')
else:
    print(f'Não temos o número 3 em {s}')

# Importante lembrar que além de não ter valores duplicados, não temos valores ordenados tabmém:
dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

lista = list(dados)
tupla = tuple(dados)
dicionario = {}.fromkeys(dados)
conjunto = set(dados)

print(f'Esta é a nossa lista: {lista}')
print(f'Esta é a nossa tupla: {tupla}')
print(f'Esta é o nosso dicionário: {dicionario}')
print(f'Este é o nosso conunto: {conjunto}')
