# -*- coding: UTF-8 -*-

"""
Aula 165 - Tipos em Python na Prática
"""

# Veja que podemos utilizar type hintings com tipos mais complexos:
"""
nomes: list = ['Geek', 'University']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'direcao': True, 'vidro_eletrico': True}
valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""

# Legal, mas a pergunta fica em como anotar os tipos dos dados dentro das coleções?
"""
from typing import Dict, List, Tuple, Set

nomes: list[str] = ['Geek', 'University']
versoes: tuple[int, int, int] = (3, 4, 7)
opcoes: dict[str, bool] = {'ar': True, 'direcao': True, 'vidro_eletrico': True}
valores: set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""

# Jogo de cartas V1 - Sem type hints:
# link dos naipes: https://www.alt-codes.net/suit-cards.php

import random

NAIPES = [
    'copas preto',
    'espadas preto',
    'paus preto',
    'ouros preto',
    'copas vermelho',
    'espadas vermelho',
    'paus vermelho',
    'ouros vermelho'
]
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """ Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


print(NAIPES)
print(CARTAS)
print(criar_baralho(aleatorio=True))
