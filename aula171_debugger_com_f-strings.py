"""
Aula 171 - Debugger mais simples com f-strings
"""


# Como usamos o f-strings:
# Exemplo 1:


def multiplicar(num1: float, num2: float) -> float:
    return num1 * num2


resultado: float = multiplicar(4.2345, 6.7890)

print(f'O resultado é {resultado}')

print(f'O resultado é {multiplicar(9, 4):.2f}')  # :.2f quer dizer que queremos o resultado com 2 casas decimais

# Exemplo 2 usando o operador walrus:

print(f'{(media := 8 / 2)} é a metade de {media * 2}')

# Utilizando o novo recurso:

geek: str = 'Geek University'

# Antes a forma de imprimir o nome da variável e seu valor em seguida era assim:
print(f"geek='{geek}'")

# Agora com o novo recurso, basta fazer assim:
print(f'{geek=}')

# Usando o mesmo recurso para inverter a string:
print(f'{geek.upper()[::-1]=}')

# Mas como assim fazer debugger? Exemplo:

# Podemos testar situações vendo o resultado junto com a expressão usada:
print(f'{geek.upper()[0:4:-1]=}')

# Ou:
print(f'{geek.upper()[:4:-1]=}')
