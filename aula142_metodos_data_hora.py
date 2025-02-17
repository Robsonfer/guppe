"""
Aula 142 - Métodos de datas e horas
"""

import datetime

print('---------- Imprimindo método now() ----------')

# Com now() podemos especificar um timezone (Fuzo Horário)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

# Com today() não conseguimos especificar um timezone!
print('---------- Imprimindo método today() ----------')
hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo à meia-noite - combine():
# Suponha que precisemos fazer algo automático à meia-noite de amanhã

print('---------- Imprimindo método combine() ----------')
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
# datetime.time() vazio como usamos, vai setar as horas, minutos e segundos como zero!
# datetime.datetime.combine() vai combinar duas propriedades datetime.
print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# Encontrar o dia da semana - weekday()
# Os dias da semana do método weekday() começam em zero, sendo esta a segunda-feira

"""
0 - Monday
1 - Tuesday
2 - Wednesday
3 - Thursday
4 - Friday
5 - Saturday
6 - Sunday
"""

print('---------- Imprimindo método weekday() ----------')
nascimento = datetime.date(1980, 9, 17)
print(nascimento.weekday())

"""
# Recebendo a data de aniversário e trabalhando o método weekday():

print('---------- Personalizando aniversário com o método weekday() ----------')
aniversario = input('Qual é a sua data de nascimento? Por favor, use dd/mm/yyyy: ')

aniversario = aniversario.split('/') # Criando uma lista e separando por "/" itens da lista
print(aniversario)

# Organizando os itens pela ordem de data no formato americano:
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
print(aniversario)

# Tratando os dias da semana de número para nomes:
if aniversario.weekday() == 0:
    print('Você nasceu em uma Segunda-Feira!')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-Feira!')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quarta-Feira!')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-Feira!')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-Feira!')
elif aniversario.weekday() == 5:
    print('Você nasceu em um Sábado!')
else:
    print('Você nasceu em um Domingo!')
"""

# Formatando datas/horas com strftime() - String Format Time:
# dd/mm/yyyy hora:minuto

print('-------- Formatando com método strftime() --------')
hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')  # usar %Y, o resultado será 4 dígitos para o ano!
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%m/%y')  # se usar %y, o resultado será somente com 2 dígitos para o ano!
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%B/%Y')  # se usar %B, o resultado será com o nome do mês!
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%b/%Y')  # se usar %b, o resultado será com o nome do mês, porém abreviado!
print(hoje_formatado)

# Mas podemos trabalhar essas datas de uma forma melhor:

print('-------- Data no formato pt-BR --------')


# Sem a bibilioteca textblob:


def formata_data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'
    elif data.month == 6:
        return f'{data.day} de Junho de {data.year}'
    elif data.month == 7:
        return f'{data.day} de Julho de {data.year}'
    elif data.month == 8:
        return f'{data.day} de Agosto de {data.year}'
    elif data.month == 9:
        return f'{data.day} de Setembro de {data.year}'
    elif data.month == 10:
        return f'{data.day} de Outubro de {data.year}'
    elif data.month == 11:
        return f'{data.day} de Novembro de {data.year}'
    else:
        return f'{data.day} de Dezembro de {data.year}'


print(formata_data(hoje))

# Com a biblioteca deep-translator:


print('-------- Data no formato pt-BR com deep_translator --------')

"""
from deep_translator import GoogleTranslator


def formatar_data(data):
    return f"{data.day} de {GoogleTranslator(source='auto', target='pt').translate(data.strftime('%B')).title()} de {data.year}"


hoje = datetime.datetime.today()
print(formatar_data(hoje))
"""

print('-------- Por algum motivo no VS Code não funciona o deep_translator --------')

# Convertendo uma string em um objeto do tipo datetime
# strftime -> string format time
# strptime -> string parameter time

print('-------- string para o formato datetime com strptime --------')

"""
nascimento2 = datetime.datetime.strptime('17/09/1980', '%d/%m/%Y')

print(nascimento2)

print('-------- Recebendo a data do usuário --------')

nascimento2 = input('Qual sua data de nascimento? Favor usar o formato dd/mm/aaaa: ')
nascimento2 = datetime.datetime.strptime(nascimento2, '%d/%m/%Y')

print(nascimento2)
"""

# Trabalhando somente com a hora:

print('-------- Trabalhando somente com a hora --------')
almoco = datetime.time(12, 30, 0)
print(almoco)

print('-------- Marcando tempo de execução com timeit --------')

# Marcando o tempo de execução do nosso código com timeit:

import timeit

# Loop For:
tempo_for = timeit.timeit('"_".join(str(n) for n in range(100))', number=10000)
print(tempo_for)

# List Comprehension:

tempo_comp = timeit.timeit('"_".join([str(n) for n in range(100)])', number=10000)
print(tempo_comp)

# Map:

tempo_map = timeit.timeit('"_".join(map(str, range(100)))', number=10000)
print(tempo_map)

import functools

# Marcando o tempo de execução do nosso código com timeit, functools e partial:
print('-------- Marcando tempo de execução com timeit, functools e partial --------')


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
# Esse partial recebe o nome da função que vamos executar e o parâmetro da função: (teste, 2)
