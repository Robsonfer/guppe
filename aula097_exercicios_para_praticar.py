"""
Exercício 1:
    Crie um programa que:
        a) Crie/abra um arquivo texto de nome "arq.txt";
        b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere "O";
        c) Feche o arquivo;
        d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados.
"""

import os

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
Exercício 2:
    Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.
"""



"""
Exercício 3:
    Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este arquivo possui.
"""
