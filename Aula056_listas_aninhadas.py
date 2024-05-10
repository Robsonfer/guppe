"""
Listas Aninhadas (Nested Lists)

 - Algumas linguagens de progrmação (C/Java/PHP) possumem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas que diferente das outras linguagens, aceitam tipos variados, não têm tamanhos fixos e muitas outras vantagens.

Nesta aula veremos o equivalente a listas multidimensionais ou Matrizes.
"""

# Exemplo 1:
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Equivale a uma matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0])
print(listas[0][1]) # [linha][coluna], ou seja [linha 0][coluna 1]
print(f'Imprimindo o item 2 (número 8) da terceira lista = {listas[2][1]}') # Acessando o número 8 da terceira lista
print(f'Mesmo acesso usando índice negativo = {listas[2][-2]}') # Mesmo acesso usando índice negativo

# Iterando com loops em uma lista aninhada:
for lista in listas:
    for numero in lista:
        print(numero)

# Agora usando List Comprehension:
[[print(valor) for valor in lista] for lista in listas]
# Traduzindo: para cada lista em listas e para cada valor em lista, imprimir o valor.
# Ou, para cada valor de cada lista de dentro de listas, imprimir esse valor.

# Outros Exemplos:

# Gerando um tabuleiro ou matriz 3 x 3:
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha:
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais:
print([['*' for i in range(1, 4)] for j in range(1, 4)])
