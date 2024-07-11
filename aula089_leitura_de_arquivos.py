"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função open(), que literalmente signifca 'abrir'.

open() = Na forma mais simples de utilização, nós passamos apenas um porâmetro de entrada que neste caso é o caminho
para o arquivo a ser lido. Esta função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

Pra conhecer um pouco mais todos os parâmetros desta função, vamos à documentação:
https://docs.python.org/3/library/functions.html#open

OBS: Por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir ou então teremos o erro
FileNotFoundError!
"""

# Exemplo:
arquivo = open('texto.txt')

print(arquivo)
print(type(arquivo))

"""
Resultado no console do Python:
<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>
mode r = Modo de Leitura. r = read
Por padrão o modo de abertura do open() é leitura.
"""

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read())

"""
Se tentarmos imprimir novamente o texto na sequência, nada acontece. Mas porquê?
O Python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor do windows
quando estamos escrevendo. Ele define onde as ações acontecem, seja a partir de onde vamos escrever algo ou a partir
de onde vamos ler algo.
OBS IMPORTANTE: A função read() lê todo o conteúdo do arquivo. Independente da quantidade de linhas
"""

# Vamos ver o que a função read() retorna:
"""
retorno = arquivo.read()
print(type(retorno))
print(retorno)
"""
