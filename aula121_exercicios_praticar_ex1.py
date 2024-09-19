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

    @property
    def nome(self) -> str:
        return self.__nome

