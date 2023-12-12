"""
Tipo Float: tipo real, decimal
Casas decimais
OBS: O separador de casa decimais na programação é o ponto e não a vírgula.
"""

# Certo do ponto de vista float:
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição:
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter valores float para int. Obs: Perde-se precisão:
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos:
num_complex = 5j
print(num_complex)
print(type(num_complex))
teste = num_complex ** 2
print(teste)
print(type(teste))

# Podemos converter tipos int em float:
num = 1000000
print(num)
print(float(num))
