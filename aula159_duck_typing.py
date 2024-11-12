"""
Aula 159 - Duck Typing

Definição: Se determinado objeto parece um pato, anda como pato e nada como pato, então é um pato!

Isso significa que objetos similares devem ter métodos, atributos e comportamentos similares.

Note que tanto a classe CisneNegro quanto as variáveis nome, lista e dicio são similares.
Todos têm as mesmas características. Todos são containeres, ou seja, guardam uma quantidade de dados dentro, são iteráveis.
Embora a classe CisneNegro não aparente, o método __len__() foi implementado para ter o mesmo comportamento dos demais.
Já idade e peso têm somente um valor armazenado, portanto não são similares.
"""

class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {'Carlos': 12, 'Vanessa': 34, 'Joana': 49}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 42
peso = 81.4

print(len(idade))
