"""
Map
Com Map fazemos mapeamento de valores para funções.
"""

import math

def area(r):
    """
    Calcula a área de um cícurulo com raio 'r'
    :param r: O raio da cincunferência
    :return: O cálculo da área: pi * raio ao quadrado
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

# Calculando da forma utilzano Map:
# Map é uma função que recebe dois parâmetros (a função, um iterável):
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
"""
Traduzindo: areas recebe um mapeamento da função area para todos os valores de raios,
ou seja, calcule a área para cada valor da lista raios.
"""

# Geralmente, onde vai a função area passa-se uma expressão lambda.
# Calculando usando Map com Lambda:
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# OBS: Após utilizar a função map depois da primeira utilização do resultado, ele zera!

"""
# Para fixar - Map

Temos dados iteráveis:
    - dados a1, a2,... an:

Temos uma função:
    - função: f(x)

Utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função

O Map Object que é gerado: f(a1), f(a2), ..., f(an)
"""

# Mais um exemplo:
cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
print(cidades)

# Converter de graus Celsius para Farenheight:
# Fórmula: f = 9/5 * c  + 32
c_to_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
"""
Traduzindo: celsius para farenheight recebe expressão lambda que tem como parâmetro dado e como retorno dado na posição
0 que são os nomes das cidades e a fórmula calculando com o dado da posição 1 que é a temperatura.
"""
print(list(map(c_to_f, cidades)))
