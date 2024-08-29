#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
ORIENTAÇÃO A OBJETOS
    É um paradigma de programação que se utiliza de mapeamento de objetos do mundo real para modelos computacionais.
    Paradigma de programação é a forma/metodologia utilzada para pensar/desenvolver sistemas.

PARADIGMAS DE PROGRAMAÇÃO

- PROGRAMAÇÃO ESTRUTURADA
- PROGRAMAÇÃO ORIENTADA A OBJETOS
- PROGRAMAÇÃO FUCIONAL

PRINCIPAIS ELEMENTOS DA POO:
    - Classe: Modelo do objeto do mundo real representado computacionalmente;
    - Atributos: Características do objeto;
    - Métodos: Comportamento do objeto (funções);
    - Construtor: Método especial utilizado para criar os objetos:
    - Objetos: Também chamado instância da classe, é o resultado da soma dos atributos, métodos e construtor. É o
        produto final a partir da sua classe.

- PROGRAMAÇÃO ORIENTADA A OBJETOS
    Classe = Molde:
        Produto
            Atributos (características do produto):
                nome
                preço
                desconto
            Métodos (funcionalidades do produto):
                funções
            Construtor:
                Método para criar objetos a partir da classe
            Objetos/Instâncias:
                Notebook
                R$ 2.300,00
                15%
                ---------------
                Caneta BIC
                R$ 2,94
                5%

- PROGRAMAÇÃO FUNCIONAL
"""

# Verificando dados e tipos:

print('------- numero -------')
numero = 10
print(numero)
print(type(numero))

print('------- nome -------')
nome = 'Geek'
print(nome)
print(type(nome))

print('------- class Produto -------')


class Produto:
    pass


ps4 = Produto()

print(ps4)
print(type(ps4))
