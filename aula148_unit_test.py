"""
Aula 148 - Introdução ao módulo Unittest

=======================================================================================================
ATENÇÃO - PARA ELUCIDAR MELHOR O FUNCIONAMENTO NA REALIDADE, TODOS OS TESTES ESTÃO NO ARQUIVO testes.py
    ASSIM COMO O PROGRAMA TESTADO ESTÁ NO ARQUIVO atividades.py
=======================================================================================================

Unittest - Testes unitários:
    É a forma de se testar unidades individuais de código fonte.
    Unidades individuais podem ser funções, métodos, classes, módulos e etc.

O objetivo destes testes unitários é mostrar que cada unidade atende corretamente a sua especificação e encontrar antecipadamente
    bugs e problemas em nossos códigos.

OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então, ganhamos todos os 'assertions'
    presentes no módulo que nos permitem testar todos os comportamentos de nossa unidade.

Para rodar nossos testes, utilizamos unittest.main()

TestCase - Casos de teste para sua unidade.

Para acessar a documentação do módulo Unittest do Python: https://docs.python.org/pt-br/3.13/library/unittest.html

CONHECENDO AS ASSERTIONS

MÉTODO                          VERIFICA SE
assertEqual(a, b)               a é igual b
assertNotEqual(a, b)            a é diferente b
assertTrue(x)                   x é verdadeiro
assertFalse(x)                  x é falso
assertIs(a, b)                  a é b
assertIsNot(a, b)               a não é b
assertIsNone(x)                 x é None
assertIsNotNone(x)              x não é None
assertIn(a, b)                  a está contido em b
assertNotIn(a, b)               a não está contido b
assertIsInstance(a, b)          a é instância de b
assertNotIsInstance(a, b)       não é instância de b

Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_

Para executar os testes com unittest:
    python nome_do_modulo.py

Para executar os testes com unittest no modo verbose (com detalhes):
    python nome_do_modulo.py -v

Docstrings nos testes:
    Podemos acrescentar e é recomnedado, Docstrings em nossos testes.
"""

# Prática - Utilizando a abordagem TDD. Para a prática, buscar os arquivos testes.py e atividades.py
# O arquivo testes.py testa os códigos do arquivo atividades.py
