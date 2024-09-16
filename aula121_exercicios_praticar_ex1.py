#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
AULA 121
EXERCÍCIOS PARA PRATICAR

EXERCÍCIO 1 - Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters
    e setters para os atributos e um método para imprimir os dados de uma pessoa.
"""


# Criando a classe pessoa:

class Pessoa:

    def __init__(self, nome, data_nascimento, email):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__email = email

    def mostra_dados(self):
        print(f'NAME: {self.__nome} | BIRTH: {self.__data_nascimento} | E-MAIL: {self.__email}')


pessoa1 = Pessoa('Robson Ferreira', '17/09/1980', 'robsonnfer@gmail.com')
pessoa2 = Pessoa('Rosângela S. Ferreira', '02/10/1981', 'rosantiniatelie@gmail.com')

pessoa1.mostra_dados()
pessoa2.mostra_dados()
