﻿"""
Seek e Cursors

seek() = É utilizada para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar
o cursor. Traduzindo de maneira literal, seek quer dizer procurar.

Imagine que você tem um conteúdo muito grande para ler com o Python. Neste caso o correto seria fazer a leitura
linha a linha. Para isto usamos a função readline().

readline() = É uma função que lê o arquivo linha a linha.

"""

arquivo = open('texto.txt')

"""
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek():
arquivo.seek(0)
# Colocando o parâmetro do seek() como zero, eu defino que o cursor volte para a posição zero do texto.

# Agora podemos imprimir pela segunda vez seguida:
print(arquivo.read())

# O interessante é que podemos iniciar o seek() em qualquer que desejamos, por exemplo, a partir do caracter 22:
arquivo.seek(22)

print(arquivo.read())
"""

# Exemplo de readline():
print(arquivo.readline())
# Usando no formato acima nós imprimimos somente a 1ª linha, mas o cursor ficou esperando no início da 2ª linha
print(arquivo.readline())
# E assim imprimimos a segunda linha na sequência
print(arquivo.readline())
# E a terceira linha