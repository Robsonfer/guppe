"""
Generator Expression

Em aulas anteriores vimos list comprehension, dictionary comprehension e set comprehension, mas não vimos tuple
    comprehension. Não vimos pq elas se chamam generators.

Na aula anterior usamos o all() e o any() e criamos o seguinte código:
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

"""
Visualmente a única diferença entre o List Comprehension e o Generator são os colchetes e parênteses,
mas por trás temos outra diferença:
    - Performance: O Generator é mais performático e consome menos recursos da sua máquina. Basta ver a
        resposta impressa no print() onde para o List Comprehension temos a lista em memória e para o
        generator, só temos o objeto generator!

E quando usamos um ou outro?
    - Usamos o List Comprehension quando precisarmos da lista para alguma utilização.
    - Usamos o generator quando precisamos somente checar uma informação.
"""

# Provando a difernça de performance:

# O getsizeof retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostrando quantos bytes a string está ocupando em memória. quanto maior a string, mais espaço ocupa:
print(f'Testando o getsizeof. A string Geek tem {getsizeof('Geek')} bytes')
print(f'Testando o getsizeof. A string University tem {getsizeof('University')} bytes')
print(f'Testando o getsizeof. O número 9 tem {getsizeof(9)} bytes')
print(f'Testando o getsizeof. O número 91 tem {getsizeof(91)} bytes')
print(f'Testando o getsizeof. O número 92345668823 tem {getsizeof(92345668823)} bytes')
print(f'Testando o getsizeof. O booleano True tem {getsizeof(True)} bytes')

# Gerando uma lista de números com o list comprehension:
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com o set comprehension:
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com o dictionary comprehension:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com o generator:
generator = getsizeof(x * 10 for x in range(1000))

print('----- comparando tamanhos -----')

print('Para fazer a mesma tarefa, gastamos em memória:')
print(f'Com List Comprehension: {list_comp} bytes')
print(f'Com List Set Comprehension: {set_comp} bytes')
print(f'Com Dictionary Comprehension: {dict_comp} bytes')
print(f'Com Generator Expression: {generator} bytes')

# Como podemos iterar no Generator Expression:
gen = (x * 10 for x in range(20))
print(gen)
print(type(gen))
for num in gen:
    print(num)
