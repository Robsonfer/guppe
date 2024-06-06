"""
Min e Max

max() = Retorna o maior valor de um iterável ou o maior de dois ou mais elementos.

min() = Retorna o menor valor de um iterável ou o menor de dois ou mais elementos.
"""

lista = [1, 8, 4, 99, 34, 129]
print(f'O maior número de nossa lista é: {max(lista)}')

tupla = (1, 8, 4, 99, 34, 129)
print(f'O maior número de nossa tupla é: {max(tupla)}')

conjunto = {1, 8, 4, 99, 34, 129}
print(f'O maior número de nosso conjunto(set) é: {max(conjunto)}')

# Importante lembrar que se não usarmos max(dicionario.values()) ele vai imprimir o índice
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'O índice do maior número de nosso dicionário é: {max(dicionario)}')

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'O maior número de nosso dicionário é: {max(dicionario.values())}')
# Conforme já estudamos, não importa qual seja o iterável

# Definido o max() entre dois ou mais valores:
"""
# Faça um programa que receba dois valores do usuário e mostre o maior:

valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
print(f'Entre {valor1} e {valor2}, o maior é: {max(valor1, valor2)}')

"""

# Definindo o max() entre três valores:
print(max(4, 67, 54))

# Definindo o max() entre strings:
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'd', 'e'))
print(max('Geek Universty'))

# Definindo o max() entre pontos flutuantes:
print(max(3.145, 5.789))

print(' -------------- Exemplos de min() -------------- ')

lista = [1, 8, 4, 99, 34, 129]
print(f'O menor número de nossa lista é: {min(lista)}')

tupla = (1, 8, 4, 99, 34, 129)
print(f'O menor número de nossa tupla é: {min(tupla)}')

conjunto = {1, 8, 4, 99, 34, 129}
print(f'O menor número de nosso conjunto(set) é: {min(conjunto)}')

# Importante lembrar que se não usarmos max(dicionario.values()) ele vai imprimir o índice
dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'O índice do menor número de nosso dicionário é: {min(dicionario)}')

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(f'O maior menor de nosso dicionário é: {min(dicionario.values())}')
# Conforme já estudamos, não importa qual seja o iterável

# Definido o min() entre dois ou mais valores:

"""

# Faça um programa que receba dois valores do usuário e mostre o menor:
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
print(f'Entre {valor1} e {valor2}, o menor é: {min(valor1, valor2)}')

"""

# Definindo o min() entre três valores:
print(min(4, 67, 54))

# Definindo o max() entre strings:
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'd', 'e'))
print(min('Geek Universty'))

# Definindo o max() entre pontos flutuantes:
print(min(3.145, 5.789))

print(' -------------- Mais Exemplos -------------- ')

# Exemplos mais complexos de min() e manx():
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

"""
Note que quando pedimos o min() e o max() da lista de nomes, o Python não entende quem é o maior nome e sim quem é
o primeiro em ordem alfabética e quem é o útlimo em ordem alfabética!
"""
print(max(nomes)) # Tim
print(min(nomes)) # Aria

"""
Para conseguir o min() e o max() pelo tamanho do nome, precisamos usar o atributo key com uma expressão lambda
para que ele encontre o tamanho de cada nome dentro da lista nomes e depois defina o menor e o maior!
"""
print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim

# Tirando o min() e o max() de uma lista de dicionários:
musicas = [
    {"titulo": "Thunderstruck", "tocou": 15},
    {"titulo": "Black Ice", "tocou": 9},
    {"titulo": "Back in Black", "tocou": 20},
    {"titulo": "Highway to Hell", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica["tocou"]))
print(min(musicas, key=lambda musica: musica["tocou"]))
# Sem usar o key com a expressão lambda, o Python nem entende o que é para considerar como min() e como max()

# DESAFIO 1! Imprima somente o título da música mais e menos tocada:
print(max(musicas, key=lambda musica: musica["tocou"])['titulo'])
print(min(musicas, key=lambda musica: musica["tocou"])['titulo'])
"""
Dado que o que estamos imprimindo é o próprio objeto, basta no final e fora do mas, mas dentro do print, pedir para
imprimir somente o ['titulo´].
"""

# DESAFIO 2! Como encontrar a música mais tocada e a menos, sem usar max(), min() e lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

# Repare o quão grande fica o código usando for ao invés do min() ou do max(), sem contar a ajuda do lambda!
