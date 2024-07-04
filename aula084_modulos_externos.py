"""
Módulos Externos

Utilizamos o gerenciado rde pacotes Python chamado pip (Python Installer Package

E como saber quais pacotes existem para o Python?
Basta acessar o site: https://pypi.org

Na aula instalamos o pacote chamado colorama.
Colorama -> É utilizado para permitir impressão de textos coloridos no terminal.
"""

# Fazer os passos abaixo seguindo as instruções do site
from colorama import init
init()

from colorama import (
    Fore,
    Back,
    Style
)

print(Fore.RED + 'some red text')
print(Back.LIGHTWHITE_EX + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
