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

# Exemplo 3:
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo 4 (com lógica condicional):
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in numeros}
# Traduzindo: Para cada num em números, se o mod 2 de num for igual a zero, valor = 'par', caso contrário, valor = 'ímpar'
print(res)
