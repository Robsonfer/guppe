"""
Entendendo o *args

O *args é um parâmetro como outrou qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que começo com o asterisco.
Mas por convenção ficou decidido adotar o nome *args para definí-lo.

Mas afinal, o que é o *args?
    - O parâmetro *args utilizado em uma função coloca os valores extras informados como entrada em uma tupla.
    Importante: Lembre-se que as tuplas são imutáveis
"""

# Exemplo:
def soma_todos_numeros(num1=0, num2=0, num3=0):
    return num1 + num2 + num3
print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
# print(soma_todos_numeros(4, 6, 9, 4)) # TypeError
"""
No caso da função acima, se passarmos menos argumentos ou mais argumentos do que o padrão da função, teremos um TypeError!

Ainda que colocássemos valores padrão para todos os parâmetros no âmbito de cessar o erro (feito depois para representar o segundo print), no caso de informar mais argumentos ainda teríamos o mesmo erro.

Uma forma de corrigir esse erro seria adicionar mais um parâmetro à função, mas e se em outro momento eu quiser colocar cinco ou mais argumentos? Depender sempre de adicionar um novo parâmetro pra cobrir a entrada de um novo argumento não está correto.
"""

# Entendendo o *args:
def somar_numeros(nome, email, *args):
    return sum(args)

print(somar_numeros('Robson', 'robsonnfer'))
print(somar_numeros('Robson', 'robsonnfer', 1))
print(somar_numeros('Robson', 'robsonnfer', 1, 2))
print(somar_numeros('Robson', 'robsonnfer', 1, 2, 3))
print(somar_numeros('Robson', 'robsonnfer', 1, 2, 3, 4))
"""
IMPORTANTE: Tomar cuidado com o tipo de argumentos a serem inputados, pois sabemos que não podemos somar uma string com um number, por exemplo!

Uma função não precisa ter somente o *args, podemos acrescentar mais parâmetros na função, mas os demais são obrigatórios. Vamos acrescentar em nossa função acima!
"""

# Outro exemplo de utilização do *args:
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    return 'Desculpe, mas não sei quem você é!'
print(verifica_info('Robson'))
print(verifica_info('Geek'))
print(verifica_info('University'))
print(verifica_info('Geek', 'University'))
print(verifica_info('University', 'Geek'))

# Se tentarmos usar uma lista como argumento da função abaixo teremos um TypeError
# Uma forma de resolver esse problema é usando um desempacotador usando *numeros como argumento
def soma_numeros(*args):
    print(args)
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_numeros(*numeros))
"""
O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados. Desta forma ele saberá que precisará antes desempacotar estes dados.
"""
