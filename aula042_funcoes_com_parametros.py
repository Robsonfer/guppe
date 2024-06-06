"""
Funções com Parâmetros de Entrada

- Funções que recebem dados para serem processados dentro da mesma.

Pensando em um programa qualquer, geralmente temos:
    Entrada -> Processamento -> Saída

Pensando em uma função, já sabemos que temos funções que:
    - Não possuem entrada;
    - Não possuem saída;
    - Possuem entrada, mas não possuem saída;
    - Não possuem entrada, mas possuem saída;
    - Possuem entrada e saída.
"""

# Refaturando a função quadrado_de_7():
def quadrado_de_7():
    return 7*7

print(quadrado_de_7())

# Refatorando ela fica assim:
def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# Ou podemos usar uma variável para pegar o retorno:
ret = quadrado(6)
print(ret)

# Outra forma de se fazer isso seria:
def quadrado2(num):
    return num ** 2

print(quadrado2(5))
print(quadrado2(6))

print('----')
# Refaturando a função cantar_parabens():
def cantar_parabens(aniversariante):
    print('Parabens pra você,')
    print('Nesta data querida,')
    print('Muitas felicidades,')
    print('Muitos anos de vida.')
    print(f'Viva {aniversariante}')

cantar_parabens('Robson')
print('---')
cantar_parabens('Rosângela')

# Funções podem ter n parâmetros de entrada, ou seja, podemos ter quantos parâmetros forem necessários

# Exemplos:

def soma(a, b):
    return a + b

def multiplica(c, d):
    return c * d

def outra(e, f, g):
    return (e + f) * g

print(soma(380, 720))
print(multiplica(32, 8))
print(outra(3, 2, 'Python '))

"""
OBSERVAÇÕES IMPORTANTES:

Quando passasmos a letra "a" na definição da função, estamos definindo um parâmetro.
quando passamos o número 380 na chamada da funções, estamos definindo um argumento.
Dessa forma estamos passando o argumento 380 para o parâmetro "a".

Portanto, se informarmos um número errado de parâmetros ou argumentos,teremos TypeError
"""

# Nomeando parâmetros:
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

"""
A diferença entre Parâmetros e Argumentos:
    - Parâmetros são variáveis declaradas na definição de uma função;
    - Argumentos são dados passados durante a execução de uma função;
"""

# A ordem dos parâmetros importa - Exemplo:
nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome))

"""
Argumentos Nomeados ou Keyword Arguments:
    Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.
"""
print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))
print(nome_completo(sobrenome='Jolie', nome='Angelina'))
# Ao especificar, podemos colocar na ordem que quisermos que será identificado corretamente na função.

# Outro erro comum na utilização do return:
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))
# Erro: Se finalizar no bloco do if, o retorno será 1, o correto é retornar no bloco do for.
# Se a função termina no return, o for não vai iterar todos os números, pois termina no primeiro do if.
