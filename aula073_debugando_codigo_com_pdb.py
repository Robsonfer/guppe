"""
Debugando códigos com PDB (Python Debugger).

Bug -> Inseto
"""

# Alguns programadores usam print para debuggar códigos, entretanto essa é uma prática ruim:

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'WARNING! {err}.'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug, utilizando o debugger.
# Em Python podemos fazer isso em diferentes IDEs como o Pycharm ou utilizando o PDB - Python Debugger.

# Exemplo com o Pycharm:

def dividir(a, b):
    try:
        return float(a) / float(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'WARNING! {err}.'

print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger:

