"""
Aula 160 - Type Hinting


"""


# Exemplo:


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Robson'))


# Exemplo 2 - Teste:


def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))
