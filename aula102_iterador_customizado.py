"""
Escrevendo um iterador customizado
"""

# Escrevendo um contador igual ao range:
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration

for n in Contador(1, 61):
    print(n)


# O que foi feito acima é basicamente o mesmo que:
for n in range(1, 61):
    print(n)
