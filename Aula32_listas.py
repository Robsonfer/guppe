"""
Listas em Python funcionam como vetores/matrizes (arrays em outras linguagens). Com a diferença de serem dinâmicos e aceitarem qualquer tipo de dados.

Como funcionam os arrays em C ou Java por exemplo:

    - Possuem tamanho e tipo de dados fixos, ou seja, nestas linguagens se for criado um array do tipo int e tamanho 5, este array  será sempre do tipo inteiro e só poderá ter no máximo 5 valores.

Como funcionam em Python:

- Dinâmico:
    - Já em Python não possui tamanho fixo antecipadamente. Ou seja, podemos criar a lista e ir adicionando elementos.
Qualquer tipo de dados:
    - Não possuem tipos de dados fixo, podendo ser usado qualquer tipo de dados dentro de uma lista.

As listas em Python são representadas por colchetes: []
"""


print('------------------------------------------------------------------------')
print('Imprimindo as listas de modelo:')

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(lista1)

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(lista2)

lista3 = []
print(lista3)

lista4 = list(range(11))
print(lista4)

lista5 = list('Geek University')
print(lista5)


print('------------------------------------------------------------------------')
print('Checando os valores contidos nas listas:')

# Podemos checar valores contidos nas listas:
num = 18
if num in lista4:
    print(f'encontrei o número {num}')
else:
    print(f'não encontrei o número {num}')

print('------------------------------------------------------------------------')
print('Ordenando uma lista:')

# Podemos facilmente ordenar um lista:
lista1.sort()
print(lista1)

print('------------------------------------------------------------------------')
print('Contando o número de ocorrências de um elemento da lista:')
# Podemos facilmente contar o número de ocorrências de um valor em uma lista:
print(lista1.count(1))
print(lista5.count('e'))


print('------------------------------------------------------------------------')
print('Adicionando elementos em uma lista com append:')

# Podemos adicionar elementos em listas (append):
print(lista1)
lista1.append(42)
print(lista1)
# OBS: Com append nós só conseguimos adicionar um elemento por vez, caso contrário dá erro. Mas podemos acrescentar um outro elemento do tipo lista:
lista1.append([8, 3, 1])
print(lista1)
print('Provando que a lista adicionada é um elemento:')
# Essa lista vira um elemento dentro da lista1, veja que interessante:
if [8, 3, 1] in lista1:
    print('Encontrei a lista dentro da lista!')
else:
    print('Não encontrei a lista dentro da lista!')

print('------------------------------------------------------------------------')
print('Adicionando mais que um elemento em uma lista com extend:')

# Para adicionar mais que um elemento de uma vez na lista já existente nós utilizamos .extend():
print(lista1)
lista1.extend([123, 44, 67])
print(lista1)

print('------------------------------------------------------------------------')
print('Adicionando um item na lista em uma posição específica com o insert:')

# Como o append e o extend sempre inserem elementos no fim da lista, podemos utilizar o insert informando a posição que queremos:
lista1.insert(2, 'novo valor')
print(lista1)
# Note que o elemento é inserido, mas não substitui o anterior da posição, só empurra ele para a próxima posição.

print('------------------------------------------------------------------------')
print('Juntando duas listas com o operador soma criando uma terceira:')

# Também podemos facilmente juntar duas listas:
lista6 = lista1 + lista2
print(lista6)
print('Juntando duas listas com o extend:')
# O mesmo pode ser feito com extend, com a diferença que vc não cria uma nova lista, mas amplia uma já existente:
lista4.extend(lista5)
print(lista4)
print('Aumentando a lista1 com os itens da lista2 com o operador soma:')
# Ainda assim, o mesmo pode ser feito usando:
lista1 = lista1 + lista2
print(lista1)

# Renovando as listas para continuar com os exemplos com as listas na íntegra:
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

print('------------------------------------------------------------------------')
# Imprimindo a lista inversa:
lista1.reverse()
lista2.reverse()
print('Imprimindo a lista invertida com reverse:')
print(lista1)
print(lista2)

