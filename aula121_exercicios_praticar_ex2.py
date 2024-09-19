#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
AULA 121
EXERCÍCIOS PARA PRATICAR

EXERCÍCIO 2 - Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
    a) armazenar_contato(contato: Contato);
    b) remover_contato(contato: Contato);
    c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
    d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
    e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""


class Agenda:

    def __init__(self, nome):
        self.__nome = nome
