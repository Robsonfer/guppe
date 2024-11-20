"""
Aula 160 - Type Hinting
"""

# Exemplo:


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
print(cabecalho('geek university', alinhamento='geek'))
