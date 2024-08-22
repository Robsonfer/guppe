#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Decoradores (Decorators)

O que são decorators?
    - São funções;
    - Envolvem outras funções e aprimoram os seus comportamentos;
    - Decorators tem uma sitaxe própria usando "@". Não é obrigatório, mas é considerado Syntact Sugar.

-----------------------------------------
           FUNCTION DECORATOR
-----------------------------------------


-----------------------------------------
-----------------------------------------
          DECORATED FUNCTION
-----------------------------------------
-----------------------------------------

OBS: Pense em decorador como decorar uma casa. É como se a função comum fosse o quadro e a função decoradora
fosse a moldura do quadro. Ela tem o objetivo de conter a função comum dentro de si e melhorá-la em termos
de funcionalidade e comportamentos.
"""


# Exemplo 1 - Decorators como funções (Sintaxe não recomendada / Sem Syntax Sugar):

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem vindo à Geek University')


# Testando 1:

teste = seja_educado(saudacao)

teste()

print('\n----- separando -----\n')


# Testando 2:

def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()

print('\n----- separando -----\n')


# Exemplo 2 - Decorators com Syntax Sugar (recomendado):

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando 1:

apresentando()

print('\n----- separando -----\n')


# Testando 2:

@seja_educado_mesmo
def dormir():
    print('Quero dormir!')


dormir()

print('\n----- separando -----\n')


# Um exemplo para ser usado na Programação Web

"""
Imagine um site como o seguinte menu de cabeçalho:

+----------------+----------------+----------------+-------------------+
|      Home      |    Serviços    |    Produtos    |   Adminstrativo   |
+----------------+----------------+----------------+-------------------+

Você quer que o acesso do site se dê da seguinte forma:

https://www.suaempresa.com.br/home -> Acesso livre para qualquer usuário à pagina home
https://www.suaempresa.com.br/servicos -> Acesso livre para qualquer usuário à página serviços
https://www.suaempresa.com.br/produtos -> Acesso livre para qualquer usuário à página produtos
https://www.suaempresa.com.br/admin -> Acesso restrito somente para usuários logados

OBS: O exemplo abaixo não é um código funcional. É apenas um exemplo para elucidar como funcionaria:

def checa_login():
    if not request.usuario:
        redirect('https://www.suaempresa.com.br/login')


def checa_home(request):
    return 'Pode acessar home'


def servicos(request):
    return 'Pode acessar servicos'


def produtos(request):
    return 'Pode acessar produtos'


@checa_login
def admin(request):
    return 'Pode acessar admin'

"""

# OBS: Não confunda Decorator com Decorator Function!
