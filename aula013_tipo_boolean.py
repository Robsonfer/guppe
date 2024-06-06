"""
Tipo Boolean: Àlgebra Booleana, criada por George Boole

2 constantes = True e False
"""
print('Imprimindo ativo quando True:')
ativo = True
print(ativo)
print('Imprimindo ativo quando False:')
ativo = False
print(ativo)

# Operações básicas:

# Negação (not):
print('Negando o resultado da variável ativo:')
print(not ativo)

# Ou (or):
print('Encontrando Verdadeiro ou Falso na combinação entre x e y:')
x = False
y = False
z = x or y
print(z)

print('Encontrando Verdadeiro entre a e c:')
# E (and):
a = True
b = True
c = a and b
print(c)

# Outras formas de usar boolean:
print('Cinco é maior do que seis?')
print(5 > 6)
print('Seis é maior do que cinco?')
print(6 > 5)
print('Seis é igual a seis?')
print(6 == 6)
print('Quatro é menor ou igual a seis')
print(4 <= 6)
