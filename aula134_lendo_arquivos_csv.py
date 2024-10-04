"""
Lendo arquivos CSV

CSV - Coma Separated Values (Valores Separados por Vírgula)

Apesar do nome, podemos ter vários tipos de separadores:
    - Separador por vírgula;
        1, 2, 3, 4, 5
        "geek", "university", "pyton", "ciência", "dados"
    - Separador por ponto e vírgula:
        1; 2; 3; 4; 5
        "geek"; "university"; "pyton"; "ciência"; "dados"
    Separador por espaço:
        1 2 3 4 5
        "geek" "university" "pyton" "ciência" "dados"


Este é um website onde podemos conseguir dados:

http://dados.gov.br/dataset
"""

"""
# Possível de se trabalhar, mas não é o ideal (trabalhoso):

with open('lutadores.csv', encoding='utf-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    dados = dados.split(',')[3:]
    print(dados)
"""

"""
A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader: Permite iterar sobre as linhas do CSV como listas;
    - DictReader: Permite iterar sobre as linhas do arquivo CSV como OrederdDicts.
"""


"""
# Reader:

from csv import reader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Com next() vamos pular o cabeçalho!
    for linha in leitor_csv:
        # Cada linha é uma lista!
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros de altura.')
"""

"""
# DictReader:

from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict!
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros de altura.')
        # Sabemos que em Dicionário trabalhamos com chave/valor e neste caso o cabeçalho será a chave de cada valor.
"""


# OBS: O Reader e o DictReader já usam por padrão o separador vírgula, mas se for necessário basta acrescentar o separador como parâmetro:

# DictReader com outro separador:

from csv import DictReader

with open('lutadores_delimiter.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=';')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict!
        print(f'{linha["Nome"]} nasceu no(a)(s) {linha["País"]} e mede {linha["Altura (em cm)"]} centímetros de altura.')
        # Sabemos que em Dicionário trabalhamos com chave/valor e neste caso o cabeçalho será a chave de cada valor.
