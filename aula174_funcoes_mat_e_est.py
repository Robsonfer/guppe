"""
Aula 174 - Funções matemáticas e estatísticas
"""

import math

# MATEMÁTICA

print('---------- math.prod ----------')
# math.prod - Retorna o produto de um container numérico:

nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}

print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))


print('---------- math.isqrt ----------')
# math.isqrt - Retona a parte inteira de uma raíz quadrada. IMPORTANTE: eLe não arredonda valor:

print(math.isqrt(9))
print(math.isqrt(17))
print(math.sqrt(9))
print(math.sqrt(17))


print('---------- math.dist ----------')
# math.dist - Retorna a distância euclidiana entre dois pontos, sejam 3D ou 2D:
# Pontos 3D:

p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D:
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))


print('---------- math.hypot ----------')
# math.hypot - Retona a hipotenusa ou norma euclidiana:
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))
# O uso do asterisco é importante, pois ele serve para descompactar os valores de um container.


# ESTATÍSTICA

import statistics


print('---------- statistics.fmean ----------')
# statistics.fmean - Calcula a média de números reais:
valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))


print('---------- statistics.gometric_mean ----------')
# statistics.geometric_mean - Calcula a média geométrica de números reais;
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))


print('---------- statistics.multimode ----------')
# statistics.multimode - retorna o valor mais frequente em uma sequência:

seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
