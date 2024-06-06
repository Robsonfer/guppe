"""
Recebendo dados do usuário
"""

# Entrada de dados:
nome = input('Qual é o seu nome? ')

# Saída de dados. Exemplos com prints antigos:

# print('Seja bem vindo(a) %s' % nome)
# print('Qual é a sua idade?')
# idade = input()
# print('%s anos é uma ótima idade' % idade, nome)

# Saída e saída de dados. Exemplo com prints modernos:

# print('Seja bem vindo(a) {0}' .format(nome))
# print('Qual é a sua idade?')
# idade = input()
# print('Que legal {0}, {1} anos é uma ótima idade!' .format(nome, idade))

# Saída e saída de dados. Exemplo com prints atuais:
print(f'Seja bem vindo(a) {nome}')
idade = int(input('Qual é a sua idade? '))
print(f'Que legal {nome}, {idade} anos é uma ótima idade!')
ano = 2023 - idade #Cast - conversão de um tipo de dado para outro
print(f'Você nasceu em {ano}. Este foi um ano incrível!')
