"""
Aula 146 - Assertions - Afirmações (checagens/questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' numa expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o 'assert' retorna None e caso seja falsa, levanta um erro do tipo AssertionError.

OBS: Nós podemos especificar ocasionalmente um segundo argumento ou mesmo uma mensagem de erro personalizada.

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código. Não precisa ser exclusivamente nos testes.

ALERTA: Cuidado ao utilizar o 'assert'.
    Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado.
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Atenção! Ambos os números precisam ser positivos!'
    return a + b


ret = soma_numeros_positivos(2, 2)  # Ok
# ret = soma_numeros_positivos(2, -2) # AssertionError

print(ret)


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata frita',
        'cachorro quente'
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


comida = input('Informe a comida: ')

print(comer_fast_food(comida))
