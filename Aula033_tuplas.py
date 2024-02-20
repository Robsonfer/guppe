"""
Tuplas (tuple)

Muito parecido com listas. Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: isso signigica que ao se criar uma tupla, ela não pode ser mudada.
    Toda operação em uma tupla gera uma nova tupla.

"""
print('Provando que as tuplas são representadas por parênteses:')
print(type(()))

# CUIDADO 1: As tuplas são representadas por (), mas veja:
print('Criando uma tupla com parêmteses:')
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(f'O tipo da tupla1 é: {type(tupla1)}')
# ---------------------------------------------------------------
print('Criando uma tupla sem parêntese:')
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(f'O tipo da tupla2 é: {type(tupla2)}')
# O Python considera como uma tupla, mesmo o que é criado sem parênteses!

# CUIDADO 2: Tuplas com um elemento:
tupla3 = (4)
print(tupla3)
print(f'O tipo da tupla3 é: {type(tupla3)}')
# Ou seja, isso não é uma tupla. O Python identifica somente com int.
# ----------------------------------------------------------------
tupla4 = (4,)
print(tupla4)
print(f'O tipo da tupla4 é: {type(tupla4)}')

# CONCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênte.
# (4) -> não é tupla | (4,) -> é tupla | 4 -> não é tupla | 4, -> é tupla

print('-----------------------------------------------------------')
print('Criando uma tupla com range:')
tupla = tuple(range(11))
print(tupla)
# Podemos gerar uma tupla dinamicamente com range. Tudo nos padrões já vistos anteriormente.

print('-----------------------------------------------------------')
print('Desempacotamento de tupla:')
tupla5 = ('Geek University', 'Programação em Python Essencial')
escola, curso = tupla5
print(escola)
print(curso)
# Da mesma forma que em listas, se colocarmos um número diferente de elementos para desempacotar, vai dar erro.
# Lembre-se, com exceção de ser imutável, todas as características são semelhantes às listas.

"""
IMPORTANTE: Métodos de adição e remoção de elementos nas tuplas não existem devido ao fato das tuplas serem imutáveis.
"""

print('-----------------------------------------------------------')
# Soma, Valo Máximo, Valor Mínimo e tamanho pode ser realizado se os valores forem todos inteiros:
print(f'Tupla de exemplo: {tupla}')
print(f'Exemplo de soma: {sum(tupla)}')
print(f'Exemplo de Valor Máximo: {max(tupla)}')
print(f'Exemplo de Valor Mínimo: {min(tupla)}')
# Se houver uma string no meio por exemplo, daria um erro.

print('-----------------------------------------------------------')
# Concatenação de tuplas:
print('Concatenando tuplas:')
print(f'Essa é a tupla: {tupla}')
print(f'Essa é a tupla1: {tupla1}')
print('Resultado da concatenação:')
print(tupla + tupla1) # Concatenando!
print('Note que concatenamos as tuplas, mas elas continuam imutáveis:')
print(f'Essa ainda é a tupla: {tupla}')
print(f'Essa ainda é a tupla1: {tupla1}')

print('Mas se quisermos criar uma nova tupla com essa soma, basta fazer assim:')
tupla6 = tupla + tupla1
print(f'Agora nós temos uma nova tupla que é a tupla6: {tupla6}')

print('Sobrescrevendo os valores da tupla:')
tupla += tupla1 # Sobrescrevendo!
print(f'Veja a tupla com valores sobrescritos de tupla1: {tupla}')
# As tuplas são imutáveis, mas podemos sobrescrever seus valores!

print('-----------------------------------------------------------')
# Podemos verificar se determinado elemento está contigo na tupla:
print('Verifcando se o elemento está contido na tupla:')
print(f'Existe o núemero 3 na tupla? {3 in tupla}')
print(f'Existe o núemero 33 na tupla? {33 in tupla}')
# Funciona exatamente como na lista.

print('-----------------------------------------------------------')
print('Iterando sobre uma tupla:')
for n in tupla:
    print(n)

print('-----------------------------------------------------------')
print('Iterando com índice:')
for indice, valor in enumerate(tupla):
    print(indice, valor)
