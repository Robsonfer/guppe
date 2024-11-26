"""
Aula 163 - Fazendo uso de Annotations

Annotations nos ajuda a usar o type hinting, por exemplo:

def cabecalho(texto: str, alinhamento: bool = True) -> str:

No trecho de código acima, quando usarmos <texto: str> ou <alinhamento: bool>, nós anotando no parâmetro texto
    informando que ele é do tipo string, anotando no parâmetro alinhamento que ele é do tipo booleano e por fim,
    anotando na função cabeçalho que o retorno dela deve ser uma string.

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

# Annotations não são de uso exclusivo de parâmetros/métodos:

"""
nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)
"""


# Annotations em POO:

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


p = Pessoa(nome='Robson', idade=44, peso=96.5)

print(p.__dict__)

# print(p.__annotations__) A classe em si não tem annotations

# O método andar tem annotations:
print(p.andar.__annotations__)

# O método construtor tem annotations:
print(p.__init__.__annotations__)
