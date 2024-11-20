"""
Aula 161 - Checagem de tipos com MyPy

Para rodar o programa com MyPy:
mypy <nome_do_programa.py>
mypy aula161_checagem_tipos_mypy.py

IMPORTANTE: Para que o MyPy funcione, não adianta codificar no formato padrão do Python, sem o type hinting.
    É preciso usar o type hinting em todo o código. Não usar vai maquiar o resultado.
"""

def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Robson'))


# Exemplo 2 - Teste:


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))

# Em aula o professor mostra que errar o tipo não trava o programa, mas nesta versão da IDE ele avisa do erro!
print(cabecalho('geek university', alinhamento=True))
