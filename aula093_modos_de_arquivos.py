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

# Exemplo do modo 'x':

"""
with open('university.txt', 'x') as arquivo:
    arquivo.write('Teste de conteúdo.\n')
"""
# A partir de agora, ou seja, depois de gerado o arquivo, se tentar abrir o arquivo novamente, o Python nos retorna um FileExistsErro.

# Suponha que queremos escrever um arquivo, mas não queremos subscrever se ele já exista, podemos fazer o seguinte:
"""
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Este arquivo já existe, tente outro nome!')
"""

# Eemplo do modo 'a':
"""
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ').lower()
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
"""

# Exemplo do modo '+':
with open('outro.txt', 'a+') as arquivo:
    arquivo.seek(0)
    arquivo.write('No topo!\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')
# O mais sempre vem com algum outro modo.
