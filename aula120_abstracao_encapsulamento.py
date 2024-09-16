#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
ABSTRAÇÃO E ENCAPSULAMENTO

O granade objetivo da programação orientada a objetos é encapusular o nosso código num grupo lógico e
    hierárquico utilizando classes.

ENCAPSULAMENTO:

Encapsular = O ato encapsular os elementos dentro de uma classe, ou o agrupamento de atributos e métodos:

- CLASSE
    - ATRITUTOS
        - a
        - b
        - c
    - MÉTODOS
        - a
        - b
        - c

Relembrando:

    Atributos e métodos privados em Python:

        Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado
        chamado __falar().

        Esses elementos privados só deveriam ser acessados dentro da classe, mas o Python não bloqueia este acesso
        fora da classe. Com Python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma de
        se acesar os elementos privados conforme abaixo:

            _Classe__elemento

        Exemplo acessando elementos privados fora da classe:

            instancia._Pessoa__nome
            instancia._Pessoa__falar()

ABSTRAÇÃO:

Abstração em programação orientada a objetos é o ato de expor apenas dados relevantes de uma classe, escondendo
    atributos e métodos privados do usuário.

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de $ {self.saldo} do titular {self.titular} com limite de $ {self.limite}')

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


# Testando a classe Conta:

conta1 = Conta('Geek', 150.00, 1500.00)

print(f'Conta Corrente nº: {conta1.numero}')
print(f'Nome do Títular: {conta1.titular}')
print(f'Saldo da conta: $ {conta1.saldo}')
print(f'Limite da conta: $ {conta1.limite}')

# Usar os atributos e métodos públicos são problemáticos, pois temos acesso direto a eles. Veja o que pode ser feito:

conta1.numero = 42
conta1.titular = 'Xuxa'
conta1.saldo = 100000.00
conta1.limite = 1000000.00

print(conta1.__dict__)

# Como o acesso está público, nós conseguimos não só ler os dados como também podemos alterá-los!

conta1.extrato()

# Isso acontece porque não encapsulamos os nossos dados como deveria.
"""


# Refatorando a nossa classe Conta com a nossa abstração:


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de $ {self.__saldo} do titular {self.__titular} com limite de $ {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('ATENÇÃO: O valor de depósito deve ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo - valor < self.__limite * -1:
                print('ATENÇÃO: VOCÊ ULTRAPASSOU O VALOR DO SEU LIMITE')
                print('OPERAÇÃO NÃO REALIZADA')
                print(f'Seu saldo é de: $ {self.__saldo}')
                exit(1)
            else:
                self.__saldo -= valor
        else:
            print('ATENÇÃO: O valor de saque deve ser positivo')

    def transferir(self, valor, conta_destino):
        # Removendo valor da conta de origem:
        self.__saldo -= valor

        # Adicionando taxa de transferência:
        taxa = valor * 0.01
        self.__saldo -= taxa

        # Adicionando valor à conta de destino:
        conta_destino.__saldo += valor

        print(f'Saldo transferido de $ {valor} e taxa de trasnferência de $ {taxa} somando $ {valor + taxa}')


# Testando a classe Conta após refatorada com abstração:

conta1 = Conta('Angelina', 150.00, 1500.00)
conta1.extrato()

conta2 = Conta('Felicity', 300.00, 2000.00)
conta2.extrato()

conta2.transferir(100.00, conta1)

conta1.extrato()
conta2.extrato()
