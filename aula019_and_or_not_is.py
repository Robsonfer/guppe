"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - nota, is
Operadores binários:
    - and, or

Para o 'and' ambos os valores precisam ser True;
Para o 'or' apenas um dos valores precisa ser True;
Para o 'not' o valor booleano é invertido;
Para o 'is' um valor é comparado com outro. Exemplo: 1 == 1 funciona com 1 is 1
"""

ativo = True
logado = False

# Operador and:
if ativo and logado:
    print('Usuário ativo no sistema')
else:
    print('Você precisa ativar usa conta. Por favor, cheque seu e-mail.')

# Operador or:
if ativo or logado:
    print('Bem vindo usuário.')
else:
    print('Você precisa ativar usa conta. Por favor, cheque seu e-mail.')

# Operador not:
if not ativo:
    print('Você precisa ativar usa conta. Por favor, cheque seu e-mail.')
else:
    print('Bem vindo usuário.')

# Operador is:
if ativo is True: # Funciona, mas é redundante.
    print('Bem vindo usuário.')
else:
    print('Você precisa ativar usa conta. Por favor, cheque seu e-mail.')

"""
Mas o is pode ser usado de várias formas. Se der um dir(variável), podemos ver várias formas de usar o is,
como por exemplo variável.istitle() ele vai retornar True ou False.
"""
