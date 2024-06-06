"""
Map
Com map fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """
    Calcula a area de um círculo com raio 'r'
    :param r: radio da circunferência
    :return: cálculo da área da circunferência pi * r ** 2
    """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Calculando da forma comum:
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Caldulando utilizando o map:
# O Map é uma função que recebe dois parâmetros: o primeiro é a função, o segundo é um iterável.
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
