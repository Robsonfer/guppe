#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Teste de velocidade com Expressões Geradoras

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

# Ambos são generators, mas o primeiro foi feito através da função nums().
# O segundo não tem função por isso é uma expression
# Os dois são executados de formas diferentes.
"""

# Realizando o teste de velocidade:
import time

# Generator Expression:

gen_inicio = time.time()
print(sum(num for num in range(100000000))) # 100 milhões
gen_tempo = time.time() - gen_inicio


# List Comprehension:

list_inicio = time.time()
print(sum([num for num in range(100000000)])) # 100 milhões
list_tempo = time.time() - list_inicio

print(f'O Generator Expression levou {gen_tempo} segundos.')
print(f'O List Comprehension levou {list_tempo} segundos.')
