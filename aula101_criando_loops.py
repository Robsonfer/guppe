"""
Criando sua própria versão de loop

# Como é que fazemos:
for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

# O que o Python faz por trás:
iter([1, 2, 3, 4, 5])

iter('Geek Uversity')

"""

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Geek University')

numeros = range(11)

meu_for(numeros)
