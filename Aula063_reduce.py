"""
Reduce

A partir da versão 3 do Python a função reduce() não é mais uma função integrada (built-in) do Python.
Agora temos que importar e utilizar esta função a partir do módulo "functools".

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes
    um loop for é mais legível.

Para entender o reduce():
    Imagine que você tenha uma coleção de dados:
        dados = [a1, a2, a3, ..., an]
    E você tem uma função que recebe dois parâmetros:
        def funcao(x, y):
            return x * y

    Assim como map() e filter() a função reduce() recebe dois parâmetros:
        A função e o iterável: reduce(funcao, dados)

    A função reduce() funciona da seguinte forma:
        Passo 1: res = funcao(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resutado
        Passo 2: res = funcao(res, a3) # Aplica a função passando o resultado do passo 1 + o terceiro elemento
            e guarda o resultado.
        Isso se repete até o final. Ou seja, em cada passo ela aplica a função passando como primeiro argumento o
            resultado da aplicação anterior. No final, reduce() retornará o resultado final.

Uma forma de explcar graficamente o que acontece é a seguinte:

funcao(funcao(funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista:

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Mesma função utilizando um loop normal:
resultado = 1
for n in dados:
    resultado *= n

print(resultado)

# Se não utilizarmos dois parâmetros, teremos TypeError
