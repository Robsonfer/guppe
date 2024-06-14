"""
zip() = Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.
"""

# Exemplo 1:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionário!
print(list(zip1))
print(tuple(zip1))
print(set(zip1))
print(dict(zip1))

"""
O zip() cria tuplas com os elementos de todos os iteráveis juntando na mesma tupla os elementos por índice.

OBS: Note que nos casos de tuple(), set() e dict() ele retorna como vazio. O comportamento do zip() é exatamente igual
ao que vimos no map, filter e generator. Ou seja, assim que ele é trabalhado, ele some da memória.

Mas podemos executar novamente:
"""
zip1 = zip(lista1, lista2, 'abc')
print(list(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(tuple(zip1))
zip1 = zip(lista1, lista2, 'abc')
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

# Exemplo 2:
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
"""
O zip() utiliza como parametro, o menor tamanho em iterável. Isto significa que se estiver trabalhando com iteráveis
de tamnanho s diferente, irá parar quando os elementos do menor iteravel acabar.

Outra informação importante é que a ordem dos atributos importa, retorna na mesma ordem que os atributos são declarados
na função. Ver exemplo 3 abaixo:
"""

# Exemplo 3 - Ordem dos parâmetros:
zip2 = zip(lista3, lista2, lista1)
print(list(zip2))

# Exemplo 4:
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zip_total = zip(tupla, lista, dicionario.values()) # Não esquecer, para dicionário usar .values()
print(list(zip_total))

# Exemplo 5 - lista de tuplas:
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados))) # Lembre-se que usamos o * para desempacotar os valores

# Exemplo 6 (mais complexo):
# suponha que temos três alunos com duas notas cada um. Queremos saber qual á a maior nota de cada um deles:
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']

# Usando um dictionary compreension fazemos isso facilmente:
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
"""
Tradução: dado na posição zero será a chave e para o valor vamos coletar o maior valor (max) entre o dado da posição 1 
e o dado da posição 2. Fazer isso para cada dado do zip(alunos, prova1, prova2)!
"""
print(final)
