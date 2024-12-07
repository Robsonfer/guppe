"""
Aula 170 - Tipos de dados mais precisos
"""
import typing


def dobro(valor: int) -> int:
    return valor * 2


"""
Note que embora declaramos que valor é do tipo int e ainda que a string avise o erro dentro do segundo print abaixo,
    o Python calcula o resultado como GeekGeek, ou seja, o valor duplicado. Isso se dá porque mesmo com Type Hinting
    O python ainda é uma linguagem de tipagem dinâminca e muito forte.
"""
print(dobro(8))
print(dobro('Geek'))

"""
Tipos mais preciso:
    - Literal type
    - Union
    - Final
    - Typed Dictionaries
    - Protocols
"""

# LITERAL TYPE: Indica que um parâmetro ou retorno é forçado a um ou mais valores literais específicos.
from typing import Literal, Union, Final


# Exemplo:


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}') # !r destaca o argumento da operação com erro entre aspas


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
# calcula_v1('*', 3, 5)


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
# calcula_v2('*', 3, 5)


# Union - Determina o retorno de dois tipos:


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado


print(soma(25, 25))


# Final - Utiliza-se para criar constantes:

NOME: Final = 'Geek'

print(NOME)