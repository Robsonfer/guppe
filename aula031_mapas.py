"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representandos por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(f'Este é o dicionário receita: {receita}')

# Iterar sobre dicionários

# Para cada chave dentro de receita, imprima a chave:
for chave in receita:
    print(chave)

# Para cada chave dentro de receita, imprima o valor da receita:
for chave in receita:
    print(receita[chave])

# Para cada chave dentro de receita, imprima a chave e o valor da receita:
for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Podemos ainda personalizar o exemplo anterior:
for chave in receita:
    print(f'Em {chave} a receita foi de R$ {receita[chave]},00')

# Tendo acesso direto a todas às chaves:
print(receita.keys())

# Podemos usar o .keys() para fazer o for.
# Para cada chave dentro de receita.keys(), imprima o valor da receita:
for chave in receita.keys():
    print(receita[chave])
# Essa é a forma recomendada de fazer a iteração!

# Tendo acesso direto a todos os valores:
print(receita.values())

# E também podemos fazer um for em cima disso
# Para cada valor dentro de receita.values() imprima o valor:
for valor in receita.values():
    print(valor)
# Notar que a expressão do for aceita tanto chave quanto valor para iterar!
# Esta também é a forma correta de fazer a Iteração!

# Desempacotamento de Dicionários:
print(receita.items())
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho.
# * Somente se os valores forem inteiros ou reais.
print(f'Esta é a soma dos valores deste dicionário: {sum(receita.values())}')
print(f'Este é o valor máximo deste dicionário: {max(receita.values())}')
print(f'Este é o valor mínimo deste dicionário: {min(receita.values())}')
print(f'Este é o tamanho deste dicionário: {len(receita.values())}')
