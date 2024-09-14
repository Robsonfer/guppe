#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
OBJETOS

Objetos: São Instâncias da Classe, ou seja, após o mapeamento do objeto do mundo real para a sua representação
    computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias
    de uma classe como variáveis do tipo definido na Classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf


class Contacorrente:
    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = Contacorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        Contacorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'NOME CLIENTE: {self.__cliente._Cliente__nome}')

    # Metodo criado como treino fora da aula:
    def mostra_cpf(self):
        print(f'CPF CLIENTE: {self.__cliente._Cliente__cpf}')

    def mostra_saldo(self):
        print(f'SALDO CONTA CORRENTE: {self.__saldo}')

    # Metodo criado como treino fora da aula:
    def deposita_retira(self):
        valor_operacao = int(input('Favor informar o valor da operação: '))
        operacao = input('Favor informar se deseja depositar ou sacar: ').lower()
        if operacao != 'depositar' and operacao != 'sacar':
            print('ATENÇÃO, PARA PROSSEGUIR, FAVOR INFORMAR A OPERAÇÃO CORRETA!')
        elif self.__saldo < valor_operacao:
            print(f'Atenção, seu saldo é insuficiente para esta operação: {self.__saldo}')
        elif operacao == 'depositar':
            self.__saldo += valor_operacao
            print(f'Operação realizada com sucesso, seu saldo é de: {self.__saldo}')
        else:
            self.__saldo -= valor_operacao
            print(f'Operação realizada com sucesso, seu saldo é de: {self.__saldo}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos:

# Ligando e desligando o objeto Lampada:
lamp1 = Lampada('branca', '110', '60')
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
lamp1.ligar_desligar()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')

print('-------------- Divisão --------------')


cliente1 = Cliente('Robson Ferreira', '123.456.789-01')

cc = Contacorrente(5000, 10000, cliente1)

cc.mostra_cliente()
cc.mostra_cpf()
cc.mostra_saldo()
cc.deposita_retira()
