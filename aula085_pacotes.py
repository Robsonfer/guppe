"""
Pacotes

Módulo = É apena um arquivo Python que pode ter diversas funções para utilizarmos.
Pacote = É um diretório contendo uma coleção de módulos.

Desta forma, a pasta onde foi criado o projeto guppe pode ser considerado um pacote.

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__. py Nas
versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é uilizado para
manter compatibilidade.

****** IMPORTANTE ****** :
Neste ponto do curso criamos um pacote chamado geek dentro do diretório do curso e dentro deste pacote, criamos
dois scripts chamados geek1.py e geek2.py. Além destes scripts, criamos também um outro pacote chamado university
e dentro dele, mais dois scripts chamados geek3.py e geek4.py. Os arquivos __init__.py foram criados automaticamente.
"""

# Agora vamos começar a usar o pacote, seus módulos e conteúdos:

"""
# Importando os módulos geek2 e geek2 do pacote geek:
from geek import geek1, geek2

# Importando os submódulos geek3 e geek4 do subpacote university do pacote geek:
from geek.university import geek3, geek4

# Imprimindo a constante pi do módulo geek1 do pacote geek:
print(geek1.pi)

# Imprimindo a funcao1 do módulo geek1 do pacote geek:
print(geek1.funcao1(4, 6))

# Imprimindo a variável curso do módulo geek2 do pacote geek:
print(geek2.curso)

# Imprimindo a função do módulo geek2 do pacote geek:
print(geek2.funcao2())

# Imprimindo a função do submódulo geek3 do subpacote university do pacote geek:
print(geek3.funccao3())

# Imprimindo a função do submódulo geek4 do subpacote university do pacote geek:
print(geek4.funcao4())
"""

# Importando somente uma função específica de um módulo específico do pacote geek:
from geek.geek1 import funcao1

# Importando somente uma função específica de um módulo específico do subpacote university do pacote geek:
from geek.university.geek4 import funcao4

# Imprimindo o que foi importado anteriormente
print(funcao1(6, 9))
print(funcao4())
