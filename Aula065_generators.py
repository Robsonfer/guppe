"""
Generators

Em aulas anteriores vimos list comprehension, dictionary comprehension e set comprehension, mas não vimos tuple
    comprehension. Não vimos pq elas se chamam generators.

Na aula anterior fizemos usamos o all() e o any() e criamos o seguinte código:
    nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
    print(any([nome[0] == 'C' for nome in nomes]))
Mas poderíamos ter feito com Generators
"""

# Exemplo acima com Generators:
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))

# Verificando o retorno como list Comprehension:
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Verificando o retorno como Generator:
res2 = (nome[0] == 'C' for nome in nomes)
print(type(res2))
print(res2)
# OBS: O Generator não retorna uma tupla!
# Mas podemos gerar para conferência, entretanto assim como o map() e o filter(), uma vez usado é apagado da memória.
print(tuple(res2))

print(f'Segunda chamada de print do generator: {tuple(res2)}')
