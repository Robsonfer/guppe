# Módulo de teste para executar na aula de Módulos customizados

from random import (
    random,
    uniform
)


# --------- Gerando número aleatório de 0 a 100 com random() --------
def gera_aleatorio():
    print(f'Este é um número aleatório entre 0 e 100 gerado com random: {round(random() * 100)}')


# -------- Gerando número aleatório de 0 a 100 com uniform() --------
def gera_aleatorio_uniform():
    print(f'Este é um número aleatório entre 0 e 100 gerado com uniform: {round(uniform(1, 101))}')


# -------- Somando somente os números ímpares de uma lista --------
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]

# Converter de graus Celsius para Farenheight:
# Fórmula: f = 9/5 * c  + 32
c_to_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tupla = (1, 3, 5, 7, 9, 11, 13, 15)
