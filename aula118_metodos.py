"""
POO - MÉTODOS

Métodos (funções): Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos em dois grupos: Métodos de Instância e Métodos de Classe.

MÉTODOS DE INSTÂNCIA

O método __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.
Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline).
Os Métodos/Funções Dunder em Python são chamados de Métodos Mágicos.

ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado.
    O Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
    dessas funções mágicas internas da linguagem. Portanto nunca faça isso!

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """
        Retorna o valor do produto com desconto
        :param porcentagem:
        :return:
        """
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


# Testando o método desconto:

produto1 = Produto('Playstation 5', 'Vídeo Game', 2300)

print(f'O valor do Pruduto com desconto é de R$ {produto1.desconto(20)}')

# Ou também podemos fazer assim, passando o self = produto1 e a porcentagem de desconto:
print(f'O valor do Pruduto com desconto é de R$ {Produto.desconto(produto1, 50)}')


# Testando o método nome_completo:

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())


# Testando o acesso à senha:

print(f'Senha user1: {user1._Usuario__senha}') # Acesso de forma errada a um atributo de classe
print(f'Senha user2: {user2._Usuario__senha}') # Acesso de forma errada a um atributo de classe
# Note que mesmo fazendo acesso de forma errada, nós conseguimos obter a senha dos usuários
