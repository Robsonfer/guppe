#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Decoradores com diferentes assinaturas
"""

# Relembrando

"""
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de um(a) {principal}, acompanhdo de {acompanhamento}, por favor.'


# Testando:

print(saudacao('Angelina'))

print(ordenar('Hot Roll', 'Molho Tarê'))


Ao chamar a função decorada o Python dá um erro, pois a função gritar recebe somente um parâmetro, mas a função ordenar recebe dois.
Para resolver isso utilizamos um padrão de projeto chamado Decorator Pattern (*args, *kwargs)
"""

# Refatorando com Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de um(a) {principal}, acompanhdo de {acompanhamento}, por favor.'


# Testando:

print(saudacao('Angelina'))

print(ordenar('Hot Roll', 'Molho Tarê'))

print(ordenar('picanha', 'molho de pimenta'))
