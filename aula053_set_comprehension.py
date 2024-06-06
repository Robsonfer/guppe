"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""

# Exemplo 1:
numeros = {num for num in range(1, 7)}
print(numeros)
print(type(numeros))

# Exemplo 2:
numeros = {x ** 2 for x in range(10)}
print(numeros)

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dicionário ao invés de Set:
num = {x: x ** 2 for x in range(10)}
print(num)

# Exemplo 3 com strings:
letras = {letra for letra in 'Geek University'}
print(letras)
