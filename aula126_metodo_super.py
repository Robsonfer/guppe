#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
POO - Método super()

O método super() se refere à super classe.
"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie
    
    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')
    
class Gato(Animal):
    def __init__(self, nome, especie, raca):
        # Animal.__init__(self, nome, especie) # Podemos fazer assim tbm, mas o ideal é usar o super()
        super().__init__(nome, especie)
        super().faz_som('miau, miau')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')

felix.faz_som('miau')
