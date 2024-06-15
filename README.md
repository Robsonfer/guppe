# Repositório das aulas do Curso de Python da Geek University da Udemy
___

## Sobre este documento
Este documento visa criar um caderno de estudos durante o andamento do curso de Python da Geek University.

O objetivo é estudar a linguagem de programação em questão e ao mesmo tempo, treinar o formato markdown e se preparar posteriormente para a criação de documentações.

Portanto, nenhum conteúdo de uso exclusivo para alunos da Geek University será encontrado neste documento. Os arquivos e links disponibilizados neste documento o direcionarão somente para conteúdos livres de direitos autorais como Sites abertos da Internet, o repositório em questão, e repositórios de outros que venha nos ajudar a melhor compreender o conteúdo do curso. 

Com base nestas últimas informações, deixo aqui o repositório com as orientações sobre edição de arquivos markdown: https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
___
## Seção 1 - Apresentação do Curso

### 1. Sobre o curso
Neste tópico temos basicamente uma explanação sobre o que vem por aí.

### 2. Informações importantes

Todos os cursos da Geek University são constantemente atualizados quando há necessidade. Desta forma, novas seções ou aulas podem ser adicionadas em diferentes partes do curso. Pode ser, por exemplo, que você inicie uma aula onde eu informo o nome ou número da seção ou aula que não condiz com a seção ou aula que você está estudando. Ignore isto e se atente ao conteúdo da aula na sequência que está assistindo.

Você poderá encontrar materiais para download em algumas seções/aulas do curso. Caso encontre problemas para realizar os downloads, acesse o suporte da plataforma Udemy sobre este tema em: https://support.udemy.com/hc/en-us/articles/229604708-Downloading-Course-Resources

Se tiver dúvidas ou problemas sobre as aulas do curso, faça uma pesquisa na Área de Perguntas e Respostas presente na página do curso. Se você não encontrar uma solução para sua dúvida ou problema, crie um novo tópico postando prints de tela de forma que possamos analisar todo o contexto e então te auxiliar. Se não souber usar a Área de Perguntas e Respostas, você pode verificar o guia presente na plataforma Udemy em https://support.udemy.com/hc/en-us/articles/229233387-How-to-Use-The-Q-A

Ao finalizar o curso você poderá gerar um certificado simples gerado pela plataforma Udemy. Caso você esteja com problemas em gerar este certificado, verifique este tópico na plataforma Udemy: https://support.udemy.com/hc/en-us/articles/229603868-Certificate-of-Completion

Ao finalizar o curso você poderá solicitar um certificado completo gerado pela Geek University em https://www.geekuniversity.com.br/certificados

### 3. Preparação do ambiente
Neste tópico também não temos vídeo, somente um texto com os links para download das ferramentas necessárias para dar sequência no curso.

SOFTWARES UTILIZADOS DURANTE O CURSO:

Python: https://www.python.org/downloads/

JAVA JDK LTS: https://www.oracle.com/java/technologies/downloads/

PyCharm Community: https://www.jetbrains.com/pycharm/download/

### 4. Testando o ambiente preparado
Neste tópico é explicado como instalar as ferramentas necessárias como o próprio Python, o JDK do Java e a IDE Pycharm. Mas o mais importante fica a cargo do ambiente virtual.

Para programar de forma profissional com o Python, é importante iniciar cada projeto dentro de seu próprio ambiente virtual. Isso é necessário para que em cada ambiente tenha sua própria versão da linguagem e de suas bibliotecas. Existem empresas que trabalham com outras versões das linguagens e devido à limitações de outras tecnologias, não atualizam estas versões. Portanto, usar os ambientes virtuais possibilita que cada projeto tenha suas particularidades sem conflitos.

O próprio Python já tem a ferramenta para esse ambiente virtual chamado venv (virtual environments).

