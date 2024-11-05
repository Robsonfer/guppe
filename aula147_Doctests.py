"""
Aula 147 - Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

Para rodar um teste do doctest:
    No Pycharm, ao rodar o script como o desta aula ele vai retornar o resultado dizendo que iniciou o teste e dará
        até um horário de início do teste, entretanto, você não terá o resultado do teste.
    Para ter resultado direto do teste, devemos ir ao terminal proceder da seguinte forma:
        python -m doctest -v aula147_Doctests.py (lembrando que depois de -v deve vir o nome do programa com a
        extensão.

____________________________________________________________________________
Resultado do teste com sucesso:

7
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 item had no tests:
    aula147_Doctests
1 item passed all tests:
   1 test in aula147_Doctests.soma
1 test in 2 items.
1 passed.
Test passed.

# Explicando o resultado do teste:
    1 - Note que primeiro ele dá o resultado da função (7);
    2 - Logo em seguida ele menciona uma possibilidade de entrada, o que está a testar e o resultado esperado;
    3 - Na sequência, ele dá uma resposta de ok, avisando que o teste foi realizado com sucesso;
    4 - Depois menciona os itens testados e finaliza somando quantos deles passaram no teste;
    5 - E por fim, dá o resulado final: Test passed.
____________________________________________________________________________
Resultado do teste com erro:

7
Trying:
    soma(12, 2)
Expecting:
    3
**********************************************************************
Failed example:
    soma(12, 2)
Expected:
    3
Got:
    14
1 item had no tests:
    aula147_Doctests
**********************************************************************
1 item had failures:
   1 of   1 in aula147_Doctests.soma
1 test in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failure.

# Explcando o resultado do teste:
    1 - Note que primeiro ele dá o resultado da função (7);
    2 - Logo em seguida ele menciona uma possibilidade de entrada, o que está a testar e o resultado esperado;
    3 - Na sequência, ele avisa que o exemplo falhou;
        a - Mostra novamente o que mostrou no passo 2, mas devolve um Got: 14, resultado obitido diverente do esperado!
    4 - Depois menciona os itens testados e finaliza somando quantos deles passaram no teste e quantos falharam;
    5 - E por fim, dá o resulado final: ***Test Failed*** 1 failure.
"""


def soma(a, b):
    """
    Soma os valores das variáveis a e b
    >>> soma(1, 2)
    3
    >>> soma(4, 6)
    10
    """
    return a + b


print(soma(3, 4))


# Outro exemplo, aplicando o TDD:

def duplicar(valores):
    """
    Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    >>> duplicar([])
    []
    >>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]


# Erro inesperado...


def fala_oi():
    """
    Fala oi

    >>> fala_oi()
    "oi"
    """
    return "oi"

# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.


# Mais um caso estranho:


def verdade():
    """
    Retorna verdade

    >>> verdade()
    True  
    """
    return True

