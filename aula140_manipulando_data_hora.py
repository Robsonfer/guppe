"""
Aula 140 - Manipulando data e hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora chamado datetime
"""

import datetime

# print(dir(datetime))

# Retorna o ano máximo suportado pelo Python:
print(datetime.MAXYEAR)

# Retorna o ano mínimo suportado pelo Python:
print(datetime.MINYEAR)

# Retorna a data e hora corrente:
print(datetime.datetime.now()) # 2024-10-08 21:49:40.657001

# Imprimindo a representação:
print(repr(datetime.datetime.now())) # datetime.datetime(2024, 10, 8, 21, 51, 25, 646957)

# replace() para fazer ajustes na data/hora:
inicio = datetime.datetime.now()
print(inicio)

# Usando o replace() para ajustar a hora:
inicio = inicio.replace(hour=23, minute=59, second=59, microsecond=59)
print(inicio)
