"""
Bloco With

Passos para se trabalhar com arquivos:
1 - Abrir o arquivo;
2 - Maninpular o arquivo;
3 - Fechar o arquivo.
Importante fechar o arquivo para encerrar o streaming!

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.
"""

# O bloco with:
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

"""
Note que o processo é o mesmo, mas usando o bloco with cria um contexto onde já determinamos o nome arquivo no lugar
da variável e já manda executar o print logo abaixo. Ao encerrar o comando, não precisamos mais fechar o arquivo, pois
ao concluir o bloco o Python já nos tira para fora de contexto do bloco.

Se tentarmos fazer um novo print, teremos o seguinte erro: ValueError: I/O operation on closed file.
O próprio erro já diz: Erro de valor: operação de entrada/saída em um arquivo fechado!

Essa é a forma Pythônica de manipular arquivos, ou seja, é a forma correta.
"""

print(arquivo.closed)
