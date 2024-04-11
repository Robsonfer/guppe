"""
AULA 36 - CONJUNTOS

- Conjuntos em qualquer linguagem de programação, é uma referência à teoria dos conjuntos da matemática.

- Em Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática, os Sets (conjuntos):
    - Não possuem valores duplicados;
    - Não possuem valores ordenados;
    - Os elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Desta forma, conjuntos são bem utilizados quando precisamos armazenar elementos e:
    - Não precisamos nos preocupar com a ordenação deles;
    - Não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (Sets) são referenciados em Pyton com chaves {}

A diferença entre Conjutos (Set) e Mapas (Dicionários) em Python é que um dicionário tem chave/valor enquanto um conjunto tem apenas valores.
"""

# Definindo um conjunto:

# Forma 1:
s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3} # Repare que em "s" temos valores repetidos.
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não fará parte do conjunto.
set
"""
Forma 2 (mais comum): A forma 2 e mais comumente usada é na verdade a forma 1.
Pelo que eu compreendi, a forma 1: s = set({1, 2, 3}) o Pycharm não aceita mais.
Todas as vezes que eu tentei fazer o editor corrigiu para a forma correta.
"""

# Podemos verificar se determinado elemento está contido no conjunto:
if 3 in s:
    print(f'Temos o número 3 em {s}')
else:
    print(f'Não temos o número 3 em {s}')

# Importante lembrar que além de não ter valores duplicados, não temos valores ordenados tabmém:
dados = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34

lista = list(dados)
tupla = tuple(dados)
dicionario = {}.fromkeys(dados)
conjunto = set(dados)

print(f'Esta é a nossa lista: {lista}')
print(f'Esta é a nossa tupla: {tupla}')
print(f'Esta é o nosso dicionário: {dicionario}')
print(f'Este é o nosso conunto: {conjunto}')

# Assim como todo outro conjunto Python, podemos colocar todos tipos de dados misturados em Sets:
u = {1, 'b', True, 34.22, 44}
print(u)
print(type(u))

# Podemos iterar em um Set normalmente:
for valor in u:
    print(valor)

"""
Usos interessantes com Sets:

    Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou um museu e os visitantes informam manualmente a cidade de onde vieram.
    Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição.
    Exemplo:
"""

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(f'Estas são as cidades listadas por receber visitantes: {cidades}')
print(f'A quantidade de visitantes no dia de hoje foi de {len(cidades)} pessoas')

# Agora precisamos saber quantas cidades distintas temos visitando:
print(f'Nós tivemos somente {len(set(cidades))} cidades diferentes')
cidades_distintas = set(cidades)
print(f'E estas cidades são: {cidades_distintas}')

# Adicionando elementos em um conjunto:
v = {1, 2, 3}
v.add(4)
print(v)
v.add(4)
print(v)
# OBS: A duplicidade de adição de elementos em um conjunto não gera erro, entretanto é ignorado e não é adicionado.

# Removendo elementos de um conjunto:

# Forma 1 (remove):
print(f'Este é meu conjunto v antes de remover um elemento: {v}')
v.remove(4) # Deve ser informado o valor a ser removido (conjuntos não são indexados).
print(f'Este é meu conjunto v depois de remover o elemento 4: {v}')
# Se tentar remover um valor inexistente, será retornado um KeyError!

# Forma 2 (discard):
v.discard(3)
print(f'Esse é meu conjunto v depois de removido o elemento 3 com discard: {v}')
# Neste caso, se o valor não for encontrado, nenhum erro é gerado!
# Nenhum valor é retornado ao remover elementos.

# Copiando um conjunto para outro:
print(f'Este é o meu conjunto s: {s}')

# Forma 1 (Deep Copy):
novo = s.copy()
print(f'Este é o conjunto novo copiado de s: {novo}')
novo.add(8)
print(f'Este é o conjunto novo depois de adicionado o número 8: {novo}')
print(f'Este é o meu conjunto s: {s}')

# Forma 2 (Shallow Copy):
novo1 = v
novo1.add(3)
print(f'Este é o conjunto novo1 depois que recebeu os valores de v e adicionado 3: {novo1}')
print(f'Este é o conjunto v que sofreu Shallow Copy: {v}')

# Podemos remover todos os itens de um conjunto:
print(f'Este é o meu conjunto v: {v}')
v.clear()
print(f'Este é o meu conjunto v depois do clear: {v}')

# Métodos matemáticos de conjuntos:
estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patrícia'}

# União de conjuntos - forma 1 (usando union):
uniao = estudantes_python.union(estudantes_java)
print(f'Esta é a união entre os dois conjuntos usando union: {uniao}')

# União de conjuntos - forma 2 (usando pipe | ):
uniao2 = estudantes_python | estudantes_java
print(f'Esta é a união entre os dois conjuntos usando pipe ( | ): {uniao}')

# Inserseccao de conjuntos - forma 1 (usando intersection):
interseccao = estudantes_python.intersection(estudantes_java)
print(f'Esta é a instersecção entre os dois conjuntos usando intersection: {interseccao}')

# Inserseccao de conjuntos - forma 2 (usando & ):
interseccao2 = estudantes_python & estudantes_java
print(f'Esta é a instersecção entre os dois conjuntos usando &: {interseccao2}')

# Diferença entre conjuntos:

# Mostrando os estudantes que só estudam Python:
diferenca_python = estudantes_python.difference(estudantes_java)
print(f'Esta é a diferença entre os dois conjuntos dos estudantes que só estudam python: {diferenca_python}')

# Mostrando os estudantes que só estudam Java:
diferenca_java = estudantes_java.difference(estudantes_python)
print(f'Esta é a diferença entre os dois conjuntos dos estudantes que só estudam java: {diferenca_java}')

# Soma*, Valor máximo*, Valor mínimo*, Tamanho:
# * Se os valores forem todos inteiros ou rais
w = {1, 2, 3, 4, 5, 6}

print(f'Esta é a soma de w: {sum(w)}')
print(f'Este é o valor máximo de w: {max(w)}')
print(f'Este é o valor mínimo de w: {min(w)}')
print(f'Este é o tamanho de w: {len(w)}')