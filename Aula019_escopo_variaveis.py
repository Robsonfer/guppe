"""
Escopo de variáveis

Dois casos de esocpo:

1 - Variáveis globais;
    - Seu escopo compreende todo o programa, ou seja, são reconhecidas em todo o programa.

2 - Variáveis locais;
    - São reconhecidas apenas no bloco onde foram declaradas.

Para declarar variáveis em Python:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica.
"""

# Esse é um exemplo de variável global:
numero = 42
print(numero)
print(type(numero))

# reatribuição não é possível em linguagens de tipagem fixa
numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

# Esse é um exemplo de variável local:
if numero > 10:
    novo = numero + 10
    print(novo)

"""
Na lógica do bloco acima, se a variável número for processada e alimentar a variável novo, quando eu gerar um
print dela teremos o resultado da lógica, mas caso contrário, o código vai dar um erro, pois a variável novo nunca
foi alimentada com valor algum, ou seja, ela nunca foi gerada.
"""
print(novo)
