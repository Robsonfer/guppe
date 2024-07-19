"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

OS = Operation System (Sistema Operacional)
"""

# Fazer o import:
import os, platform
import sys


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
# print(os.name) # A resposta a esse print será posix para Linux e Mac e nt para Windows.


"""
Podemos ter mais detalhes no sistema operacional. Usamos o os.uname() para o posix, mas infelizmete tivemos que importar
outro módulo chamado platform para o windows. Desta forma usamos o platform.uname():

print(platform.uname())

print(sys.platform)
"""


# Como acessar diretórios dentro do Python:
# 'C:\Users\robsonfer\OneDrive - Armco do Brasil S.A\Perfil\Desktop\ROBSON\UDEMY\guppe\teste_geek'
# print(os.getcwd()) # C:\Users\robsonfer\OneDrive - Armco do Brasil S.A\Perfil\Desktop\ROBSON\UDEMY\guppe
# res = os.path.join(os.getcwd(), 'geek') # Comando para juntar geek no diretório (ol.path.join())
# os.chdir(res) # Comando para mudar o diretório
# print(os.getcwd()) # C:\Users\robsonfer\OneDrive - Armco do Brasil S.A\Perfil\Desktop\ROBSON\UDEMY\guppe\geek


# Se qusermos adicionar mais, basta colocar uma vírgua depois de 'geek' e somar o próximo diretório: 'geek', 'university'.
# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o diretório que será juntado ao atual.


# Podemos listar os arquios e diretórios com o listdir():
print(os.listdir())
print(f'Este diretório tem {len(os.listdir())} arquivos.')

# Podemos também listar colocando um diretório dentro do listdir():
print(os.listdir('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY'))

# Podemos obter mais detalhes do diretório:
scanner = os.scandir('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY')
print(scanner)

# E como podemos Temos um Iterator Object, podemos gerar uma lista disto:
arquivos = list(scanner)
print(arquivos)

# Vamos ver tudo o que é podems fazer com esta lista de arquivos:
print(dir(arquivos[0]))

print('------------------')

# Agora vamos testar algumas possibilidades com base na consulta acima:
print(arquivos[0].inode()) # retorna o identificador de node (nó)
print(arquivos[0].is_dir()) # retorna se é um diretório = True
print(arquivos[0].is_file()) # retorna se é um arquivo = False
print(arquivos[0].is_symlink()) # retorna se é um link simbólico = False
print(arquivos[0].name) # retorna o nome do arquivo
print(arquivos[0].path) # retorna o caminho até o arquivo
print(arquivos[0].stat()) # retornam as estatísticas desse arquivo/diretório

# OBS: Quando utilizamos a função scandir(), nós precisams fechá-la. Assim como quando abrimos um aquivo:
scanner.close()
