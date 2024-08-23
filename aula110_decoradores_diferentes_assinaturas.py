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

# A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada.
# A questão de diferentes assinaturas fica à cargo dos parâmetros *args e **kwargs que permitem que utilizemos quantos parâmetros quisermos.

@gritar
def lol():
    return 'lol'

print(lol())

# Por exemplo nesta última função que não tem parâmetro nenhum, mas funciona do mesmo jeito quando decorada com @gritar.

# OBS: Vale lembrar também que podemos utilizar parâmetros nomeados:

print(ordenar(acompanhamento='batata frita', principal='picanha'))



# Decorator com argumentos:

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro argumento precisa ser igual a {valor}.'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


# Testando:

print(soma_dez(10, 12)) # 22

print(soma_dez(1, 21)) # Deveria ser 22 tbm, mas o primeiro argumento não é 10, retorna o aviso.

print(comida_favorita('pizza', 'churrasco')) # pizza, churrasco

print(comida_favorita('sanduíche', 'pizza')) # Deveria ser sanduíche e pizza, mas como o primeiro argumento não é pizza, retorna o aviso.
