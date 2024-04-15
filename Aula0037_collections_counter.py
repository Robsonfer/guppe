"""
Módulo Collections - Counter

Collections -> Hight-performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter, que é parecido
    com um dicionário que contém como chave o elemento da lista passada como parâmetro e como valor a
    quantidade de ocorrências deste elemento.

Documentação: https://docs.python.org/3/library/collections.html#collections.Counter
"""

# Realizando o import
from collections import Counter

# Exemplo 1:

# Podemos utilizar qualquer iterável
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# utilizando o Counter
resultado = Counter(lista)

print(type(resultado))
print(resultado)

# Veja que para cada elemento da lista gerada, o Counter crio uma chave e colocou como valor a quantidade de vezes que a chave se repete.

# Exemplo 2:

print(Counter('Geek University'))

# Exemplo 3:

texto = """A Apollo 5, também chamada de AS-204, foi um voo espacial não-tripulado norte-americano e o primeiro voo teste do Módulo Lunar Apollo, que depois levaria astronautas para a superfície lunar. Ela foi lançada por um foguete Saturno IB em 22 de janeiro de 1968 do Complexo de Lançamento 37 em Cabo Kennedy, na Flórida. A missão foi um sucesso, porém problemas de programação forçaram a execução de uma missão alternativa em relação a aquela que tinha sido originalmente planejada."""

palavras = texto.split()
print(palavras)

resultado2 = Counter(palavras)
print(resultado2)

# Encontrando as 10 palavras com mais ocorrência no texto:
print(resultado2.most_common(10))
