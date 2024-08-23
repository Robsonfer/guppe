#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Preservando Metadatas com Wraps

Metadatas (Metadados) -> São dados intrínsecos em arquivos.

Wraps -> São funções que envolvem elementos com diversas finalidades.


"""

print('----------- PROBLEMA -----------')

# Problema:

def ver_log(funcao):
    def logar(*args, **kwargs):
        """
        Função de Login dentro de outra
        :print: 'aviso de chamado da função'
        :print: 'documentação'
        :retun: funcao
        """
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """
    Soma dois números
    :return: a + b
    """
    return a + b


# Testando:

print(soma(10, 10))

print('----------- dividindo -----------')

print(soma.__name__) # Deveria imprimir: soma
print(soma.__doc__) # Deveria imprimir: Soma dois númeos :return: a + b

# Mas imprime o nome e a documentação da função decoradora

print('----------- SOLUÇÃO -----------')

# -------------------------------------------------------------------------------------------------------------- #

# SOLUÇÃO:

from functools import wraps


def ver_log(funcao):
    @wraps(funcao) # Essa é a solução do problema!
    def logar(*args, **kwargs):
        """
        Função de Login dentro de outra
        :print: 'aviso de chamado da função'
        :print: 'documentação'
        :return: funcao
        """
        print(f'Você está chamando a função {funcao.__name__}')
        print(f'Aqui está a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """
    Soma dois números
    :return: a + b
    """
    return a + b


# Testando:

print(soma(10, 10))

print('----------- dividindo -----------')

print(soma.__name__) # soma
print(soma.__doc__) # Soma dois númeos :return: a + b
print(help(soma))
