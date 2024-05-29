"""
Sorted

OBS: Não confunda com a função sort(), pois o sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável. Como o próprio nome diz, sorted() é utilizado para ordenar.

OBS: O sorted() sempre retornará uma lista.
"""

# Relembrando o sort():
print('Relembrando o sort():')
lista = [4, 7, 3, 8, 1, 5, 9, 2, 0]
lista.sort()
print(lista)

# Exemplo de sorted() com lista:
print('Exemplo de sorted com listas:')
num_lista = [6, 1, 8, 2]
print(num_lista)
print(sorted(num_lista))

# Mas se a gente fizer o sorted() armazenando ele em uma nova variável, teremos essa lista ordenada:
print('Armazenando o sorted() em uma nova variável:')
new_num_lista = sorted(num_lista)
print(new_num_lista)

# Primeira diferença entre sort() e sorted(). O sort() modifica a ordem da lista, o sorted() não modifica a:
print('Iprimindo novamente a lista depois do sorted():')
print(num_lista)

# Exemplo de sorted() com tupla:
print('Exemplo de sorted com tuplas:')
num_tupla = (6, 1, 8, 2)
print(num_tupla)
# Importante: Não importa se eu uso o sorted() em uma tupla, ele sempre vai retonar uma lista:
print(sorted(num_tupla))

# Exemplo de sorted() com set:
print('Exemplo de sorted com sets:')
num_set = {6, 1, 8, 2}
print(num_set)
print(sorted(num_set))

# Exemplo de sorted() com dicionários:
print('Exemplo de sorted com dicionários:')
num_dict = {'c': 6, 'a': 1, 'd': 8, 'b': 2}
print(num_dict)
print(sorted(num_dict.items()))

numeros = [6, 1, 8, 2]

# Adicionando parâmetros ao sorted():
print('Exemplo usando o parâmetro reverse=True:')
print(numeros)
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

# Convertendo o resultado do sorted() para uma tupla:
print('Convertendo o tipo da saída do sorted() para tupla:')
print(sorted(numeros))
print(tuple(sorted(numeros)))

# Podemos utilizar o sorted() para coisas mais complexas:
usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': [], 'cor': 'Amarelo'},
    {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': ['Olá', 'Bom dia', 'Simples assim', 'Hahaha'], 'cor': 'Preto', 'música': 'Rock'}
]

print('Orndenando uma lista de dicionários pelo sorted():')
print('Imprimindo a lista original:')
print(usuarios)
print('Ordenando pelo tamanho dos dicionários:')
print(sorted(usuarios, key=len))
print('Ordenando de forma inversa pelo tamanho dos dicionários:')
print(sorted(usuarios, key=len, reverse=True))
print('Ordenando por nome de usuário em ordem alfabética:')
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
# Note que o key é o parâmetro onde nós informamos qual é a chave de ordenação que queremos utilizar
print('Ordenando pelos tweets:')
print(sorted(usuarios, key=lambda usuario: usuario["tweets"]))
print('Ordenando pela quantidade de tweets:')
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Último exemplo:
musicas = [
    {"titulo": "Thunderstruck", "tocou": 15},
    {"titulo": "Black Ice", "tocou": 9},
    {"titulo": "Back in Black", "tocou": 20},
    {"titulo": "Highway to Hell", "tocou": 32}
]

# Ordenando da mais tocada para a menos tocada:
print('Lista de músicas mais tocadas:')
print(musicas)
print('Em ordem da mais tocada até a menos tocada:')
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
