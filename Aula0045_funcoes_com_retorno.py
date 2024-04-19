"""
Funções com retorno
"""

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'Retonro de print: {ret_pr}')

"""
No exemplo acima criamos uma lista com três números, depois uma variável pra receber a informação da função numeros.pop()
Quando imprimimos o retorno de pop, temos como resultado o número 3 que por sua vez é o retorno da função pop(), ou seja, esta função retorna não somente o valor que foi removido como também a lista com esse item a menos.
Também criamos uma variável que recebe o resultado de print() que é uma função que não retorna nada.
Ao imprimir essa variável fica muito claro que a função print() não retorna nada, pois o resultado dela é None.
"""

# Exemplo função
def quadrado_de_7():
    print(7*7)

ret = quadrado_de_7()

print(f'Retorno da função quadrado_de_7: {ret}')
# Veja que a função acima não retonar nada também, só imprimi. Imprimir (print), não é retornar!
# Em Python quando uma função não retorna nenhum valor, o retorno é None.

# Refatorando a função pra retornar o valor:
def quadrado_de_5():
    return 5*5

retorno = quadrado_de_5()
print(f'Retorno da função quadrado_de_5: {retorno}')

# Parei em 11:10!
