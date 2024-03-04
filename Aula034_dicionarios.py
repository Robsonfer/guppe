"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são connhecidos como mapas.

Dicionários são coleções do tipo chave/valor e são representados por chaves {}.

OBSVAÇÕES IMPORTANTES:
- Chave e valor são separados por dois pontos;
- Tanto chave quanto valor podem ser de qualquer tipo de dado;
- Podemos misturar tipos de dados;


"""

print('------------------------------------------------------------------------------')
print('Mostrando o tipo do dicionário:')
print(type({}))

# CRIAÇÃO DE DICIONÁRIOS:

print('------------------------------------------------------------------------------')
# FORMA 1 (MAIS COMUM)
print('Exemplo 1:')
paises = {'br': 'Brasil', 'usa': 'Estados Unidos', 'par': 'Paraguai'}
print(f'Aqui temos o dicionário paises: {paises}')
print(f'Aqui temos o tipo do dicionário paises: {type(paises)}')

print('------------------------------------------------------------------------------')
# FORMA 2 (MENOS COMUM)
print('Exemplo 2:')
paises1 = dict(br='Brasil', usa='Estados Unidos', par='Paraguai')
print(f'Aqui temos o dicionário paises1: {paises}')
print(f'Aqui temos o tipo do dicionário paises1: {type(paises)}')

print('------------------------------------------------------------------------------')
print('Acessando elementos pela chave:')
# IMPORTANTE: Dicionários não são indexados
# FORMA 1 - Acessando via chave:
print(f'Acessando o elemento Brasil via chave com colchetes: {paises["br"]}')
print(f'Acessando o elemento Paraguai via chave com colchetes: {paises["par"]}')
# Lembrando quem em listas e tuplas acessamos pelo índice, aqui não é pelo índice, mas sim pela chave.
# Usando chave inexistente será gerado um erro.

print('------------------------------------------------------------------------------')

# Parei a aula em 14:23 min
