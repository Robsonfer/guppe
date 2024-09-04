#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
POO - ATRIBUTOS

Atributos: Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python dividimos os atributos em três grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos.

ATRIBUTO DE INSTÂNCIA: São atributos declarados dentro do método construtor.

OBS: O Método Construtor é um método especial utilizado para a construção do objeto.


"""

# Exemplos de Atributos de instância:


class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


# Seguem as demais classes conforme aula anterior:


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""
SOBRE A ESTRUTURA DO MÉTODO E SEUS ATRIBUTOS:

TRADUZINDO O MÉTODO ACIMA:
    1 - Logo na primeira linha declaramos a classe chamada Usuario
    2 - Em seguida criamos o método de inicialização onde nós declaramos como parâmetros:
        self (o próprio objeto);
        nome;
        email;
        senha;
    Com exceção do próprio objeto, todos estes parâmetros de instância são parâmetros comuns do objeto Usuario
    3 - Nas linhas abaixo onde está escrito self.nome = nome e demais leia-se:
        O objeto Usuario, no atributo nome vai receber nome;
        O objeto Usuario, no atributo email vai receber email;
        O objeto Usuario, no atributo senha vai receber senha.

O mesmo funciona para todas as demais classes. 

SIGNIFICADO DO SELF
O que significa o self declarado como primeiro parâmetro do método?
    Ele serve para informar que o próprio objeto é responsável pela execução do método.

Dica Geek: A palavra self na verdade é uma convenção, mas não é obrigação. Veja o exemplo abaixo. O método
    funcionará perfeitamente, ainda que o primeiro parâmetro seja definido como cerveja, mas veja que o Python
    vai te orientar a alterar o nome, pois não segue os padrôes da linguagem.
    Portanto, o primeiro parâmetro de um método é sempre self.
"""


class Teste:
    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade


"""
ATRIBUTOS PÚBLICOS E ATRIBUTOS PRIVADOS:

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público. Ou seja, pode ser 
acessado em todo o projeto.

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser 
acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ (duplo underscore) no
início de seu nome.

Isso é conhecido também como Name Mangling.
"""

