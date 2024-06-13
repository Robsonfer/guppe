"""
Len, Abs, Sum e Round

len() = Retorna o tamanho, ou seja, o número de itens de um iterável.
abs() = Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
sum() = Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma total dos elementos, incluindo o valor inicial. OBS: O valor inicial default é 0!
round() = Retorna um número arredondado para n dígitos d eprecisão após a cada decimal. Se a precisão não for informada, retorna o inteiro mais próximo da entrada.
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

print(' ---------- Exemplos de sum() ---------- ')

# Sem valor inicial declarado:
print(sum([1, 2, 3, 4, 5]))
# Nesse caso ele soma toda a lista resultando 15.

# Com valor inicial declarado:
print(sum([1, 2, 3, 4, 5], 5))
# Nesse caso ele inicia com 5 e depois soma a lista toda resultando 20.
# Imagine que a lista são os itens de um carrinho de compras e o valor inicial é o frete!

# Podemos usar o sum:

# Em listas:
print(sum([3.145, 5.678]))

# Em tuplas:
print(sum((1, 2, 3, 4, 5)))

# Em sets(conjuntos):
print(sum({1, 2, 3, 4, 5}))

# Em Didicionários:
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
# Nunca esquecer que ao somar valores de dicionários temos que usar o .values()!
# OBS IMPORTANTE: O sum() não funciona com strings. Para isso usamos o join()

print(' ---------- Exemplos de round() ---------- ')

print(round(10.2))
print(round(10.5))
print(round(10.51))
print(round(10.6))
print(round(1.212121212121, 2))
print(round(1.219999999999, 2))
