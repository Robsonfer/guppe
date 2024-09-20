#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
AULA 121
EXERCÍCIOS PARA PRATICAR

EXERCÍCIO 1 - Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters
    e setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

from datetime import date


# Criando a classe pessoa:

class Pessoa:

    def __init__(self, nome: str, data_nascimento: date, email: str) -> None:
        self.__nome: str = nome
        self.__data_nascimento: date = data_nascimento
        self.__email: str = email

    # Criando a propriedade getter para nome:
    @property
    def nome(self) -> str:
        return self.__nome

    # Criando a proriedade setter para nome:
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    # Criando a propriedade getter para data_nasciento:
    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    # Criando a proriedade setter para data_nascimento:
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        self.__data_nascimento = data_nascimento

    # Criando a propriedade getter para email:
    @property
    def email(self) -> str:
        return self.__email

    # Criando a proriedade setter para email:
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    # Criando método para imprimir os dados e uma pessoa:
    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'e-mail: {self.email}')
        print(f'Data Nascimento: {self.data_nascimento}')


if __name__ == '__main__':
    p: Pessoa = Pessoa('Felicity Jones', date(1987, 7, 22), 'felicity@gmail.com')

    p.imprimir()
