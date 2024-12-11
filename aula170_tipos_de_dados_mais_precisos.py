"""
Aula 170 - Tipos de dados mais precisos
"""
import typing

from mypy.build import TypedDict


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

# *** LITERAL TYPE *** : Indica que um parâmetro ou retorno é forçado a um ou mais valores literais específicos.
from typing import Literal, Union, Final, final


# Exemplo:


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')  # !r destaca o argumento da operação com erro entre aspas


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


# *** Union *** - Determina o retorno de dois tipos:


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    else:
        return resultado


print(soma(25, 25))

# *** Final *** - Utiliza-se para criar constantes:

NOME: Final = 'Geek'

print(NOME)

"""
    Importante: Em Python, mesmo criando uma constante, podemos alterar.
    Mas se rodar mypy neste arquivo, seremos avisados.
"""

NOME = 'University'

print(NOME)

# Outro tipo de final é com um decorator para classe:


@final
class Pessoa:
    pass


class Estudante(Pessoa): # Quando usamos @final, queremos dizer que nenhuma outra classe pode estender a classe decorada
    pass

    @final # Ao usar o decorator final em um método, dizemos que as classes filhas desta classe não podem sobrescrever este método.
    def estudar(self):
        print('Estou estudando')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando!')

# Importante, a linguagem Pyhon não vai nos impedir de fazer isso. O único caminho de checage é o mypy

# *** Typed Dictionaries *** :

class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)

# Neste caso o Python tbm vai processar, mas no mypy tbm vai dar erro, assim como abaixo pela própria IDE:
outro = CursoPython(algo='vai', coisa=True)
print(outro)


# *** Protocols ***

class Curso(Protocol):
    titulo: str

def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')
