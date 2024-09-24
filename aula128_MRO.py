#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
POO - MRO (METHOD RESOLUTION ORDER)

Method Resolution Order, ou Ordem de Resolução de Métodos, é a ordem de execução dos métodos, ou seja,
    quem será executado primeiro.

Em Python podemos conferir a ordem de execução dos métodos (MRO) de três formas:
    - Via propriedade da classe __mro__;
    - Via método (mro)
    - Via help()
"""

# Relembrando aula anterior:

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Oi, eu sou o {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Olá, eu sou {self._Animal__nome} e sou um animal marinho!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Olá, eu sou {self._Animal__nome} e sou um animal terrestre!'


class Pinguim(Aquatico, Terrestre):
    # A ordem em que é declarada a herança determina quem será escolhido pelo método cumprimentar() para o objeto tux.
    def __init__(self, nome):
        super().__init__(nome)


# Vamos direto ao que interesa:
tux = Pinguim('Tux')
print(tux.cumprimentar())

"""
Note que quando temos herança múltipla:

Ao executar o método cumprimentar(), nós executamos a ordem:
    class Pinguim(Aquatico, Terrestre)
Nós temos o resultado do método cumprimentar da classe Aquatico, mas se invertermos a herança da classe para:
    class Pinguim(Terrestre, Aquatico)
Nós temos o resultado do método cumprimentar da classe Terrestre.
"""

# Conforme mencionado no enunciado, vamos usar as três formas de descobrir a ordem de execução do método cumprimentar():

print(Pinguim.__mro__)
print(Pinguim.mro())
print(help(Pinguim))
