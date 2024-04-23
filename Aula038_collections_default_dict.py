"""
Módulo Collections - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um
    lambda praa isso. Estes valor será utilizado sempre que não houver um valor definido. Caso tentemos
    acessar uma chave que não existe, essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores.

Documentação: https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

# Recapitulando Dicionários
dicio = {'curso': 'Programação em Python'}
print(dicio)
print(dicio['curso'])

# Fazendo o import
from collections import defaultdict

# Criando o dicionário defaultdict com a função lambida e pedindo pra retornar 0:
dicionario = defaultdict(lambda: 0)
print(dicionario)

# Adidiconando a chave curso neste dicionário defaultdict:
dicionario['curso'] = 'Programação em Python Essencial'
print(dicionario)

# Tentando acessar uma chave que não existe:
print(dicionario['outro']) # Não vai dar erro

# Resultado da tentativa:
print(dicionario)
# Foi criada mais uma chave agora com o nome de outro!

# Brincando um pouco pra testar o defaultdict:
dictest = defaultdict(lambda: 0)
print(f'Imprimindo dictest sem parâmetros, só lambda: {dictest}')
dictest['Nome'] = 'Robson'
dictest['Sobrenome'] = 'Ferreira'
print(dictest)
print(dictest['Idade'])
print(dictest)
dictest['Idade'] = 43
print(dictest)
dictest.pop('Idade')
print(dictest)
