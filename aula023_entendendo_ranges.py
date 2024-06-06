"""
 - É preciso conhecer o loop for para usar range;
 - É preciso conhecer range para trabalhar melhor com loops for.

De forma geral, ranges são utilizados para gerar sequências numéricas de forma não aleatória, mas sim especificada.

Forma Geral:

Forma 1:
range(valor_de_parada) -> Valor de parada não inclusive (início padrão 0, valor de parada definido, passo de 1 em 1)

Forma 2:
range(valor_de_inicio, valor_de_parada) -> Valor de parada não inclusive (início definido, passo de 1 em 1)

Forma 3:
range(valor_de_inicio, valor_de_parada, passo) -> Valor de parada não inclusive (início definido, valor de parada
definido, passo definido)

Forma 4 (igual à 3 mas ao inverso):
range(valor_de_inicio, valor_de_parada, passo) -> Valor de parada não inclusive (início definido, valor de parada
definido, passo definido)

"""

# Exemplo Forma 1:
for num in range(11):
    print(num)

# Exemplo Forma 2:
for num in range(4, 11):
    print(num)

# Exemplo Forma 3:
for num in range(0, 55, 5):
    print(num)

# Exemplo Forma 4 (inverso):
for num in range(10, -1, -1):
    print(num)
