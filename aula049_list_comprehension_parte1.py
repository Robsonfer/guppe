"""
List Comprehension
    - Utilizando lists comprehensions, nós podemos gerar novas listas com dados processados a partir de
    outro iterável.

Sitaxe da List Comprehension:

[dado for dado in iterável]
"""

# Exemplos:

# Exemplo 1:
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
# para cada número da lista numeros, multiplique-o por 10
print(res)
# Resultado: [10, 20, 30, 40, 50]

"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em duas partes:
    - A primeira parte:
        for numero in numeros
    - A seguunda parte:
        numero * 10
"""

# Exemplo 2:
result = [numero / 2 for numero in numeros]
print(result)


# Exemplo 3:
def funcao(valor):
    return valor * valor


resultado = [funcao(numero) for numero in numeros]
print(resultado)

# LIST COMPREHENSION X LOOP

# Loop
lista = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
# Para cada número na lista de numeros, gera pra mim um numero_dobrado que vai ser numero * 2
# E na minha lista de numeros_dobrados, adiciona um numero_dobrado
# No final imprime minha lista numeros_dobrados
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])
# O mesmo resultado do Loop com apenas uma linha contra cinco linhas!

# Exemplo 4:
nome = 'Geek Unversity'
print([letra.upper() for letra in nome])


# Exemplo 5:
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'júlia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
# O professor fez assim...

# O exemplo acima feito em uma única linha (fora a criação da lista)
print([amigo.title() for amigo in amigos])
# Mas eu preferi fazer assim, sem função caixa_alta() só title()

# Exemplo 6:
print([numero * 3 for numero in range(1, 11)])

# Exemplo 7:
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
# Convertendo em booleano os valores da lista dada!

# Exemplo 8:
print([str(numero) for numero in [1, 2, 3, 4, 5]])
