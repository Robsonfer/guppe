"""
Expressões Lambda
Conhecidas por expressões lambdas ou simplesmente lambdas, são funções sem nome, ou seja, funções anônimas.
"""
# Função comum:
def funcao(x):
    return 3 * x + 1
print(funcao(4))
print(funcao(7))

# Expressão Lambda resolvendo a mesma função acima:
lambda x: 3 * x + 1
# Mas essa expressão não tem chamada, pois ela não tem nome!

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))
# Mas essa forma de criar uma variável ainda não é a forma ideal de utilizar a expressão lambda ainda.

# Podemos ter expressões lambdas com múltiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' angelina ', '  JOLIE'))
print(nome_completo(' FELICITY ', '  jones   '))
# strip() remove os espaços em branco no início e no fim da variável
# title() transforma toda primeira letra de uma string em maíuscula

# Em funções Python podemos ter: nenhuma ou várias entradas. Em Lambdas também:
zero_entrada = lambda : 'Como não amar Python?'
uma_entrada = lambda x: 3 * x + 1
duas_entradas = lambda x, y: (x * y) ** 0.5
tres_entradas = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(zero_entrada())
print(uma_entrada(6))
print(duas_entradas(5, 7))
print(tres_entradas(3, 6, 9))
# OBS: Se passarmos mais argumentos do que o parâmetros informados, teremos TypeError

# Exemplo da forma mais comum do uso do lambda sem definir variável:
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlen', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']
print(autores)

# Imagine que precisemos ordenar pelo sobrenome dos autores
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
# O split() cria uma lista separando o que queremos da forma que solicitarmos, aqui separa a cada espaço.
# O [-1] busca o último item da lista criada com o split.
# O lower() transforma tudo em minúsculo pra ficar tudo igual
"""
OBS: Fiz o teste tirando o lower() e só da problema se houver um erro de digitação, ou seja, 
se um dos sobrenomes etiver digitado tudo em minúsculo, então é uma forma de padronizar e evitar erros!
"""

# Função Quadrática f(x) = a * x + b * x + c

# Definindo a função:
def geradora_funcao_quadratica(a, b, c):
    """
    Retorna a função f(x) = a*x**2 + b*x + c
    :param a: x ao quadrado da função
    :param b: somente multiplicação por x
    :param c: somente número
    :return: resultado da função (equação do segundo grau)
    """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
"""
Traduzindo: No caso explicado acima, a função geradora_funcao_quadratica() serve para determina quanto é a, b e c
da equação do segundo grau. E a expressão lambda serve para determinar quanto é o x.
"""

print(geradora_funcao_quadratica(3, 0, 1)(2))
# No exemplo do print acima, descartamos a variável teste e chamamos tudo direto dentro do print!

