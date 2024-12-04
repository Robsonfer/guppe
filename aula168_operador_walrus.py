"""
Aula 168 - Operador Walrus

O Operador Walrus permite fazer a atribuição e o retorno de valor numa única expressão:

variável := expressão
"""

nome = 'Geek University'
print(nome)
# No caso anterior a gente primeiro atribui a variável e somente depois imprime.

print(nome1 := 'Robson Ferreira')
# Neste caso fazemos ao mesmo tempo, declarar a variável, atribuir o valor da variável e imprimir esta variável


# Exemplo antes do walrus:
"""
cesta = []
fruta = input('Informe uma fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe uma fruta: ')
"""

# Exemplo depois do walrus:

cesta = []
while (fruta := input('Informe uma fruta: ')) != 'jaca':
    cesta.append(fruta)
# O operador walrus recebe o valor, atribui o valor e retorna o valor, ou seja, deixa a variável disponível para uso.

print(cesta)

"""
Mas quando eu devo usar o operador walrus?
    Quando você quiser e achar necessário. O importante é conhecer o recurso!
"""
