#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Forçando tipos de dados com decoradores

Nós sabemos que em Python não é necessário declarar o tipo da variável antes da própria variável com é o caso com
C ou Java. O tipo dda variável é determinado conforme o seu conteúdo. Entretando, em algumssa situações pode ser
interessante forçar o tipo da variável para evitar ter problemas com as nossas funções.

Quando for esse o caso, podemos criar um decorator que sirva para força um tipo de dado para entrada de uma função.
"""

# Exemplo:

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor,tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '5')


@forca_tipo(float, float)
def dividir(a, b):
    print(a) # verificando se o int foi convertido para float no recebimento do valor da variável
    print(b) # verificando se o int foi convertido para float no recebimento do valor da variável
    print(a / b) # verificando se o resultado acompanhou o tipo das variáveis recebidas


dividir('1', 5)
