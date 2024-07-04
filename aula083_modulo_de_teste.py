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