print('E podemos fazer de outra forma com slice:')
print(lista1[::-1])
print(lista2[::-1])

print('------------------------------------------------------------------------')
# Corrigindo as listas invertidas:
lista1.reverse()
lista2.reverse()

# Copiando uma lista:
print('Podemos copiar uma lista')
lista6 = lista2.copy()
print(lista6)

print('------------------------------------------------------------------------')
# Descobrindo o tamanho de uma lista:
print('Descobrindo o tamanho de uma lista com len:')
print(len(lista5))

print('------------------------------------------------------------------------')
# Removendo o último elemento de uma lista:
print('Removendo o último elemento de uma lista com pop:')
print(lista5)
lista5.pop()
print(lista5)
lista5.pop()
print(lista5)
# OBS: O pop não somente remove o último elemento, mas também o retorna.

# Ainda podemos remover um elemento pelo índice:
print('Removendo um ítem pelo índice:')
print(lista5)
lista5.pop(2)
print(lista5)
# Os elementos à direita deste índice serão todos deslocados para a esquerda.
# OBS: Se não houver elemento no índice informado, teremos um erro chamado IndexError

# Podemos ainda remover todos os elementos de uma lista:
print('Removendo todos os elementos de uma lista de uma só vez (zerar a lista):')
print(lista5)
lista5.clear()
print(lista5)

print('------------------------------------------------------------------------')
# Podemos multiplicar uma lista:
print('Multiplicando os itens de uma lista usando *:')
nova = [1, 2, 3]
nova *= 3
print(nova)

print('------------------------------------------------------------------------')
# Podemos facilmente converter uma string para uma lista:
print('Convertendo uma string para uma lista. Exemplo 1 (split):')
curso = 'Programação em Python Essencial'
print(curso)
curso = curso.split()
print(curso)
# Por padrão o split separa os elementos da lista pelo espaço entre elas.

print('Convertendo uma string para uma lista. Exemplo 2 (delimitando a divisão com vírgula):')
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em string:
print('Agora convertendo uma lista em string (Join):')
print(curso)
curso = ' '.join(curso)
print(curso)
# Basicamente o comando diz: Pegue a lista curso, coloque espaços entre cada elemento e transforme em uma string.
# Podemos fazer isso com outros caracteres além do espaço.

print('------------------------------------------------------------------------')
# Iterando sobre listas:

#Exemplo 1 Utilizando for:
print('Iterando sobre listas - Exemplo 1 (for):')
print(f'Lista1: {lista1}')
for elemento in lista1:
    print(elemento)

# Inclusive podemos fazer o seguinte para tornar a iteração dinâmica para um uso:
print('Inclusive podemos utilizar essa iteração fazendo uma soma:')
print(f'Os elementos da lista4 são: {lista4}')
soma = 0
for elemento in lista4:
    soma += elemento
print(f'A soma dos elentos da lista4 é: {soma}')
# Desde que respeitemos os tipos, podemos somar até mesmo strings, o que vai me gerar uma concatenação de caracteres gerando uma string única.

#Exemplo 2 Utilizando While:
print('Iterando sobre lsitas - Exemplo 2 (while):')
"""
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print(carrinho)
"""

print('------------------------------------------------------------------------')
print('Deixarei comentado o item de iteração com while, pois ele pede input!')
print('------------------------------------------------------------------------')

# Utilizando variáveis em listas:
print('Utilizando variáveis em listas:')
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

print('------------------------------------------------------------------------')
# Em listas fazemos o acesso aos elementos de forma indexada
print('Acessando os elementos da lista pelo índice:')
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazendo o acesso aos elementos de forma indexada inversa;
print('Fazendo o acesso aos elementos de forma indexada inversa:')
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
# para entender melhor o índice negativo, pense na lista como um círculo, onde o final de um elemento está ligado ao início da lista.

