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


# Contando até 10 e usando um loop for:
gen10 = conta_ate(10)

for num in gen10:
    print(num)


# Se a gente trabalhar mesclando:
gen_mesc = conta_ate(10)

print(next(gen_mesc)) # 1
print(next(gen_mesc)) # 2

print('Até aqui foi com next!')

for num in gen_mesc: # de 3 a 10!
    print(num)


# E pode acontecer de eu precisar gerar tudo de uma vez. Uma fora é:
gen_all = list(conta_ate(10))

print(gen_all)
