"""
Sistema de Arquivos - Manipulação


# Descobrindo se um arquivo ou diretório existe:

# Arquivos
print(os.path.exists('arquivo.txt'))              # Retorno: False
print(os.path.exists('frutas.txt'))               # Retonro: True

# Diretórios:

# Paths relativos:
print(os.path.exists('geek'))                     # Retorno: True
print(os.path.exists('geek/university'))          # Retorno: True
print(os.path.exists('outro'))                    # Retorno: True
print(os.path.exists('geek/university/geek3.py')) # Retorno: True


# Paths absolutos:
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university')) # Retorno: True
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/university'))      # Retorno: False
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university/geek4.py')) # Retorno: True


# Criando arquivos:

# Forma 1:
open('arquivo_teste.txt', 'w').close()

# Forma 2:
open('arquivo_teste2.txt', 'w').close()

# Forma 3:
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass
# Esse pass serve somente para que seja obedecida a indentação, pois ':' abre um bloco de código.
Com o with o arquivo fecha ao final do bloco.

# Melhor forma de criar arquivos, mas que não funciona no Windows:
os.mknod('arquivo-teste4.txt')
os.mknod('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university.txt')

OBSERVAÇÃO IMPORTANTE: Este comando mknod() NÃO FUNCIONA NO WINDOWS!
Para Windows use sempre uma das formas entre 1 e 3 mencionados acima

OBS: Criando um arquivo via mknod(), se o arquivo já existir, teremos o erro FileExistisError.
Mas sabemos como tratar erros.


# Criando diretórios:

# Path Relativo
try:
    os.mkdir('templates')
except FileExistsError:
    print('ATENÇÃO, ESTE DIRETÓRIO JÁ EXISTE, TENTE OUTRO NOME OU CAMINHO!')
# Esse diretório será criado onde o Python está a ser executado. E caso já exista, teremos um FileExistsError.
# Mas já tratamos com try/except o exemplo acima.

# Path Absoluto:
try:
    os.mkdir('C:/Users/robso/PycharmProjects/guppe/geek/templates')
except FileExistsError:
    print('ATENÇÃO, ESTE DIRETÓRIO JÁ EXISTE, TENTE OUTRO NOME OU CAMINHO!')

# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError


"""

import os

