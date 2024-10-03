"""
Aula 131 - Exercício 3

Crie um programa, instancie um objeto da classe Carro e teste o seu médodo.
"""

from aula131_exercicio2 import Carro


if __name__ == '__main__':
    carro: Carro = Carro(marca='Volkswagen', modelo='Golf', portas=4)

    carro.imprimir()
