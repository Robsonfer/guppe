"""
Geradores

Os Geradores, conhecidos como Generators são Interators (Iteradores).

OBS: O contrário não é verdadeiro, ou seja, nem todo Iterator é um Generator.

Outras informações:
    - Generators podem ser criados com funções geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com expressões geradoras.

Diferenças entre Funções e Generator Functions (Funções Geradoras):
-------------------------------------------------------------------------------
|               FUNÇÕES              |            FUNÇÕES GERADORAS           |
-------------------------------------------------------------------------------
| Utilizam return                    | Utilizam yield                         |
-------------------------------------------------------------------------------
| Retorna uma vez                    | Pode utilizar yield múltiplas vezes    |
-------------------------------------------------------------------------------
| Quando executada, retorna um valor | Quando executada, retorna um generator |
-------------------------------------------------------------------------------

"""

# Exemplo de Generator Function:

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Uma generator function não é um generator, ela gera um generator.


# Contando até 5 e usando next:
gen = conta_ate(5)

print(type(gen))
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Conando até 10 e usando um loop for:
gen10 = conta_ate(10)

for num in gen10:
    print(num)
