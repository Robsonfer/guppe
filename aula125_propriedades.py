#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
POO - PROPRIEDADES (PROPERTIES)

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos criar métodos públicos para a manipulação
    destes atributos. Esses métodos são conhecidos como getters e setters, onde os getters retornam o valor do atributo e os setters alteram
    o valor do mesmo.

To Get = Obter (Ou seja, obter o dado de seu endereço, to get)
To Set = Definir (Ou seja, definir um valor para esse dado, setar um atributo, to set)

IMPORTANTE: O getter é um método normal de ser criado e de boa, porém o setter é um método perigoso, pois como o próprio nome diz, ele pode
    alterar dados de um atributo.
"""


# Getters e Setters:
"""
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite) -> None:
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Saldo em conta de: $ {self.__saldo} do cliente: {self.__titular}'
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.__saldo -+ valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor


    # Refatorando a partir daqui:

    def get_numero(self):
        return self.__numero
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite
    
    def set_limite(self, limite):
        self.__limite = limite


conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())

# Agora imagine que precisamos somar o saldo das duas contas, podemos proceder assim:

soma_saldos = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é de $ {soma_saldos}')
"""

"""
E vai funcionar normalmente, entretanto, lembremos que essa forma de se fazer é errada, pois se o elemento foi declarado como privado,
    ele deve continuar privado. Ou seja, não deve ser acessado de fora da classe.

A melhor forma de acessar estes atributos é criando métodos para manipulá-los, ou seja, criar métodos getters e setters.

Vamos refatorar o código colocando estes métodos.
"""

# Vamos testar um método setter:
"""
print(conta1.__dict__)
conta1.set_limite(10000)
print(conta1.__dict__)
"""


# Agora vamos refatorar a classe Conta utilizando Propriedades:

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite) -> None:
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    # Usando Propriedades:
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    # Criando um setter para o limite:
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
    

    def extrato(self):
        return f'Saldo em conta de: $ {self.__saldo} do cliente: {self.__titular}'
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.__saldo -+ valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    @property
    def valor_total(self):
        return self.__saldo + self.__limite

# Instanciando os objetos:
conta1 = Conta('Felicity', 3000, 5000)
conta2 = Conta('Angelina', 2000, 4000)

# Mostrando o extrato:
print(conta1.extrato())
print(conta2.extrato())

# Somando os saldos das duas contas (objetos):
soma_saldos = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é de $ {soma_saldos}')

# Setando o limite e mostrando o antes e o depois:
print(conta1.__dict__)
conta1.limite = 10000
print(conta1.__dict__)
print(f'$ {conta1.limite}')

# Mostrando o valor total (saldo + limite):
print(conta1.valor_total)
print(conta2.valor_total)
