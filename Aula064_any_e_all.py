"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False
"""

# Exemplo all():
print(all([0, 1, 2, 3, 4])) # De 1 a 4 sabemos que é True, mas o 0 é False
print(all([1, 2, 3, 4, 5])) # True
print(all([])) # True porque a lista é vazia

# O iterável pode ser lista, tupla, set, string ou dict

# Exemplo 2 de all():
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(f'Todos os nomes começam com C? {all(nome[0] == 'C' for nome in nomes)}')
print(f'Todos os nomes começam com C? {all([nome[0] == 'C' for nome in nomes])}')

# Exemplo 3 de all():
print(f'Tem eio em aeiou? {all(letra for letra in 'eio' if letra in 'aeiou')}')
"""
Traduzindo em etapas:
    for letra in 'eio' -> para cada letra em 'eio';
    letra -> retorne a letra
    if letra in 'aeiou' -> e compare, se existe em 'aeiou'
    all() -> e retorne True se tiver, False se não tiver.
"""
# OBS: Um iterável vazio convertido em boolean é falso, mas o all() entende como True

# Correção do código acima feito por um aluno
print(all([True if letra in 'aeiou' else False for letra in 'xyz']))

# Exemplo 4 em all():
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
# Traduzindo: gerar uma lista para cada numero da lista num se o número for par
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))
# Ainda que pedirmos por ímpar, o resultado será True, pois lista vazia para all() tbm é True

print('---- Exemplos any() ----')

# Exemplo 1 de any():
print(any([0, 1, 2, 3, 4])) # De 0 a 4 sabemos que o 0 é False, mas em any() basta que 1 item seja True
print(any([])) # False porque a lista é vazia
print(any([0, False, {}, (), []])) # False porque todos os elementos da lista são False

# Retornando a lista de nomes com any():
print(any([nome[0] == 'C' for nome in nomes]))

# Reconhecendo números pares com any():
print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
# O any() funciona como uma pergunta se há numeros pares na lista

"""
all() funciona como um 'and', ou seja, se A = 1 e B = 1, A*B = True
any() funciona como um 'or', ou seja, se A = 1 ou B = 1, A+B = True
"""
