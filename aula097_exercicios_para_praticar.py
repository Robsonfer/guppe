####################################################### EXERCÍCIO 1 #######################################################
"""
Exercício 1:
    Crie um programa que:
        a) Crie/abra um arquivo texto de nome "arq.txt";
        b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere "O";
        c) Feche o arquivo;
        d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

import os

# Minha solução:
"""
with open('arq.txt', 'a') as arquivo:
    while True:
        caractere = input('Digite o que quiser ou "O" para sair: ')
        if caractere != 'O':
            arquivo.write(caractere + '\n')
        else:
            break

with open('arq.txt') as arquivo:
    print(arquivo.read())
"""

# Solução do professor:
"""
with open('arq.txt', 'a') as arquivo:
    while True:
        caractere: str = input('Informe um caractere ou 0 para sair: ')
        if caractere != '0':
            arquivo.write(f'{caractere}\n')
        else:
            break

with open('arq.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    print(linha)
"""

####################################################### EXERCÍCIO 2 #######################################################
"""
Exercício 2:
    Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.
"""

# Minha solução:
"""
with open(input('Digite o nome de um arquivo de texto: ').lower() + '.txt') as arquivo:
    texto = arquivo.read()
    vogais = []
    consoantes = []
    for letras in texto:
        if letras in 'aeiouAEIOU':
            vogais += letras
        else:
            if letras in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                consoantes += letras
    print(f'Este arquivo tem {len(vogais)} vogais.')
    print(f'Este arquivo tem {len(consoantes)} consoantes.')
"""

#Solução do professor:
"""
vogais = 0
consoantes = 0
arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()

for linha in linhas:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1

if vogais > 0:
    print(f'Existe(m) {vogais} no arquivo.')
else:
    print(f'Não existe(m) vogais no arquivo!')

if consoantes > 0:
    print(f'Existe(m) {consoantes} no arquivo.')
else:
    print(f'Não existe(m) consoantes no arquivo!')
"""

####################################################### EXERCÍCIO 3 #######################################################
"""
Exercício 3:
    Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este arquivo possui.
"""

"""
with open(input('Digite o nome de um arquivo de texto: ').lower() + '.txt') as arquivo:
    texto = arquivo.readlines()
    print(f'Este texto contém {len(texto)} linhas.')
"""

# Solução do professor:
"""
arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()

print(f'Existe(m) {len(linhas)} linha(s) no arquivo.')
"""
