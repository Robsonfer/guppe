# -*- coding: UTF-8 -*-

"""
Aula 165 - Tipos em Python na Prática
"""

# Jogo de cartas V2 - Com type hints:
# link dos naipes: https://www.alt-codes.net/suit-cards.php

import random
from typing import List, Tuple, Set, Dict

NAIPES = ['copas', 'espadas', 'paus', 'ouros']
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = tuple[str, str]
BARALHO = list[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """
    Cria um baralho com 52 cartas
    :param aleatorio: Iniciando em False
    :return: variável baralho criado com 52 cartas
    """
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> tuple[BARALHO, BARALHO,BARALHO, BARALHO]:
    """
    Gerencia a mão de cartas conforme o baralho gerado.
    :param baralho: Variavel retornada da função criar_baralho
    :return: Retorna cartas para quatro jogadores
    """
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """
    Inicia um jogo de cartas para quatro jogadores
    :return: Retorna
    """
    cartas: BARALHO = criar_baralho(aleatorio=True)
    jogadores: list[str] = 'Player1 Player2 Player3 Player4'.split()
    maos: dict[str, BARALHO] = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
