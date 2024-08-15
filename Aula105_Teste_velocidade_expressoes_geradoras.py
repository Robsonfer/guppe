#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Teste de velocidade com Expressões Geradoras
"""


# REVISANDO:

# Generators (Geradores)
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator

print(next(ge1))
print(next(ge1))
print(next(ge1))

# Generator Expression (Expressões Geradoras)
ge2 = (num for num in range(1, 10))

print(ge2)

print(next(ge2))
print(next(ge2))
print(next(ge2))

"""
Ambos são generators, mas o primeiro foi feito através da função nums().
O segundo não tem função por isso é uma expression
Os dois são executados de formas diferentes.
"""
