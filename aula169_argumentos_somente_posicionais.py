"""
Aula 169 - Argumentos somente posicionais

Parâmetro de uma função: A variável que receberá um valor dentro da função
Argumento de uma função: O valor recebido pelo parâmetro ao chamar a função ou ao declarar o parâmetro.
"""

# Exemplo:

valor = "67.3"
print(float(valor))


def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek')) # Neste caso não aceita nomear o argumento.


# Exemplos usando mais de um argumento:
def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', mensagem='Bem vinda'))


# Quando colocarmos a barra no final com mais de um parâmetro, tudo o que vier antes será só argumento posicional:
def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Robson'))


# Como obrigar o utilizador a informar o parâmetro:
def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


print(cumprimenta_v5(nome='Geek 5'))
# print(cumprimenta_v5('Geek')) # Neste caso, agor avai dar erro!
# O asterisco diz que todos os argumentos usados após ele, deverão ser informados os parâmetros obrigatóriamente.


# Assim é possível criar funções com todas as possibilidades:
def cumprimenta_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimenta_v6('Geek', mensagem1='Hello', mensagem2='tenha um ótimo dia!'))
print(cumprimenta_v6('Geek', mensagem2='tenha um bom dia'))
# print(cumprimenta_v6('Geek', 'Oi', 'vamos?')) # Não informando o parâmetro para o argumento vai dar erro.
