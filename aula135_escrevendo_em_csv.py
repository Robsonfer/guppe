"""
Aula 135 - Escrevendo em arquivos CSV

Se para ler aquivos nós usamos o método reader() que significa leitor, para escrever teremos um método writer(), ou seja, escritor.

O método writer() cria um objeto que nos permite escrever em arquivos CSV.

A partir deste conhecimento, temos:

writerow() = Este método escreve uma linha.
"""

# writer() gera um objeto para que possamos escrever em um arquivo CSV. writerow() escreve cada linha através de uma lista.

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração do filme (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
