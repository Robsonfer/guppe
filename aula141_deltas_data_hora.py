"""
Aula 141 - Trabalhando com Deltas de Data e Hora

O que é Delta de data e hora?

data_inicial = dd/mm/yyyy 12:55:34.993929
data_final = dd/mm/yyyy 13:34:23.0948484

    É a diferença entre duas datas e horas:
    delta = data_final - data_inicial
"""

import datetime

# Pegando a data atual:
data_hoje = datetime.datetime.now()

# Data de ocorrência futura:
ano_novo = datetime.datetime(2025, 1, 1, 0, 0)

# Calculando o Delta:
tempo_para_evendo = ano_novo - data_hoje

print(type(tempo_para_evendo))
print(repr(tempo_para_evendo))
print(tempo_para_evendo)
print(f'Faltam {tempo_para_evendo.days} dias e {tempo_para_evendo.seconds / 60 / 60} horas para o Ano Novo!')

print('--------------- Calculando data Futura ---------------')

# Calculando data futura:

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=30)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
