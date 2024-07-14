"""
Escrevendo em arquvos

Até aqui aprendemos que por padrão a função open() abre os arquivos no modo 'r' de leitura. Aqui então aprenderemos
como abrir um arquivo para edição.

OBSERVAÇÃO IMPORTANTE: Quando abrimos um arquivo para leitura, não podemos realizar escrita nele, somente ler.
Da mesma forma, quando abrimos um arquivo para escrita, não podemos lê-lo, somente escrever nele.
"""

# Exemplo de escrita - modo 'w' (write)
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivos é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quissermos.\n')
    arquivo.write('Esta é a última linha.\n')

"""
Vamos às explicações:
- A primeira diferença que podemos notar é que nós informamos um arquivo que não existe na extensão .txt. Quando
informamos um arquivo que não existe com o modo 'w', esse arquivo é criado.
- Segunda diferença: note que a única diferença é que informamos o modo como segundo parâmetro da função open. Como
no caso da leitura já é padrão, então não precisamos informar o modo, já no caso da escrita, é essencial informar.
"""
