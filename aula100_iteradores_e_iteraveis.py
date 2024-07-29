"""
Entendendo Iterators e Iterables

Iterator:
    - Objeto que pode ser iterado;
    - Objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

Iterable:
    - Objeto que irá retornar um iterador quando a função iter() for chamada.
"""

nome = 'Geek' # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6] # É um iterable, mas não é um iterator

print(nome)
print(numeros)

# print(next(nome)) # TypeError: 'str' object is not an iterator
# print(next(numeros)) # TypeError: 'str' object is not an iterator


# Então para iterar com next, precisamos converter os itens em iterators:
it1 = iter(nome)
it2 = iter(numeros)

# Agora podemos iterar um a um:
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# E se tentarmos usar mais um next(it1) dará um StopIteration Error!

# Da mesma forma com os números:
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))


# Por baixo dos panos quando usamos um for, é a mesma coisa que acontece do next acima:
for letra in nome:
    print(f'{letra}')
# O Python não deixa chegar no erro de StopIteration
