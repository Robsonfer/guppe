"""
Seek e Cursors

seek() = É utilizada para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar
o cursor. Traduzindo de maneira literal, seek quer dizer procurar.

Imagine que você tem um conteúdo muito grande para ler com o Python. Neste caso o correto seria fazer a leitura
linha a linha. Para isto usamos a função readline().

readline() = É uma função que lê o arquivo linha a linha.

readlines() = É uma função que coloca o texto em uma lista de strings sendo que cada linha é uma string na lista.

close() = É uma função qu eencerra a conexão (streaming) entre o arquivo aberto e lido e o nosso programa.

closed = É uma função que verifica se o arquivo está aberto ou fechado.

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar o arquivo;
3 - Fechar o arquivo.

OBSERVAÇÃO:
- Quando usamos o read(), podemos limitar o conteúdo definindo um parâmetro que determina quantos caracteres vamos ler,
ou seja, a leitura começa da posição zero e lê até onde quisermos;
- Quando usamos o readline(), o parâmetro determina o corte da linha, ou seja, se usarmos readline(22), na primeira
linha teremos somente 22 caracteres, o restante do texto é jogado para a próxima linha;
- Quando usamos o seek, o parâmetro determina a partir de onde iniciamos nossa leitura.
"""

# Passo 1 - Abrir o arquivo:
arquivo = open('texto.txt')

# Passo 2 - Trabalhar o arquivo:

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

"""
print(arquivo.readline())
# Usando no formato acima nós imprimimos somente a 1ª linha, mas o cursor ficou esperando no início da 2ª linha
print(arquivo.readline())
# E assim imprimimos a segunda linha na sequência
print(arquivo.readline())
# E a terceira linha
"""

# Analisando o tipo do readline():

"""
retorno = arquivo.readline()
print(type(retorno))
print(retorno)
# Sabendo que o tipo do retorno do readline() é string, podemos usar tudo aquilo que é funcional para strings.

# Por exemplo, criar uma lista usando como separador o caracter espaço:
print(retorno.split(' '))
"""

# Exemplo de readlines():

"""
# Podemos por exemplo saber quantas linhas temos em um texto:
linhas = arquivo.readlines()
print(f'Este arquivo tem {len(linhas)} linhas')
print(linhas)
"""

"""
OBS IMPORTANTE:
Quando abrimos um arquivo com a função open(), criamos uma conexão entre o arquivo no disco do computador e o  nosso
programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão.
Para isso utilizamos a função close().

Fechar esse arquivo é muito importante, pois evita vários problemas e erros.
"""

print(f'Status closed do arquivo: {arquivo.closed}')

# Passo 3 - Fechar o arquivo:
arquivo.close()

print(f'Status closed do arquivo: {arquivo.closed}')

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError.
