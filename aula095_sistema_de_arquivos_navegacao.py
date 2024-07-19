"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

OS = Operation System (Sistema Operacional)
"""

# Fazer o import:
import os, platform


# getcwd() - pegar o current work directory - diretório de trabalho corrente
"""
print(os.getcwd())
# retorna o Path absoluto
"""

# Para mudar o diretório, podemos usar o chdir():
"""
os.chdir('..') # E usando '..', nós descemos um nível no diretório sentido ao diretório raíz
print(os.getcwd())

os.chdir('..') # E assim vamos até chegar no diretório raíz. Chegando no raíz, não importa o que façamos, ficamos nele.
print(os.getcwd())
"""

# Podemos checar se um diretório é absoluto ou relativo:

# print(os.path.isabs('C:/Users/robso/PycharmProjects/guppe'))
# OBS: Por algum motivo, na hora de checar, o Python não reconhece \, só /

"""
OBS PARA USUÁRIOS WINDOWS:
    Se você estiver utilizando um computador com Windows, deverá ter cuidado ao verificar diretórios.
"""

# Ou seja, para usar a barra invertida, é preciso usar duas barras, uma barra normal e uma de scape:
# print(os.path.isabs('C:\\Users\\robso\\PycharmProjects\\guppe'))

# Podemos também identificar qual é o SO com módulo OS:
print(os.name) # A resposta a esse print será posix para Linux e Mac e nt para Windows.

"""
Podemos ter mais detalhes no sistema operacional, mas infelizmente usamos o os para o posix e tivemos que importar
outro módulo chamado platform para o windows
"""
print(platform.uname())
