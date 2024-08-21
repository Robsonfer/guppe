#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Funções de Maior Grandeza - Higher Order Functions (HOF)

O que isso significa?
    - Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
    como resultado, ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo criar variáveis
    do tipo de funções em nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python as funções são cidadões de primeira classe (First Class Citizen)
"""


# Exemplo - Definindo as funções:


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções:

# Somar:
print(f'Esse é o resultado da soma: {calcular(10, 10, somar)}')

# Diminuir:
print(f'Esse é o resultado da subtração: {calcular(10, 10, diminuir)}')

# Multiplicar:
print(f'Esse é o resultado da multiplicação: {calcular(10, 10, multiplicar)}')

# Dividir:
print(f'Esse é o resultado da divisão: {calcular(10, 10, dividir)}')

print('-------------------')

# Nested Functions - Funções Aninhadas:

"""
Em Python podemos também ter funções dentro de funções, que são conhecidas como Nested Functions
ou também como Inner Functions (Funções Internas)
"""

# Exemplo:

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))

    return humor() + pessoa


print(cumprimento('Robson'))
print(cumprimento('Robson'))
print(cumprimento('Robson'))
print('-------------------')


# Retornando funções de outras funções:
def faz_me_rir():
    def rir():
        return choice(('haha', 'kkk', 'hehe'))

    return rir


"""
Note que no exemplo anterior era retornada a EXECUÇÃO da função (), neste caso, será retornada a função e não a sua
execução.
"""

# Testando:

rindo = faz_me_rir()
print(f'Executando a variável rindo: {rindo()}')
print('-------------------')

"""
As Inner Functions também conhecidas como Funções Internas ou Nested Functions podem acessar o escopo de funções
mais externas.

Por exemplo:
    - A função rir() consegue acessar o escopo da função faz_me_rir();
    - A função humor() consegue acessar o escopo da função cumprimento(pessoa).
"""


# Exemplo da explicação acima:

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kkk', 'rsrsrs', 'hahaha'))
        return f'{risada} {pessoa}'

    return dando_risada


# Testando:

rindo_novamente = faz_me_rir_novamente('Fernanda')
print(rindo_novamente())
print(rindo_novamente())
print(rindo_novamente())
