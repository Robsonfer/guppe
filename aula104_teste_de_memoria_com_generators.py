"""
Teste de memória com Generators

# Sequência de Fibonacci: 
1, 1, 2, 3, 5, 8, 13, 21...

"""

# FUNÇÃO USANDO LISTAS 43MB:
"""
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

# Teste 1:
for n in fib_lista(10000):
    print(n)
"""


# FUNCÃO USANDO GERADORES:
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

# Teste 2:
for n in fib_gen(10000):
    print(n)
