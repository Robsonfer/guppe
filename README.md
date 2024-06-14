# Repositório das aulas do Curso de Python da Geek University da Udemy
___
## Sobre este documento
Este documento visa criar um caderno de estudos durante o andamento do curso. O objetivo é estudar a linguagem de programação em questão e ao mesmo tempo treinar o formado markdown e se preparar posteriormente para a criação de documentações. 
___
## Seção 2 - Praparando o ambiente

### Instalação no Windows

### Ambientes virtuais
___
## Seção 3 - Introdução à linguagem:

### PEP8 - Boas práticas

### Dir e Help

### Recebendo dados do usuário
___
## Seção 4 - Variáveis e Tipos de dados em Python

### Tipo numérico

### Tipo float

### Tipo booleano

### Tipo string

### Escopo de variáveis

## Seção 5 - Estruturas lógicas e condicionais em Python

### If, else, elif

### AND, OR, NOT, IS
___
## Seção 6 - Estruturas de repetição em Python

### Loop for

### Ranges

### Loop while

### Saindo de loops com break
___
## Seção 7 - Coleções Python

### Listas

### Tuplas

### Dicionários

#### _Definição:_
Um dicionário Python é uma forma de coleção de dados em que se guarda uma chave e um valor correspondente. É similar a um dicionário mesmo, em que há sempre um termo e uma tradução.

Assim, você encontra um valor pelo elemento correspondente — diferentemente de encontrar por um índice como em uma lista. O dicionário é uma forma de organização similar a um de banco de dados, mais completa e abrangente para diversas situações. 

Um dicionário grande e bem estruturado lembra muito um dataset, com os dados em um formato matricial, de tabela. Isso facilita o controle e o mapeamento desses dados. 

Uma forma fácil de visualizar um dicionário é uma lista telefônica. Nesse caso, as chaves são os nomes, elementos que demarcam a individualidade; ao passo que os números são os valores, elementos identificadores. 

#### _Detalhes sobre um Dicionário?_
- Os dicionários são representandos por chaves `{}`.
- São separados por dois pontos `'chave:valor'`.
- Se usarmos a seguinte linha de código: `print(type({}))`, a nossa resposta no terminal será  `<class 'dict'>`, ou seja, é um dicionário.
- Tanto chave quanto valor podem ser de qualquer tipo de dado.
- Pode-se misturar tipos de dados.

#### _Formas de criar um dicionário_
Existem duas formas de criar um diciónário em Python:
 
1. A primeira forma e mais comumente usada é determinando o nome do dicionário seguido do símbolo de atribuição e logo em seguida a abertura de colchetes e a determinação dos conjuntos chave/valor separados com dois pontos. Cada item do dicionário deve ser separado por vírgula: 

`paises = {'br': 'Brasil', 'usa': 'Estados Unidos', 'par': 'Paraguai'}`

2. A segunda forma e bem menos comum de ser usada é determinando o nome do dicionário seguido do sinal de atribuição e logo em seguida a palavra reservada dict seguida da abertura de parênteses e dentro determinando os conjuntos chave/valor separados pelo sinal de igual ou atribuição. Cada item do dicionário deve ser separado por vírgula como na primeira forma:

`paises = dict(br='Brasil', usa='Estados Unidos', par='Paraguai')`

**Observação Importante:** Notar que enquanto no primeiro formato a chave deve ser informada com àspas simples ou duplas, no segundo caso a chave não utiliza àspas em sua definição, entretanto o valor correspondente à chave continuará utilizando as àspas enquano for uma string.

#### _Formas de acessar os elementos:_

1. Forma 1: Acessando via chave da mesma forma que lista/tupla:
`print(paises['br'])`
2. Forma 2: Acessando via get - Forma recomendada:
`print(paises.get('br'))`

**Observções Importantes:**
- No caso das listas e tuplas para acessar os elementos, basta usar `[0]` que acessamos o índice zero. Entretanto os dicionários não são indexados. Portanto no lugar do índice, usamos a chave.
- A utilização de uma chave inexistente irá gerar um erro.

#### _Explicação da aula sobre o tipo None_

O tipo de dado None em Python representa a ausência de tipo ou conhecido também como tipo vazio, ou seja, é a definição de um elemento sem tipo definido.

**Observações Importantes:**
- Quando devemos utilizar o tipo None? Quando quisermos criar uma variável e inicializá-la sem tipo antes de receber um valor final. Aí define-se o tipo.
- O tipo None será SEMPRE considerado como False!
- É melhor buscar o item pelo get do que pela chave, pois com get se der erro, a aplicação não para.
- Pela chave podemos tratar o erro, mas com get elimina-se a etapa de tratativa desse erro.
- O tipo None é _SEMPRE_ especificado com a primeira letra maiúscula.

Veja abaixo o tipo de dado None mostrado no terminal como ficaria:

```
numeros = None
print(numeros)
print(type(numeros))

None
<class 'NoneType'>
```
**Exemplo de busca usando o get com if/else evitando o erro:**
```
Russia = paises.get('ru')
if Russia:
    print('Encontrei o País')
else:
    print('Não encontrei o País')
```

**Exemplo de busca usando o get sem o if/else evitando o erro:**
```
pais = paises.get('din', 'Não encontrado')
print(pais)
```

Nesse caso acima estamos definindo uma informação em caso de não encontrar a chave. Basicamente o que estamos fazendo é determinando uma variável `país` para armazenar a informação buscada por `paises.get()` de maneira pontual e mandando o Python fazer o seguinte: _procure a chave `'din'` dentro do dicionário `paises`, caso não encontre, coloque `'Não encontrado'` no lugar_.

O bom do código dessa forma é que fica muito mais enxuto e não precisamos das condicionais!

#### Consultado se o elemento está no dicionário pela chave:



#### 

### Mapas
Mapas, conhecidos em Python como Dicionários (Obs: Essa aula é uma continuação da aula 34)

#### Iterando sobre Dicionários:

Para cada chave dentro de receita, imprima a chave:
```
for chave in receita:
    print(chave)
```
Para cada chave dentro de receita, imprima o valor da receita:
```
for chave in receita:
    print(receita[chave])
```
Para cada chave dentro de receita, imprima a chave e o valor da receita:
```
for chave in receita:
    print(f'{chave} : {receita[chave]}')
```
Podemos ainda personalizar o exemplo anterior:
```
for chave in receita:
    print(f'Em {chave} a receita foi de R$ {receita[chave]},00')
```
Assim ficará o resultado no terminal:
```
Em jan a receita foi de R$ 100,00
Em fev a receita foi de R$ 250,00
Em mar a receita foi de R$ 400,00
```
#### Tendo acesso direto à todas as chaves:
Podemos simplesmente ter acesso direto às chaves desta forma:
```
print(receita.keys())
```
Ficará assim no terminal:
```
dict_keys(['jan', 'fev', 'mar'])
```
Podemos usar o .keys() para fazer o for:
```
for chave in receita.keys():
    print(receita[chave])
```
Essa é inclusive a forma recomendada de fazer a Iteração!




### Conjuntos

### Módulo Collections - Counter

### Módulo Collections - Default Dict

### Módulo Collections - Ordered Dict

### Módulo Collections - Named Tuple

### Módulo Collections - Deque

___
## Dicionário Geral de Python:

### String:
String é um conjunto de caractéres que forma um dado com o formato que estamos habituados como palavras, frases, e similares como códigos não numéricos.