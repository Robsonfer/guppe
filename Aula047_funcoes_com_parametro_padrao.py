"""
Funções com parâmetro padrão (Default Parameters)
    - Funções onde a passagem de parâmetro seja opcional.
"""

# Exemplo onde a passagem de parâmetro é opcional:
print('Geek University')
print()

# Exemplo onde a passagem de parâmetro é obrigatório:
def quadrado(numero):
    return numero ** 2
print(quadrado(3))

def exponencial(numero, potencia=2):
    return numero ** potencia
print(exponencial(2, 3))
print(exponencial(3, 2))
print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5)) # Eleva à potência informada pelo usuário
"""
Ao colocar potencia=2 estamos definindo o 2 como parâmetro padrão. Se o usuário passar só um argumento, a função vai usar o parâmetro padrão, entretanto se o usuário passar dois argumentos, a função vai usar o parâmetro determinado pelo usuário.

Podemos usar inclusive para todos os parâmetros da função

OBS: Em funções Python, os parâmetros com valores default (padrão), DEVEM SEMPRE estar ao final da declaração.
"""

# Outros exemplos:
def soma(num1=0, num2=0):
    return num1 + num2
print(soma(4,3))
print(soma(4))
print(soma())

# Exemplo mais complexo:
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'
print(mostra_informacao('Geek', True))
print(mostra_informacao('Geek', False))
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))

"""
Por quê utilizar parâmetros com valor default?
    - Permite maior flexibilidade nas funções;
    - Evita erros com parâmetros incorretos;
    - Permite trabalhar com exemplos mais legíveis de código.

Quais tipos de dados podemos utilizar como valores de parâmetros default?
    - Qualquer tipo de dado pode ser utilizado, inclusive funções.
"""

# Exemplos de funções como parâmetros:
def soma2(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2
# Criamos duas funções simples: soma e subtração

def mat(num1, num2, fun=soma2):
    return fun(num1, num2)

print(mat(2, 3))
print(mat(2, 2, subtracao))
# Nesta função definimos dois parâmetros obrigatórios e um opcional recebendo a função soma.
# Neste caso se o usuário informar uma outra função, ele vai aceitar.

# Parei aos 29:30 da aula, iniciando o assunto escopo!
