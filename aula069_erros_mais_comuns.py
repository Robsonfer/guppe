"""
Erros mais comuns em Python

ATENÇÃO! É muito importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comum:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreve algo que o Python não reconhece como parte da linguagem.

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

3 - TyoeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
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

