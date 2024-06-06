"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas!
A função reverse() só funciona com listas, enquanto a função reversed() funciona com qualquer iterável.
Sua função é reverter o iterável.
Ela retorna um iterável chamado List_reverseiterator.
"""

# Exemplo 1:
lista = [1, 2, 3, 4, 5]
result = reversed(lista)
print(result)
print(type(result))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto!
# Lista:
print(list(reversed(lista)))
# Tupla:
print(tuple(reversed(lista)))
# Conjunto:
print(set(reversed(lista)))
# Importante lembrar que o set não definimos a ordem!

# Podemos iterar sobre o reversed:
for letra in reversed('Geek University'):
    print(letra, end='')
# Usamos o end='' para tirar a quebra de linha e imprimir tudo na mesma linha.
print('\n') # E como não pulamos uma linha, nós precisamos forçar essa linha agora com '\n'

# Podemos fazer o mesmo sem o uso do for:
print(''.join(list(reversed('Geek University'))))
# Usamos o .join() para transformar a lista de strings em uma string novamente.

# Mas também já vimos como fazer isso mais fácil com slice de strings:
print('Geek University'[::-1])

# Podemos também utilizar o reversed para fazer um loop for reverse:
for n in reversed(range(0, 10)):
    print(n)

# Mas também já vimos como fazer isso utilizando o próprio range():
for n in range(9, -1, -1):
    print(n)
