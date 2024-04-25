"""
Entendendo **kwargs

Poderíamos chamar esse parâmetro de ** qualquer coisa, mas por convenção utiliza-se **kwargs

Este é só mais um parâmetro, mas diferente do args que coloca os valores extras em uma tupla, o **kwargs exite a utilização de parâmetros nomeados e transforma estes parâmetros extras em um dicionário.
"""

# Exemplo 1:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorida de {pessoa.title()} é {cor}')
    
cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()
cores_favoritas(geek='vermelho')

# Exemplo 2:
def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não sei quem é você!'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

"""
Em nossas funções podemos ter (NESTA ORDEM):
    1 parâmetros obrigatórios;
    2 *args;
    3 parâmetros default (não obrigatórios);
    4 **kwargs;
"""

# Exemplo:
def minha_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao('Robson', 43)
minha_funcao('Júlia', 8, 4, 5, 3, solteiro=True)
minha_funcao('Felipe', 34, eu='Não', você='Vai')
minha_funcao('Carla', 19, 9, 4, 3, Java=False, Python=True)

# Entenda por que é tão importante manter a ordem dos parâmetros na declaração:

# Função com a ordem correta dos parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Função com a ordem incorreta dos parâmetros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
# Veja que temos um desencontro de informações entre o args o instrutor!

# PAREI EM 30:30 !!!