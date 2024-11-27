"""
Aula 164 - Tipos em comentários
"""

import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))

"""
Note que não foi colocado o type hinting na linha da função, mas no comnetário temos o tipo para o parâmetro de
    entrada e logo em seguida o parâmetro do retorno da função.

É recomendado que utilizemos o type hinting na função, mas é importante conhecer outros formatos, pois podemos
    nos deparar com códigos escritos assim.
"""


# Mas e se a função tiver múltiplos argumentos?

def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


print(cabecalho1(texto='Geek'))


# Veja neste outro formato, embora estranho, funciona:

def cabecalho2(
        texto,  # type:str
        alinhamento=False  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


print(cabecalho2(texto='Geek'))

# O mesmo vale para variáveis:

nome = 'Geek University' # type: str

# Como comentado anteriormente, é melhor fazer type hinting por annotations, mas também é bom estar preparado.
