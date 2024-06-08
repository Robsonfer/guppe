"""
Len, Abs, Sum e Round

len() = Retorna o tamanho, ou seja, o número de itens de um iterável.
abs() = Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.

"""

print(' ---------- Exemplos de len() ---------- ')

# Exemplos de len():
print(len('Geek University'))
print(len([1, 2, 3, 4, 5])) # lista
print(len((1, 2, 3, 4, 5))) # tupla
print(len({1, 2, 3, 4, 5})) # set
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})) # dicionário
print(len(range(0, 10))) # range

# Por debaixo dos panos, quando utilizamos a função len(), o Python faz o seguinte:
print('Geek University'.__len__())
# Toda função Python que começa com dois underlines são chamadas de funções especiais Dunder!

print(' ---------- Exemplos de abs() ---------- ')

# Exemplos de abs():
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
# Não podemos utilizar abs() para strings. Não existe abs() de string!
