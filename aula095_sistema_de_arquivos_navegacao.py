"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.

OS = Operation System (Sistema Operacional)
"""

# Fazer o import:
import os


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
print(os.path.isabs('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe'))
# Por algum motivo, na hora de checar, o Python não reconhece \, só /
