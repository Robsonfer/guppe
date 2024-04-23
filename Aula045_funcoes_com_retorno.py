"""
Funções com retorno
"""

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'Retonro de print: {ret_pr}')

"""
No exemplo acima criamos uma lista com três números, depois uma variável pra receber a informação da função numeros.pop()
Quando imprimimos o retorno de pop, temos como resultado o número 3 que por sua vez é o retorno da função pop(), ou seja, esta função retorna não somente o valor que foi removido como também a lista com esse item a menos.
Também criamos uma variável que recebe o resultado de print() que é uma função que não retorna nada.
Ao imprimir essa variável fica muito claro que a função print() não retorna nada, pois o resultado dela é None.
"""

# Exemplo função
def quadrado_de_7():
    print(7*7)

ret = quadrado_de_7()

print(f'Retorno da função quadrado_de_7: {ret}')
# Veja que a função acima não retonar nada também, só imprimi. Imprimir (print), não é retornar!
# Em Python quando uma função não retorna nenhum valor, o retorno é None.

# Refatorando a função pra retornar o valor:
def quadrado_de_5():
    return 5*5

# Variável para receber o retorno da função.
retorno = quadrado_de_5()
print(f'Retorno da função quadrado_de_5: {retorno}')

"""
Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return!
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções ou mesmo para o print. Ver exemplo abaixo
"""
print(f'Retorno da função quadrado_de_5: {quadrado_de_5()}')

# Refatorando a primeira função (diz_oi()):
def diz_oi():
    return 'Oi'

print(f'Retorno da função diz_oi: {diz_oi()}')

# Inclusive podemos complementar assim:
alguem = 'Pedro'
print(diz_oi() + ' ' + alguem)
# Se não usar o return, não conseguiríamos fazer isso, pois não conseguimos somar None com string!

"""
OBSERVAÇÕES sobre a palavra reservada return:
    1 - Ela finaliza a função, ou seja, sai da execução da função;
    2 - Podemos ter diferentes returns em uma mesma função;
    3 - Pdemos retornar qualquer tipo de dado e até mesmo múltiplos valores em uma função.
"""

# Exemplo 1 (o return encerra a função):
def dizer_oi():
    print('Estou sendo executado antes do retorno.')
    return 'Oi!'
    print('Estou sendo executado após o retorno.')

print(dizer_oi())
# Veja que a linha do print nunca será executada. O return finaliza a função.

# Exemplo 2 (diferentes retuns na mesma função):
def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'B'

print(nova_funcao())
# Perceba que se variavel = True, retorna 4, mas se variavel = False, retorna B. O Python ignora o 3.2, pois o elif considera o None. Caso variavel = None, aí sim retornará 3.2!

# Exemplo 3 (diferentes tipos de dados e múltiplos valores):
def outra_funcao():
    return 2, 3, 4, 5

num2, num3, num4, num5 = outra_funcao()

print(num2, num3, num4, num5)
print(outra_funcao())
print(type(outra_funcao()))

# Vamos criar uma função que joga cara ou coroa!
from random import random

"""
def joga_moeda():
    # gera um número pseudo-randômico entre 0 e 1:
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())
"""

# Podemos melhorar a função acima refatorando-a tirando a variável:
def joga_moeda():
    # gera um número pseudo-randômico entre 0 e 1:
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Um dos erros comuns em relação à retorno de funções é usar o else desnecessariamente:
def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else:
        return False

print(eh_impar())

# Como só temos duas possibilidades, não é necessário colocar um else:
def eh_par():
    numero = 5
    if numero % 2 != 0:
        return False
    return True

print(eh_par())
