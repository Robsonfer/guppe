"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código prevenindo assim que
o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //o que deve ser feito em caso de problema



"""

# Exmeplo 1 - Tratando um erro genérico:
try:
    geek()
except:
    print('Ops, parece que tivemos algum problema!')
# Traduzindo: Tente executar a função geek(), caso encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro genérico:
try:
    len(5)
except:
    print('Ops, parece que tivemos algum problema!')
"""
OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é sempre tratar de
forma específica.
"""

# Exemplo 3 - Tratando um erro específico:
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente!')
# Se eu não tratar o erro correto, vai estourar o erro correto na tela e o try/except não vai servir de nada!

# Exemplo 4 - Tratando um erro específico:
try:
    len(5)
except TypeError as err:
    print('Você está utilizando a função len() com o tipo incorreto!')

# Exemplo 5 - Tratando um erro específico com detalhes do erro:
try:
    geek()
except NameError as err:
    print(f'ATENÇÃO! A aplicação gerou o seguinte erro: {err}')

# Exemplo 6 - Tratando um erro específico detalhes do erro:
try:
    len(5)
except TypeError as err:
    print(f'ATENÇÃO! A aplicação gerou o seguinte erro: {err}')

# Exemplo 7 - Diversos tratamentos de erros de uma vez:
try:
    #len(5)
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')

# Exemplo 8 - Diversos tratamentos de erros de uma vez com um genérico para garantir no caso de um erro desconhecido:
try:
    len('geek'[9])
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente!')

# Exemplo 9 - Testando com o erro genérico antes de todos para saber se o Python identifica o erro certo:
try:
    geek()
except:
    print('Deu um erro diferente!')
"""
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
"""
# Com o except genérico, os demais são tratados como erros!

# Exemplo 10:
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic, 'game')) # Erro: chave: 'game' não existe.
print(pega_valor(7, 'nome')) # Erro: dicionario: 7 não existe.
