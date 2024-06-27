"""
Try / Except / Else / Finaly

Dicas de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR o seu sistema.
"""

# O Else é executado somente se não entrar no except:
num = 0
"""
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('ATENÇÃO! Você digitou um texto, tente novamente no formato numérico, por favor.')
else:
    print(f'Você digitou o número: {num}')
"""

# Finaly

"""
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('ATENÇÃO! Você não digitou um valor válido.')
else:
    print(f'Você digitou o número: {num}')
finally:
    print('Executando o finally')
"""

"""
OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não!
O finally geralmente é utilizado para fechar ou desalocar recursos. Exemplo, encerrar um banco de dados ou fechar um arquivo que foi aberto para leitura ou escrita.
"""

# Exemplo mais complexo Errado:

"""
def dividir(a, b):
    return a / b

try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('ATENÇÃO! O valor precisa ser numérico!')

try:
    print(dividir(num1, num2))
except NameError:
    print('ATENÇÃO! O valor precisa ser numérico!')
"""


# Exemplo mais complexo Correto:

# OBS: Você é responsável pelas entradas das suas funções, então trate-as.

"""
def dividir(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        return 'ATENÇÃO! Valor incorreto. Tente um valor numérico.'
    except ZeroDivisionError:
        return  'ATENÇÃO! Não existe divisão por zero. Tente novamente.'

num1 = (input('Informe o primeiro número: '))
num2 = (input('Informe o segundo número: '))

print(dividir(num1, num2))
"""


"""
Da mesma forma que os erros são tratados de maneira específica no caso acima, podemos também tratar de forma genérica.
É sempre melhor tratar os erros de forma específica, pois ajuda muito mais o usuário em relação ao erro.
Mas como vamos mostrar abaixo, podemos tratar de maneira semi genérica:
"""

# Forma semi-genérica de tratar os erros:
def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'WARNING! {err}.'

num1 = (input('Informe o primeiro número: '))
num2 = (input('Informe o segundo número: '))

print(dividir(num1, num2))
