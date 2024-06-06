"""
Loop while

Forma Geral:
while expressao_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso. Exemplos:

num = 5
num < 5
"""

# Exemplo 1:
numero = 1

while numero < 10:
    print(numero)
    numero += 1
# OBS: em um loop while é importante que cuidemos do critério de parada para evitar loop infinito.

# Exemplo 2:
resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ').lower()
