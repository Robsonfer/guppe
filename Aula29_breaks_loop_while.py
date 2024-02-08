"""
Saindo de loops com break

Utilizamos o break para sair de loops de maneira projetada.
"""

# Exemplo 1 (Com for)
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)

print('Sair do Loop!')

# Exemplo 2 (Com while)
while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break

print('Você digitou sair!')