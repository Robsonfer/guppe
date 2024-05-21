"""
Filter
filter() -> Serve para filtrar dados de uma determinada coleção
"""

# Biblioteca para trabalhar com dados estatísticos:
import statistics

# Dados coltados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean():
media = statistics.mean(dados)
print(f'Média: {media}')

# Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.
res = filter(lambda valor: valor > media, dados)
"""
Tradução: res recebe a filtragem de dados por meio da função lambda que recebe o parâmetro x onde a exmpressão
lambda retorna filtrado somente os itens maiores do que a média da lista.
"""

# OBS Importante: O retorno da exmpressão lambda gera um retorno booleano (True ou False)

print(list(res))
print(f'Novamente: {list(res)}')
# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.
print(type(res)) # E como no map() o tipo do item é <class 'filter'>

# Utilização do filter() para remoção de dados faltantes:
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
retorno = filter(None, paises)
print(list(retorno))
# Note que depois do uso do None, a lista impressa não contém mais itens vazios.

# Podemos resolver de outra forma, com lambda por exemplo:
ret = filter(lambda pais: len(pais) > 0, paises)
print(list(ret))

# Podemos também resover ainda de uma terceira forma:
retorne = filter(lambda pais: pais != '', paises)
print(list(retorne))

"""
A diferença entre map() e filter() é:
    map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada
        elemento do iterável. A função retorna valores!
    filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
        de acordo com a função. Sempre retorna True ou False!
"""

# Exemplo mais complexo:

usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizza']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': []},
    {'username': 'Doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []}
]
print(usuarios)

# Forma 1:
inativos = filter(lambda usuario: len(usuario['tweets']) == 0, usuarios)
print(list(inativos))

# Forma 2:
inativos = filter(lambda usuario: not usuario['tweets'], usuarios)
print(list(inativos))

# Combinar filter() e map()
nomes = ['Vanesssa', 'Ana', 'Maria']
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

instrutora = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(instrutora)
"""
Traduzindo: Criamos uma lista chamada instrutora que vai receber primeiro um map() que receberá uma expressão
    lambda como função. Esta lambda só tem a função de pegar o nome que será iterado e apresentar com a frase: Sua
    instrutora é + o nome. Já no segundo parâmetro que seria o iterável, recebe um filter que vai filtrar dentre
    todos os nomes da lista nomes aquele que atende á função lambda que é o nome que tenha menos de 5 caracteres.
Note que tanto o map() quanto o filter() precisam ter dois parâmetros. No caso do map() o primeiro parâmetro é
    a lambda e o segundo é exatamente o filter() que vira o iterável. Já no caso do filter o primeiro parâmetro é
    a sua própria lambda e o segundo parâmetro é o iterável nomes.
"""
