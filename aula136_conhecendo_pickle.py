"""
Aula 136 - Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:
    Objeto Python -> Binarização
    Binarização -> Objeto Python

Este proceso é chamado de serialização/deserialização

OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma, não é recomendado trabalhar com 
    arquivos Pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas.


"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    def comer(self):
        print(f'{self.nome} está comendo!')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def mia(self):
        print(f'{self.nome} está miando!')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def late(self):
        print(f'{self.nome} está latindo!')


"""
felix = Gato('Felix')
pluto = Cachorro('Pluto')
"""


# Fazendo a escrita em arquivos Pickle:

"""
with open('animais.pickle', 'wb') as arquivo: # wb neste caso significa write binary
    pickle.dump((felix, pluto), arquivo)
"""

# Note que não conseguimos ler este arquivo. Os dados serializados não podem ser lidos por nós humanos.


# Fazer a leitura de arquivos de dados no formato Pickle:

with open('animais.pickle', 'rb') as arquivo: # rb neste caso significa read binary
    gato, cachorro = pickle.load(arquivo)

    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo do cachorro é {type(cachorro)}')
