"""
Aula 163 - Fazendo uso de Annotations

Annotations nos ajuda a usar o type hinting, por exemplo:

def cabecalho(texto: str, alinhamento: bool = True) -> str:

No trecho de código acima, quando usarmos <texto: str> ou <alinhamento: bool>, nós anotando no parâmetro texto informando 
    que ele é do tipo string, anotando no parâmetro alinhamento que ele é do tipo booleano e por fim, anotando na função
    cabeçalho que o retorno dela deve ser uma string.

IMPORTANTE:

Correto:
    texto: str
    () -> str
    alinhamento: bool = True

Incorreto:
    texto:str
    texto : str
    ()->str
    () ->str
    alinhamento:bool=True
    alinhamento : bool = True
    alinhamento: bool=True
    alinhamento: bool= True

"""

# Como reconhecer os Annotations em Python:

import math

def cincunferencia(raio: float) -> float:
    return 2 * math.pi * raio

print(cincunferencia.__annotations__)
