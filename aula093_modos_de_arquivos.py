"""
Modos de abertura de arquivos:

Character - Meaning
'r' - open for reading (default)
'w' - open for writing, truncating the file first
'x' - open for exclusive creation, failing if the file already exists
'a' - open for writing, appending to the end of file if it exists
'b' - binary mode
't' - text mode (default)
'+' - open for updating (reading and writing)

Para ver todos estes modos de arquivos: https://docs.python.org/3/library/functions.html#open

Tradução:

Caractere - Significado
'r' - abre para leitura - padrão
'w' - abre para escrita, sobrescreve o arquivo caso já exista
'x' - abre exclusivamente para criação somente se o arquivo não existir
'a' - abre para escrita, adicionando conteúdo no final caso já exista conteúdo
'b' - modo binário
't' - modo texto - padrão
'+' - abre para atualização - leitura e escrita
"""

with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')

# Na tentativa de abrir o arquivo para escrita, o Python nos retorna um FileExistsErro

