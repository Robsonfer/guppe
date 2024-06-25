"""
Erros mais comuns em Python

ATENÇÃO! É muito importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comum:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreve algo que o Python não reconhece como parte da linguagem.

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

3 - TyoeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas valor inapropriado.

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
"""

# Exemplos de SyntaxError:

# Exemplo 1:
"""
def funcao:
    print('Geek University')
"""
# SyntaxError: expected '(' (A definição de uma função exige a abertura e fechamento de parênteses seguido de :)

# Exemplo 2:
"""
None = 1
"""
# SyntaxError: cannot assign to None (None é uma palavra reservada para um tipo)

# Exemplo 3:
# return
# SyntaxError: 'return' outside function (O return deve ser colocado dentro de uma função, só uma função retorna algo)

# Exemplos de NameError:

# Exemplo 1:
# print(geek)
# NameError: name 'geek' is not defined (Neste caso geek não foi definido, não é nem uma string ainda)

# Exemplo 2:
# geek()
# NameError: name 'geek' is not defined (Da mesma forma, a função geek() precisa ser definida com def antes)

# Exemplo 3:
"""
a = 18
if a < 10:
    msg = 'É maior que 10'

print(msg)
"""
# NameError: name 'msg' is not defined (Neste caso faltou um else, portanto a linha onde é definida a variável msg não é lida e assim a variável nunca é definida)
# A alternativa para este erro é definir a variável msg antes do if.

# Exemplos de TypeError

# Exemplo 1:
# print(len(5))
# TypeError: object of type 'int' has no len() (A função len é para tipos iteráveis, quando usamos em um tipo que não é iterável como é o caso do exemplo acima, temos o erro de tipo)

# Exemplo 2:
# print('Geek' + [])
# TypeError: can only concatenate str (not "list") to str (Não podemos concatenar uma string e uma lista)

# Exemplo 3:
# print('Geek' + 4)
# TypeError: can only concatenate str (not "list") to str (Não podemos concatenar uma string e um número. Só funcionaria fazendo cast de int para string)

# Exemplos de IndexError

# Exemplo 1:
lista = ['Geek']
# print(lista[1])
# IndexError: list index out of range (Em nossa lista só existe item no índice 0, não existe índice 1)

# Exemplo 2:
print(lista[0][0]) # Imprimindo o índice 0 ('Geek'), mas só a posição 0 ('G')
# print(lista[0][10])
# IndexError: string index out of range (Em nossa lista o item do índice zero só tem 4 letras, portanto não tem posição 10)

# Exemplos de ValueError

# Exemplo 1:
# print(int('Geek'))
# ValueError: invalid literal for int() with base 10: 'Geek' (O cast int() espera receber como entrada uma string, então o argumento está correto, entretanto o valor é inapropriado, pois não é possível converter este valor "Geek" em um int)

# Exemplos de KeyError

# Exemplo 1:
dict = {}
# print(dict['Geek'])
# KeyError: 'Geek' (Estamos tentando acessar uma chave inexistente no dicionário em questão)

