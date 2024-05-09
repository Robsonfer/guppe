"""
List Comprehension
    - Podemos adicionar estruturas condicionais lógicas às nossas list comprehensions
"""

# Exemplo 1:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)

# Refatorando:

# Explicação: Qualquer número par, o mod de 2 é 0. Em Python 0 é False (bool). Portanto, not False = True
pares = [numero for numero in numeros if not numero % 2]

# Explicação: Qualquer número ímpar mod de 2 é 1. Em Python 1 é True (bool). Inverso do anterior!
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# Exemplo 2:
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
"""
Para cada numero na lista numeros, multiplique numero por 2 se o resto da divisão for 0,
caso contrário divida numero por 2.
"""
print(res)
