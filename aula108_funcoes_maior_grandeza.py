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


# Nested Functions - Funções Aninhadas:
