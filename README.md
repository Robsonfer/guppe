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

**Você encontrará o primeiro código criado neste módulo no repositório ***[guppe](https://github.com/Robsonfer/guppe)*** como ***[aula004_teste.py](https://github.com/Robsonfer/guppe/blob/main/aula004_teste.py)***, ou clicando no link com o nome da aula.**
___
## Seção 2 - Introdução à linguagem Python

### 5. O que vamos aprender nessa seção?
- PEP8;
- Dir;
- Help;
- Recebendo dados do usuário.

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

**O código dessa aula pode ser encontrado aqui: [aula006_pep8.py](https://github.com/Robsonfer/guppe/blob/main/aula006_pep8.py)** 

### 7. Dir e Help
São utilitários Python para auxiliar na programação:

- Dir = Apresenta todos os atributos/propriedades, funções/métodos disponíveis para determinado tipo de dado ou variável.
- Help = Apresenta a documentação/Como utilizar os atribuos/propriedades e funções/métodos disponíveis para determinado tipo de dado ou variável.

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

**O código dessa aula pode ser encontrado clicando aqui: [aula007_dir_e_help.py](https://github.com/Robsonfer/guppe/blob/main/aula007_dir_e_help.py)**

### 8. Recebendo dados do usuário
Para receber dados do teclado nós utilizamos o comando `input()`. Por exemplo:

Input de dados:
`nome = input('Qual é o seu nome? ')`

Saída de dados:
`print(f'Seja bem vindo(a) {nome}')`

Retorno no console Python:
`Seja bem vindo(a) Robson`

E podemos continuar o diálogo colocando mais um input de dados:
`idade = int(input('Qual é a sua idade? '))`

E configurando a saída:
```
print(f'Que legal {nome}, {idade} anos é uma ótima idade!')
ano = 2023 - idade
print(f'Você nasceu em {ano}. Este foi um ano incrível!')
```

**_OBS IMPORTANTE_: Note que ao receber valores através do input para a variável idade, nós fazemos um Cast que nada mais é do que a conversão de um tipo de dado para outro:**

`idade = int(input('Qual é a sua idade? '))`

E por que precisamos fazer esse cast?
- Em primeiro lugar, é importante saber que toda recepção de dados via input, sempre acontecerá no formato string. Mesmo que armazerar este input em uma variável, ele será sempre uma string.
- Portanto, sempre que for necessário receber um valor que não seja no formato string, será necessário fazer o cast. Que é o caso da variável idade, pois desejamos logo em seguida realizar um cálculo com ela, o que não aconteceria se fosse uma string.

Retorno no console Python:
```
Qual é a sua idade? 43
Que legal Robson, 43 anos é uma ótima idade!
Você nasceu em 1980. Este foi um ano incrível!
```

**_OBS_**: Durante toda essa aula eu utilizei o formato moderno de print dinâmico que é `print(f'Olá {nome}')`. Esse formato é o mais atual e surgiu a já na versão 3 do Python, assim como a versão `print('Olá {0}' .format(nome))` enquanto a versão `print('Olá %s' %nome)` era utilizado na versão 2 do Python. Os três formatos funcionam, mas é recomendado com boa prática utilizar sempre a forma mais atual.

É muito importante conhecer os três formatos, pois podemos nos deparar com algum código antigo para dar manutenção e nesse momento não precisamos entendê-lo.

**O código dessa aula pode ser encontrado clicando aqui: [aula008_recebendo_dados_usuario.py](https://github.com/Robsonfer/guppe/blob/main/aula008_recebendo_dados_usuario.py)**

### 9. Recapitulando
Nesta seção aprendemos:
- PEP8: Como escrever códigos Pythônicos, ou seja, bonitos, práticos e da forma correta;
- Dir e Help: Recursos utilitários do Python:
  - Dir: Mostra a listagem do que é possível utilizar com determinado tipo de dado;
  - Help: Mostra a documentação destes recursos.
- Recebendo dados do usuário: Como receber dados via teclado e formatá-los conforme a sua necessidade. Destaque para o recurso de Cast.
___
## Seção 3: Variáveis e Tipos de Dados em Python

### 10. O que vamos aprender nessa seção?
- O tipo numérico;
- O tipo float;
- O tipo boolean;
- O tipo string;
- Escopo de variáveis.

### 11. O tipo numérico
O tipo numérico basicamente é tipo de variável de operações e quantificações matemáticas calculáveis.

Operações com o tipo numérico:

**Soma**: `5 + 2`
Retorno: `7`

**Subtração**: `7 - 2`
Retorno: `5`

**Multiplicação**: `3 * 5`
Retorno: `15`

**Divisão**: `5 / 2`
Retorno: `2.5`

Mas e se eu quiser ter somente a parte inteira da divisão acima? Devemos então fazer o cast?

```
divisao = int(5 / 2)
print(divisao)
```
Saída no console Python: `2`

Em Python para divisão retornar somente o valor inteiro não precisamos fazer cast, basta usar //: `print(5 // 2)`

Saída no console Python: `2`

E se quisermos obter então o resto da divisão, usamos o módulo %: `print(5 % 2)`

Saída no console Python: `1`

**_DICA_**: Este é um recurso muito utilizado na programação, pois é dessa forma que conseguimos distinguir números pares de números ímpares. Todo módulo de um número par resultará em zero, enquanto que todo módulo de um número ímpar resultará em 1!  

**Potenciação**: `5 ** 2` (cinco elevado ao quadrado)
Retorno: `25`

**_CURIOSIDADE_**: Em Java o tipo inteiro suporta até `2 ** 64`, mas um Byte ele reserva para o sinal, portanto o maior número inteiro que podemos armazenar em Java é `9223372036854775808`. Já no Python não existe essa limitação. Basicamente o seu limite é a sua memória. Enquanto seu computador tiver memória, o seu número pode crescer.

Outra coisa interessante no Python é que quando temos um número muito grande, podemos facilitar a visualização separando cada milhar do número por _underlines_ sem prejuízo de interpretação da linguagem, por exemplo:

Usando `1000000000` ou `1_000_000_000`, o Python entenderá o que está escrito. Se jogar no console da linguagem ele retornará o valor correto sem _underlines_.

Também podemos realizar operações com variáveis numéricas. Por exemplo:

```
num = 42
print(num + 1)
```
Retorno no console Python: `43`

**_DICA_**: Outro recurso muito utilizado nas linguagens de programação é a operação matemática seguida da alimentação da mesma variável da operação:

Podemos fazer a variável receber o valor dela mesma somado de mais uma unidade:
```
num = 42
num = num + 1
```
Retorno no console Python: `43`

Traduzindo, num recebe ele mesmo + 1

Ainda assim, existe uma forma mais curta para fazer isso:
```
num = 42
num += 1
```
Retorno no console Python: `43`

O `+=` faz exatamente o papel da expressão "ele mesmo +".

O mesmo serve para `num -= num`, `num *= num`, `num /= num`, `num //= num` ou `num %= num` 

Este recurso é interesante para criar contadores, e a partir daí pode-se fazer muitas outras coisas, como a criação de um número automático de cadastro ou a iteração em itens de uma lista onde cada soma de número chama o próximo já existente. As possibilidadese são infinitas.

Uma forma de itentificar qual é o tipo de uma variável ou valor, podemos utilizar a função `type()` que nos dá qual é o tipo:

```
>>> type(num)
<class 'float'>
```
Ou:
```
>>> type(23)
<class 'int'>
```

**_OBS_**: O formato demonstrado acima é o memso formato exibido no console Python onde já temos a digitação do comando e resposta automática abaixo sem precisar chamar o resultado com um print.

**O código dessa aula pode ser encontrado clicando aqui: [aula011_tipo_numerico.py](https://github.com/Robsonfer/guppe/blob/main/aula011_tipo_numerico.py)**

### 12. O tipo float
O tipo float, também conhecido como real ou decimal é o tipo numérico de ponto flutuante.

**_OBS_**: Importante lembrar que como o sistema seguido pelas linguagens de programação é o sistema americano, o separador das casas decimais é o ponto e não a vírgula.

Exemplo:

Se usarmos vírgula como no exemplo abaixo, estamos criando uma tupla e não um tipo float:
```
valor = 1, 44
print(valor)
```
Inclusive, o Python não aceita `valor = 1,44`, pois dará um erro de PEP8. Como ele está entendendo que estamos separando um número do outro, a boa prática conforme o PEP8 é dar um espaço entre a vírgula e o próximo número declarado. O correto seria `valor = 1, 44` para gerar a tupla.

Saída no console Python:
`(1, 44)`

E para gerar um tipo float, o correto é assim com ponto:
```
valor = 1.44
print(valor)
print(type(valor))
```
Saída no console Python:
```
1.44
<class 'float'>
```
É possível fazer dupla atribuição. Exemplo:
```
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))
```
Saída no console Python:
```
1
<class 'int'>
44
<class 'int'>
```
**_OBS IMPORTANTE_**: A dupla atribuição não é exclusiva do tipo float, mas foi demonstrado agora devido ao modo como a sentença `1, 44` foi escrita.

Todas as operações matemáticas estudadas com o tipo int, podemos realizar com o tipo float.

E como já foi visto antes na aula onde aprendemos a receber dados do usuário, é possível converter um tipo float para um tipo int. Exemplo:
```
valor = 1.44
resultado = (int(valor))
print(resultado)
print(type(resultado))
```
Saída no console Python:
```
1
<class 'int'>
```
Note que o Python retornou a parte inteira do número decimal, resultado da conversão do tipo float para o tipo inteiro (cast). O problema reside na perda de precisão.

Podemos também trabalhar com números complexos. O número complexo é representado pela junção com a letra j:
```
num_complex = 5j
print(num_complex)
print(type(num_complex))
teste = num_complex ** 2
print(teste)
print(type(teste))
```
Saída no console Python:
```
5j
<class 'complex'>
(-25+0j)
<class 'complex'>
```

**O código dessa aula pode ser encontrado clicando aqui: [aula012_tipo_float.py](https://github.com/Robsonfer/guppe/blob/main/aula012_tipo_float.py)**

### 13. O tipo boolean
O tipo boolena ou booleano vem da Álgebra de Boole e tem sempre duas constantes, verdadeiro ou falso. Na linguagem Python, True ou False. Sempre com a inicial maíuscula. Diferente disso, o Python não entenderá.

Usa-se este tipo para realizar operações básicas de duas posições, por exemplo, ligado ou desligado, ativo ou inativo, com sinal ou sem sinal.

#### 13.1. Operações Básicas: ####
- Negação (not)

A negação torna o valor booleano o inverso. Se for `True`, com a negação o valor alterna para `False` e se for `False`, alterna para `True`.
```
ativo = False
print(ativo)
```
Saída no console Python: `False`
```
ativo = False
print(not ativo)
```
Saída no console Python: `True`
- Ou (or)

É uma operação binária e depende de dois valores. O `or` retona um resultado comparativo entre duas variáveis booleanas e para que o resultado disso seja `True` é preciso que pelo menos uma das duas posições comparadas seja `True`:
```
x = True
y = False
z = x or y
print(z)
```
Saída no console Python: `True`
```
x = False
y = False
z = x or y
print(z)
```
Saída no console Python: `False`

Desta forma, de quatro combinações possíveis, só uma resultará em `False`.

- E (and)

Da mesma forma que o `or`, o `and` é uma operação binária que faz a comparação entre dois valores. No caso do `and`, para que o resultado seja `True`, é necessário que os dois valores sejam `True`:
```
x = True
y = False
z = x or y
print(z)
```
Saída no console Python: `False`
```
x = False
y = False
z = x or y
print(z)
```
Saída no console Python: `False`
```
x = True
y = True
z = x or y
print(z)
```
Saída no console Python: `True`

Desta forma, de quatro combinações possíveis, só uma resultará em `True`.

- Maior `>`, Menor `<`, Igual `==` e Diferente `!=`

Ainda operando com o tipo booleano temos as operações com Maior representando pelo símbolo matemático `>`, o Menor representado pelo símbolo matermático `<`, o Igual representado por `==` e por fim o Diferente representado por `!=`. Podemos entender melhor essas operação e esses operadores se partirmos direto para o console do Python onde basta digitar que o Python responde automaticamente:
```
>>> 5 > 6
False
>>> 5 < 6
True
>>> 6 == 6
True
>>> 4<= 5
True
>>> 5 != 6
True
```
O mesmo pode ser feito utilizando-se de variáveis:
```
>>> num1 = 7
>>> num2 = 8
>>> num1 >= num2
False
>>> num1 == num2
False
>>> num1 < num2 or num1 > 3
True
>>> num1 < num2 and num1 > 3
True
```
E se consultarmos os tipos:
```
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```
**O código dessa aula pode ser encontrado clicando aqui: [aula013_tipo_boolean.py](https://github.com/Robsonfer/guppe/blob/main/aula013_tipo_boolean.py)**

### 14. O tipo string



### 15. Escopo de variáveis

### 16. Recapitulando
- O tipo numérico:
- O tipo float:
- O tipo boolean:
- O tipo string:
- Escopo de variáveis:

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