print('------------------------------------------------------------------------')
print('Imprimindo os itens da lista usando loop for:')
for cor in cores:
    print(cor)

print('Imprimindo os itens da lista usando loop while:')
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

print('------------------------------------------------------------------------')
print('Gerando índice em um loop for:')
for indice, cor in enumerate(cores):
    print(indice, cor)

print('------------------------------------------------------------------------')
# Relembrando que listas aceitam valores repetidos
print('Relembrando que listas aceitam repetição de valores:')
lista7 = []
lista7.append(42)
lista7.append(42)
lista7.append(33)
lista7.append(33)
lista7.append(42)
print(lista7)

print('------------------------------------------------------------------------')
# Outros métodos não tão importantes mas também úteis para se trabalhar com listas:
print('Encontrar o índice de um elemento na lista:')
numeros = [5, 6, 7, 5, 8, 9, 10]

print('Em qual índice da lista está o valor 6?')
print(numeros.index(6))

print('Em qual índice da lista está o valor 9?')
print(numeros.index(9))
# OBS: Caso não exista o elemento na lista, será apresentado um erro.

print('Se tivermos elementos repetidos ao pedir o índice, retorna o índice do primeiro elemento encontrado:')
print(numeros.index(5))

print('Podemos fazer a busca dentro de um range estabelecendo onde iniciar')
print(numeros.index(5, 2))
# Traduzindo, encontre o elemento 5 a partir do índice 2!

print('Podemos fazer a busca dentro de um range estabelecendo onde iniciar e onde terminar')
print(numeros.index(5, 2, 5))
# Traduzindo, encontre o elemento 5 a partir do índice 2 e pare no índice 5!

print('------------------------------------------------------------------------')
# Revisando Slicing:
# lista[início:fim:passo]
# range[início:fim:passo]

print('Trabalhando com slice de lista com o parâmetro início:')
lista8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(lista8[1:])

print('Trabalhando com slice Imprimindo todos os elementos(::):')
print(lista8[::])

print('Trabalhando com slice de lista com parâmetro início e fim:')
print(lista8[1:6])

print('Trabalhando com slice de lista só com parâmetro fim:')
print(lista8[:6])

print('Trabalhando com slice de lista com parâmetro início, fim e com passo de 2:')
print(lista8[1:8:2])

print('Trabalhando com slice de lista somente com passo de 2 e fim:')
print(lista8[:11:2])

print('Trabalhando com slice de lista com índice negativo:')
print(lista8[-3:]) # Lembre da lista como um círculo.

print('Trabalhando com slice de lista com parâmetro início, com passo de 2 até o final:')
print(lista8[1::2])

print('Trabalhando com slice de lista com parâmetro início, com passo de negativo:')
print(lista8[::-1]) # A lista acaba sendo invertida.

print('------------------------------------------------------------------------')
print('Invertendo valores em uma lista:')
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
print('Lembrando que para isso tbm podemos usar o reverse!')

print('------------------------------------------------------------------------')
# Realizar: Soma*, valor máximo*, valor mínimo* e tamanho de uma lista.
# * Somente se os valores forem todos inteiros ou reais.
print('Econtrando soma, máximo, mínimo e tamanho de uma lista:')
lista9 = [1, 2, 3, 4, 5, 6]
print(f'Eis a lista9: {lista9}')
print(sum(lista9))
print(max(lista9))
print(min(lista9))
print(len(lista9))

print('------------------------------------------------------------------------')
print('Transformando uma lista em tupla:')
print(lista9)
print(type(lista9))
tupla = tuple(lista9)
print(tupla)
print(type(tupla))

print('------------------------------------------------------------------------')
# Desempacotamento de lista:
print('Desempacotamento de listas:')
lista10 = [1, 2, 3]
n1, n2, n3 = lista10
print(n1)
print(n2)
print(n3)
# Se a quantidade de elementos for diferente da quantidade de dados o Python apontará um erro!

print('------------------------------------------------------------------------')
