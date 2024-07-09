"""
Módulos Externos

Utilizamos o gerenciador de pacotes python chamado pip - Python Installer Package

Como eu consigo saber quais pacotes existem para Python?
    Você pode acessar o site: https://pypi.org

colorama: É utilizado para permitir impressão de textos coloridos no terminal.
"""

# Utilizando o pacote externo colorama após instalado:
from colorama import init
init()

from colorama import (
    Fore,
    Back,
    Style
)

print(Fore.RED + 'Geek University')
print(Fore.MAGENTA + 'Geek University')
print(Fore.GREEN + 'Geek University')
print(Fore.YELLOW + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Back.LIGHTWHITE_EX + 'Colocando um background branco!')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL + 'Resetando tudo')
print('Agora, tudo de volta ao normal')
