"""
POO - HERANÇA MÚLTIPLA

Herança múltipla nada mais é do que a possiblidade de uma classe herdar de múltiplas classes fazendo com que a classe filha herde todos os
    atributos e métodos de todas as classes herdadas.

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta;
    - Ou por multiderivação indireta.


# Exemplo de Multiderivação Direta:

class Base1:
    pass


class Base2:
    pass

class Base3:
    pass


class Multiderivada_dir(Base1, Base2, Base3): # Em Python uma classe pode herdar de quantas outras classes quisermos
    pass


# Exemplo de Multiderivação Indireta:

class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class Multiderivada_ind(Base6): # Note que nossa classe herda diretamente a Base6 e indiretamente todos os atributos de Base5 e Base4
    pass


OBS: Não importa se a Derivação é direta ou indireta, a classe que realizar a Herança, herdará todos os atributos e métodos das
    super classes.
"""


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
    def __init__(self, nome):
        super().__init__(nome)


# Testanndo:

baleia = Aquatico('Willy')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar()) # 
