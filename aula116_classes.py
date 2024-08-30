#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
POO - CLASSES

Em POO, classes nada mais são do que modelos dos objetos do mundo real representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Nós podemos criar uma variável para idade, nome, preco e cada um vai ter o seu tipo de dados a ser recebido.
A idade receberá um tipo 'int', o nome um tipo 'str' e o preço um tipo 'float'.
Mas o que queremos de verdade é criar um tipo 'lampada'.
Quando criamos uma classe, então temos um tipo lampada (ver exemplo 1 abaixo). Ou seja, eu trouxe um objeto do
    mundo real representado computacionalmente através da criação de uma classe.

Classes podem conter:
    - Atributos: Representam as características do objeto, ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente terá como atributos a
    tensão (110V ou 220V), a cor (luz branca ou amarela), a luminosidade em lumens, etc.
    - Métodos (funções): Representam os comportamentos do objeto, ou seja, as ações que este objeto pode
    realizar no seu sistema. No caso da lâmpada, provavelmente um método seria de ligar e desligar.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos classes em Python, utilizmos por convenção o nome com inicial em maíusculo. Se o
    nome for composto, utiliza-se as iniciais de ambas as palavras em maíusculo e todas juntas.

OBS: As classes internas do Python, como a class 'int' por exemplo, são todas definidas com inicial minúscula.

Dica Geek: Em computação não utilizamos acentuação, caracteres especiais, espaços ou similares para nomes de
    classes, atributos, métodos, arquivos, diretórios, etc.

OBS: Quando planejamos um ‘software’ e definimos quais classe devemos ter no sistema, chamamos estes
    objetos que serão mapeados para classes de entidade.
"""


# Exemplo 1:


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


class Int:
    pass


lamp = Lampada()

print(type(lamp))
