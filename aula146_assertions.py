"""
Aula 146 - Assertions - Afirmações (checagens/questionamentos)

Em Python utilizamos a palavra reservada 'assert' para realizar simples afirmações utilizadas nos testes.

Utilizamos o 'assert' numa expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, o 'assert' retorna None e caso seja falsa, levanta um erro do tipo AssertionError.

OBS: Nós podemos especificar ocasionalmente um segundo argumento ou mesmo uma mensagem de erro personalizada.

OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código. Não precisa ser exclusivamente nos testes.
"""


def soma_numeros_positovos(a, b):
    assert a > 0 and b > 0, 'Atenção! Ambos os números precisam ser positivos!'
    return a + b


ret = soma_numeros_positovos(2, -2)

print(ret)
