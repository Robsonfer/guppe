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
paises = {'br': 'Brasil', 'usa': 'Estados Unidos', 'par': 'Paraguai', 'din': 'Dinamarca'}
print(f'Aqui temos o dicionário paises: {paises}')
print(f'Aqui temos o tipo do dicionário paises: {type(paises)}')

print('------------------------------------------------------------------------------')
# FORMA 2 (MENOS COMUM)
print('Exemplo 2:')
paises1 = dict(br='Brasil', usa='Estados Unidos', par='Paraguai')
print(f'Aqui temos o dicionário paises1: {paises}')
print(f'Aqui temos o tipo do dicionário paises1: {type(paises)}')

# ACESSANDO ELEMENTOS:

print('------------------------------------------------------------------------------')
# FORMA 1 - ACESSANDO PELA CHAVE:
print('Acessando elementos pela chave:')
# IMPORTANTE: Dicionários não são indexados
# FORMA 1 - Acessando via chave:
print(f'Acessando o elemento Brasil via chave com colchetes: {paises["br"]}')
print(f'Acessando o elemento Paraguai via chave com colchetes: {paises["par"]}')
# Lembrando quem em listas e tuplas acessamos pelo índice, aqui não é pelo índice, mas sim pela chave.
# Usando chave inexistente será gerado um erro.

print('------------------------------------------------------------------------------')
# FORMA 2 - ACESSANDO VIA GET (FORMA RECOMENDADA):
print('Acessando elementos via get:')
print(f'Acessando o elemento Brasil via get: {paises.get("br")}')
print(f'Acessando o elemento Paraguai via get: {paises.get("par")}')
print(f'Acessando um elemento que não existe via get: {paises.get("ru")}')
# IMPORTANTE: Note que neste caso usar um elemento que não existe não retorna um erro, mas sim um tipo None

"""
Tipo None

O tipo de dado None em Python representa a ausência de tipo ou conhecido também como tipo vazio.
Resumindo, é a definição de um elemento sem tipo definido.

OBS: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Quando devemos utilizar o tipo None?
- Quando quisermos criar uma variável e inicializá-la sem tipo antes de receber um valor final defindo um tipo.

IMPORTANTE: CONCLUINDO ENTÃO, E MELHOR BUSCAR O ITEM PELO GET DO QUE PELA CHAVE, POIS COM GET SE DAR ERRO A APLICAÇÃO NÃO PARA.
    PELA CHAVE PODEMOS TRATAR O ERRO, MAS COM GET ELIMINA-SE A ETAPA DE TRATATIVA DESSE ERRO!

OBS: O tipo None será SEMPRE considerado como False!
"""

print('Tipo None')
# Exemplificando:

numeros = None
print(f'Mostrando a variável numeros: {numeros}')
print(f'Mostrando o tipo da variável numeros: {type(numeros)}')

print('Variável do tipo None mudando de tipo.')

numeros = 1.44, 1.34, 5.67
print(f'Mostrando a variável numeros depois de receber dados: {numeros}')
print(f'Mostrando o tipo da variável numeros: {type(numeros)}')

# Exemplo de busca usando o get com if/else e evitando erro:
print('Exemplo de busca usando o get com if/else e evitando erro:')

Russia = paises.get('ru')
if Russia:
    print('Encontrei o País')
else:
    print('Não encontrei o País')

# Exemplo de busca usando get sem if/else:
print('Usando o mesmo código acima, mas sem o if/else:')
pais = paises.get('din', 'Não encontrado')
print(pais)

# IMPORTANTE: O tipo None sempre será falso:
if None:
    print('Sim')
else:
    print('Não')

print('------------------------------------------------------------------------------')
# VERIFICANDO SE DETERMINADO ELEMENTO ESTÁ DENTRO DO DICIONÁRIO POR MEIO DA CHAVE:
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)
# Temos a chave 'br' por isso o resultado será True, mas não temos 'ru' nem 'Estados Unidos' como chaves, por isso resulta em False.
# OBS: 'Estados Unidos' é um elemento e não uma chave!

# Isso nos dá a chance de fazer o if abaixo:
if 'mex' in paises:
    mexico = paises['mex']
# Se 'mex' existir em paises, a variavel mexico recebe paises com a chave 'mex' para depois ser usada como bem preferir e não dará key error.

# Relembrando o que foi dito no começo da aula, podemos utilizar qualquer tipo de dados (int, float, string, boolean), inclusive listas, tuplas, dicionários como chaves de dicionários. Por exemplo:

print('Exemplo da utilização de tipos de dados diferentes para criar um didionário:')
localidades = {
    (35.6895, 139.6917): 'Escritório em Tókio', (40.6643, -73.9385): 'Escritório em Nova York', (-23.5489, -46.6388): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

# Criamos um dicionário de localidades e a chave de cada valor é uma tupla de dois valores cada.
# E porque tupla é interessante pra usar como chave de dicionário? Pq a tupla é imutável, depois de criada não se muda mais.

print('------------------------------------------------------------------------------')
# ADICIONANDO ELEMENTOS EM UM DICIONÁRIO

receita = {'jan': 100,'fer': 120, 'mar': 300}

print(f'Este é o dicionario receita: {receita}')
print(type(receita))

# Forma 1 - Mais comum:
print('Adicionando o mês de Abril em nosso dicionário através da primeira forma:')
receita['abr'] = 350
print(f'Segue receita com o mês de Abril incluído: {receita}')

# Forma 2:
print('Adicionando o mês de Maio em nosso dicionário através da segunda forma:')
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# O exemplo acima é o mesmo que fazer assim:
receita.update({'jun': 750})
print(receita)

print('------------------------------------------------------------------------------')
# ATUALIZANDO DADOS EM UM DICIONÁRIO:

# Forma 1:
receita['mai'] = 550
print(f'Alterando o valor do mês de Maio em receita através da forma 1: {receita}')

# Forma 2:
receita.update({'mai': 600})
print(f'Alterando o valor do mês de Maio em receita através da forma 2: {receita}')

# CONCLUSÃO: A FORMA DE ADICIONAR OU ATUALIZAR DADOS É A MESMA. A DIFERENÇA É QUE UM DADO JÁ EXISTE E OUTRO AINDA NÃO!
# EM DICIONÁRIOS NÃO PODEMOS TER CHAVES REPETIDAS!!! MUITO CUIDADO POIS VC PODE REESCREVER OS SEUS DADOS.

print('------------------------------------------------------------------------------')
# COMO REMOVER DADOS DE UM DICIONÁRIO:

# Forma 1:
receita.pop('jun')
print(f'Removendo o mês de Junho de receita através da forma 1: {receita}')
# Nesta forma precisamos sempre informar a chave e caso a chave não seja encontrada, um KeyErro é retornado.

# Ao removermos um objeto, o valor desse objeto é sempre retornado.
ret = receita.pop('mai')
print(f'Valor retornado do receita.pop referente à chave mai: {ret}')
print(f'Removendo o mês de Maio de receita através da forma 1: {receita}')
