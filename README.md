# Repositório das aulas do Curso de Python da Geek University da Udemy
___
## Sobre este documento
Este documento visa é criar um caderno de estudos durante o andamento do curso. O objetivo é estudar a linguagem de programação em questão e ao mesmo tempo treinar o formado markdown e se preparar posteriormente para a criação de documentações. 
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

#### 

### Mapas

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