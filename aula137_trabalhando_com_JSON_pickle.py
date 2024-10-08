"""
Aula 137 - Trabalhando com JSON e Pickle

JSON -> Javascript Object Notation

API -> Application Programing Interface -> São meios de comunicação entre os serviços oferecidos por empresas como
    o Twitter, Facebook, YouTube dentre várias outras e teceiros (nós desenvolvedores).

Exemplo:

import json

ret = json.dumps(['produto', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)


"""

import json


class Gato:
    def __init__(self, nome, raca) -> None:
        self.__nome = nome
        self.__raca = raca
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def raca(self):
        return self.raca
