"""
Debugando códigos com PDB (Python Debugger).

Bug -> Inseto

Comandos básicos do PDB
l -> para listar onde estamos no código
n -> próxima linha
p -> imprime variável
c -> continua a execução - finaliza o debugging
"""

# Alguns programadores usam print para debuggar códigos, entretanto essa é uma prática ruim:

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'WARNING! {err}.'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug, utilizando o debugger.
# Em Python podemos fazer isso em diferentes IDEs como o Pycharm ou utilizando o PDB - Python Debugger.

# Exemplo com o Pycharm:

def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'WARNING! {err}.'

print(dividir(4, 0))

# Exemplo 1 com o PDB - Python Debugger:

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace():

"""
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# Exemplo 2 com o PDB - Python Debugger:
"""
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

"""
Porque utilizar este formato?

O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início do arquivo.
Por isso, ao invés de colocar o import do pdb no início do arquivo, nós colocamos somente onde vamos debuggar.
Assim ao finalizar já fazemos a remoção do pdb. 
"""

# Exemplo 3 com o PDB - Python Debugger - breakpoint():
"""
A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como
função built-in (integrada) chamada breakpoint(). Então fazemos assim:
"""

"""
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb. Exmplo:

def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 3, 5, 7))

"""
Neste caso, as variáveis têm o mesmo nome dos comandos e toda vez que chamamos uma variável, na verdade damos um
comando do pdb. A única forma de ver uma variável nesse caso é usando o comando p (imprime variável) seguido da
variável. Exemplo: p l ou p n. 
"""
