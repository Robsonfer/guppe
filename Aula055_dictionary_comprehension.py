"""
Dictionary Comprehension

Pense no seguinte:

Quando queremos criar uma lista, fazermos o seguinte:
lista = [1, 2, 3, 4]

Para criar uma tupla:
tupla = (1, 2, 3, 4)

Para criar um set:
conjunto = {1, 2, 3, 4}

Para criar um dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Sintaxe do Dictionary Comprehension
{chave:valor for valor in iterável}
"""

# Exemplo 1:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()} # nunca esquecer da relação chave/valor e do final .items()
# Traduzindo: para cada par chave/valor no dicionario numeros, eleve ao quadrado cada número do par chave/valor.
print(quadrado)

# Exemplo 2:
nums = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in nums}
# Traduzindo: Para cada valor da lista nums coloque o valor como chave e eleve o mesmo valor ao quadrado e use como valor de chave/valor
print(quadrados)

# Parei em 12:11
