""""
Loop -> Estrutura de repetição
For -> Uma dessas estruturas

Em Python:

for item in iteravel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis

Exemplos de iteráveis:
 - String
    nome = 'Robson Ferreira'
 - Lista
    lista = [1, 3, 5, 7, 9]
 - Range
    numeros - range(1, 10)
"""

nome = 'Geek university'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de iteração sobre uma string:

for letra in nome:
    print(letra)

print('---------')

# Exemplo de iteração sobre uma lista:

for numero in lista:
    print(numero)

print('---------')

# Exemplo de iteração sobre um Range:

for numero in range(1, 10):
    print(numero)
# OBS: O valor final não é inclusive

print('---------')

print(nome[0], nome[5])

print('---------')

for indice, letra in enumerate(nome):
    print(nome[indice])
# O enumarate cria um índice para cada letra da string. O que é estranho pq toda string já tem isso default

print('---------')

for indice, letra in enumerate(nome):
    print(letra)

print('---------')

for _, letra in enumerate(nome):
    print(letra)
# Usando o underline conforme acima, eu descarto o valor. Neste caso o índice

print('---------')

for valor in enumerate(nome):
    print(valor)
"""
Isso imprime o índice e a letra logo em seguida. Se usar valor[0], ele imprime só o índice, se usar valor[1]
ele imprime só a letra. Então o valor é composto pelo índice e letra, mas podemos pegar parcial.
"""
print('---------')
print('Exemplo de loop para input:')

# Um exemplo bem legal da utilização do loop for:
qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma += num
print(f'A soma é {soma}')

print('---------')
print('Exemplo de como rodar tudo na mesma linha:')
# Como imprimir tudo na mesma linha:
for letra in nome:
    print(letra, end='')

print('---------')

print('imprimindo emoticons:')
# Original: U+1F60D
# Modificado: U0001F60D

emoji = '\U0001F601'

for _ in range(3):
    for num in range(1, 11):
        print(f'{emoji * num}')
