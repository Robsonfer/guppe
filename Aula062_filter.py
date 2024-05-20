"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção
"""

# Biblioteca para trabalhar com dados estatísticos:

import statistics

# Dados coltados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean():
media = statistics.mean(dados)
