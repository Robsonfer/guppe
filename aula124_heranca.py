#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
HERANÇA (Inheritance)

A ideia de Herança é a de reaproveitar codigo e também extender as nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e
    métodos da classe herdada.

Para entender melhor, pensemos num banco e neste banco temos duas entidades:

Cliente:
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário:
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

Com base nisso, existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a
    outras entidades?

OBS: QUANDO UMA CLASSE HERDA DE OUTRA CLASSE, ELA HERDA TODOS OS ATRIBUTOS E MÉTODOS DA CLASSE HERDADA.

Quando uma classe herda de outra classe, a classe hredadda é conhecida por:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica.

Quando uma classe herda de outra classe, a classe herdeira é chamada:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica.


Sosbrescrita de Métodos (Overriding)
    Ocorre quando reescrevemos/reimplementamos um método presente na super classe ou em classes filhas.
"""

# Formato sem aplicar Herança (para testar basta tirar as àspas triplas:
"""
class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
"""

# Código refatorado aplicando Herança:
"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, renda, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa
    def __init__(self, matricula, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente(5000, 'Angelina', 'Jolie', '123.456.789-00')
funcionario1 = Funcionario('1234', 'Felicity', 'Jones', '987.654.321-11')

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Vamos analisar os dicionários de cada objeto:
print(cliente1.__dict__)
print(funcionario1.__dict__)

# Note que ele mostra as duas classes ao mostrar os atributos, inclusive mostra no formato Name Mangling para poder
#   ter acesso normalmente.
"""


# Sobrescrita de métodos (Overriding):

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa
    def __init__(self, renda, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa
    def __init__(self, matricula, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    # Usando o conceito de Sobrescrita de Métodos:
    def nome_completo(self):
        print(super().nome_completo()) # Acessando o método original usando super()
        return f'nº Matrícula: {self.__matricula} | Nome: {self._Pessoa__nome}' # Name Mangling


cliente1 = Cliente(5000, 'Angelina', 'Jolie', '123.456.789-00')
funcionario1 = Funcionario('1234', 'Felicity', 'Jones', '987.654.321-11')

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
