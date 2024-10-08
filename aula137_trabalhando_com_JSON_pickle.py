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
        return self.__raca


felix = Gato('Felix', 'Vira-lata')

# Colocando a class Gato em formato JSON:

"""
print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)
"""

# Integrando o JSON com o Pickle (preciso instalar biblioteca jsonpickle):

import jsonpickle

"""
ret = jsonpickle.encode(felix)

print(ret)
"""


# Criando e escrvendo o arquivo JSON/Pickle:

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


# Lendo o arquivo JSON/Pickle:

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(type(ret))
    print(ret)
    print(ret.nome)
    print(ret.raca)