Você encontrará o primeiro código criado neste módulo no repositório ***[guppe](https://github.com/Robsonfer/guppe)*** como ***[aula004_teste.py](https://github.com/Robsonfer/guppe/blob/main/aula004_teste.py)***, ou clicando no link com o nome da aula.
___
## Seção 2 - Introdução à linguagem Python

### 5. O que vamos aprender nessa seção?
Neste tópico é comentado o que será apresentando nesta seção.

### 6. PEP8 - Boas Práticas
***IMPORTANTE:*** Tudo o que você precisar sobre Python poderá ser encontrado dentro do site oficial da linguagem: https://www.python.org/ e durante o decorrer deste documento, serão disponibilizados links diretos para o assunto em questão como por exemplo, para esta aula, o ***[PEP8](https://wiki.python.org.br/GuiaDeEstilo)***

O **PEP8 - Python Enhancement Proposal** são propostas de melhoria para a linguagem Python.

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

The Zen of Python: import this

1. Utilize Camel Case para nomes de classes:
```
class Calculadora:
    pass
class CalculadoraCientifica:
    pass
 ```

2. Utilize nomes em minúsculo, separados por underline para funções ou variáveis:
```
def soma():
    pass
def soma_dois():
    pass
numero = 4
numero_impar = 5
```

3. Utilize 4 espaços para identação (NÃO use tab):
```
if 'a' in 'banana':
    print('tem')
```

4. Linhas em branco:
 - Separar funções e definições de classe com duas linhas em branco.
 - Métodos dentro de uma classe deve ser serarado com uma única linha em branco.

5. Imports:
 - Imports devem ser sempre feitos em linhas separadas:
```
# Import errado:
import sys, os

# Import certo:
import sys
import os

# Não tem problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer assim:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
```

- imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes de
 constantes ou variáveis globais.

6. Espaços em expressões e instruções:

- Não faça:
`funcao( algo[ 1 ], { outro: 2 } )`

- Faça:
`funcao(algo[1], {outro: 2})`


- Não faça:
`algo (1)`

- Faça:
`algo(1)`


- Não faça:
`dict ['chave'] = list [indice]`

- Faça:
`dict['chave'] = list[indice]`


- Não faça:
```
x              = 1
y              = 2
variavel_longa = 3
```

- Faça:
```
x = 1
y = 2
variavel_longa = 3
```

7. Termine sempre uma instrução com uma nova linha

É importante lembrar que o Pycharm é a IDE adotada como oficial para o Python, portanto ela tem ferramentas exclusivas que outras IDEs não têm como por exemplo avisos quando fugimos dos padrões da PEP8.

O código dessa aula pode ser encontrado aqui: [aula006_pep8.py](https://github.com/Robsonfer/guppe/blob/main/aula006_pep8.py) 

### 7. Dir e Help
São utilitários Python para auxiliar na programação:

- Dir = Apresenta todos os atributos/propriedades, funções/métodos disponíveis para determinado tipo de dado ou variável.
- Help = Apresenta a documentação/Como utilizar os atribuos/propriedades e funções/métodos disponíveis para determinado
tipo de dado ou variável.

Exemplo do uso de dir():

`print(dir('Robson'))`

Resultado do comando acima:
```chatinput
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
'__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace',
'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
'translate', 'upper', 'zfill']
```

Exemplo do uso de help():
```
num = 4
help(num)
````

O resultado do comando `help(num)` é tão grande que não faz sentido ser colocado aqui, mas basicamente ele mostra toda a documentação do que for consultado dentro do `help()`.

O código dessa aula pode ser encontrado clicando aqui: [aula007_dir_e_help.py](https://github.com/Robsonfer/guppe/blob/main/aula007_dir_e_help.py)

### 8. Recebendo dados do usuário


### 9. Recapitulando
___
## Seção 3: Variáveis e Tipos de Dados em Python

### 10. O que vamos aprender nessa seção?

### 11. O tipo numérico

### 12. O tipo float

### 13. O tipo boolean

### 14. O tipo string

### 15. Escopo de variáveis

### 16. Recapitulando

## Seção 4: Estruturas Lógicas e Condicionais em Python

### 17. O que vamos aprender nessa seção?

### 18. If, else, elif

### 19. AND, OR, NOT, IS

### 20. Recapitulando

___
## Seção 5: Estruturas de Repetição em Python

### 21. O que vamos aprender nesta seção?

### 22. Loop for

### 23. Entendendo e explorando ranges

### 24. Loop while

### 25. Saindo de loops com break

### 26. Recapitulando

___
## Seção 6 - Coleções Python

### 27. O que vamos aprender nesta seção?

### 28. Listas

### 29. Tuplas

### 30. Dicionários

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

### 31. Mapas

### 32 .Conjuntos

### 33. Módulo Collections - Counter

### 34. Módulo Collections - Default Dict

### 35. Módulo Collections - Ordered Dict

### 36. Módulo Collections - Named Tuple

### 37. Módulo Collections - Deque

### 38. Recapitulando

___
## Seção 7: Funções em Python

### 39. O que vamos aprender nesta seção?

### 40. Definindo funções

### 41. Funções com retorno

### Exercício de programação 1: Mão na massa geek

### 42. Funções com parâmetro

### 43. Funções com parâmetro padrão

### 44. Documentando funções com Docstrings

### 45. Entendendo o *args

### 46. Entendendo o *kargs

### 47. Recapitulando

## Seção 8: Comprehensions em Python

### 48. O que vamos aprender nesta seção?

### 49. List Comprehension - parte 1

### 50. List Comprehension - parte 2

### 51. Listas aninhadas

### 52. Dictionary Comprehension

### 53. Set Comprehension

### 54. Recapitulando
___
## Seção 9: Expressões Lambdas em Funções Integradas

### 55. O que vamos aprender nesta seção?

### 56. Utilizando lambdas

### 57. Map

### 58. Filter

### 59. Reduce

### 60. Any e All

### 61. Generators

### 62. Sorted

### 63. Min e Max

### 64. Reversed

### 65. Len, Abs, Sum e Round

### 66. Zip

### 67. Recapitulando
___
## Seção 10: Debugando e Tratando erros

### 68. O que vamos aprender nesta seção?

### 69. Erros mais comuns em Python

### 70. Levantando so próprios erros com raise

### 71. O bloco Try/Except

### 72. Try, Except, Else e Finally

### 73. Debugando o código com PDB

### 74. Recapitulando
___
## Seção 11: Trabalhando com Módulos Python

### 75. O que vamos aprender nessa seção?

### 76. O módulo random

### 77. Trabalhando com módulos Built-in

### 78. Módulos customizados

### 79. Instalando e utilizando módulos externos

### 80. Pacotes

### Recapitulando
___
## Seção 12: Leitura e Escrita em Arquivos

### 83. O que vamos aprender nesta seção

### 84. Leitura de arquivos

### 85. Seek e Cursors

### 86. O comando With

### 87. Escrevendo em arquivos

### 88. Modos de arquivos

### 89. StringIO

### 90. Sistema de Arquivos - Navegação

### 91. Sistema de Arquivos - Manipulação

### 92. Recapitulando
___
## Seção 13: Iteradores e Geradores Python

### 93. O que vamos aprender nesta seção?

### 94. Entendendo iterators e iteráveis

### 95. Criando sua própria versão de loop

### 96. Escrevendo um Iterador

### 97. Geradores

### 98. Teste de memória com Generators

### 99. Teste de Velocidade com Expressões Geradoras

### 100. Recapitulando
___
## Seção 14: Decoradores em Python

### 101. O que vamos aprender nesta seção?

### 102. Funções de maior Grandeza

### 103. O que são decoradores?

### 104. Decoradores com diferentes assinaturas

### 105. Preservando Metadata com Wraps

### 106. Forçando tipos de dados com um decorador

### 107. recapitulando
___
## Seção 15: Orientação a Objetos com Python

### 108. O que vamos aprender nesta seção?

### 109. O que é Orientação a objetos?

### 110. Classes

### 111. Atributos

### 112. Métodos

### 113. Objetos

### 114. Abstração

### 115. Recapitulando
___
## Seção 16: Herança e Polimorfismo

### 116. O que vamos aprender nesta seção?

### 117. Herança

### 118. Propriedades

### 119. O método super()

### 120. Herança Múltipla

### 121. MRO -Method Resolution Order

### 122. Polimorfismo

### 123. Métidos Mágicos

### 124. Recapitulando
___
## Seção 17: Manipulando Arquivos CSV e JSON

### 125. O que vamos aprender nesta seção

### 126. Lendo arquivos CSV

### 127. Escrevando em arquivos CSV

### 128. Conhecendo o Pickle

### 129. Trabalhando com JSON e Pickle

### 130. Recapitulando
___
## Seção 18: Trabalhando com Data e Hora em Python

### 131. O que vamos aprender nesta seção

### 132. Manipulando data e hora

### 133. Trabalhando com deltas de data e hora

### 134. Métodos de datas e horas

### 135. Recapiltulando
___
## Seção 19: Testes com Python

### 136. O que vamos aprender nesta seção?

### 137. Por que testar nosso código?

### 138. Assertions (afirmações)

### 139. Doctests

### 140. Introdução ao módulo Unittest

### 141. Outros tipos de assertions

### 142. antes e após hooks

### 143. Recapitulando
___
## Seção 20: Gerenciamento de Memória em Python

### 144. O que vamos aprender nesta seção?

### 145. Alocação e Gerência de Memória em Python

### 146. GIL - Python Global Interpreter Lock

### 147. Como praticar mais Python? Edabit

### 148. Recapitulando
___
## Seção 21: Checagem de Tipos em Python

### 149. O que vamos aprender nesta seção?

### 150. Tipagem de dados Dinâmica x Estática

### 151. Duck Typing

### 152. Type Hinting

### 153. Checagem de Tipos com MyPy

### 154. Prós e Contras do uso de Type Hinging

### 155. Fazendo uso de Annotations

### 156. Tipos em Comentários

### 157. Tipos em Python na Prática

### 158. Recapitulando
___
## Seção 22: novos recursos do Python

### 159. O que vamos aprender nesta seção?

### 160. O operador Warlus

### 161. Argumentos somente posicionais

### 162. Tipos de dados mais precisos

### 163. Debugger mais simples com f-strings

### 164. O Conselho do diretor do Python

### 165. Metadata

### 166. Funções Matemáticas e Estatísticas

### 167. Alertas sobre sintaxes perigosas

### 168. Optimizações

### 169. Recapitulando
___
## Seção 23: Projeto Python 1 - Game

### 170. O que vamos aprender nesta seção?

### 171. Criando nosso projeto

### 172. Estruturando nosso código

### 173. Implementação - Parte 1

### 174. Implementação - Parte 2

### 175. Executando nosso projeto

### 176. Recapitulando
___
## Seção 24: Projeto Python 2 - Mercado

### 177. O que vamos aprender nesta seção?

### 178. Criando nosso projeto

### 179. Estruturando nosso código

### 180. Implementação - Parte 1

### 181. Implementação - Parte 2

### 182. Executando nosso projeto

### 183. Recapitulando
___
## Seção 25: Projeto Python 3 - Banco

### 184. O que vamos aprender nesta seção?

### 185. Criando nosso projeto

### 186. Estruturando nosso código

### 187. Implementação - Parte 1

### 188. Implementação - Parte 2

### 189. Executando nosso projeto

### 190. Recapitulando
___
## Seção 26: Encerramento

### 191. Recapitulando

### 192. Quais os próximos passos?
___
## Dicionário Geral de Python:

### String:
String é um conjunto de caractéres que forma um dado com o formato que estamos habituados como palavras, frases, e similares como códigos não numéricos.