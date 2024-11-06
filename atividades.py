"""
Módulo para a aula 148 de Testes Unitários
"""


def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma!'
    else:
        final = 'a gente só vive uma vez!'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return 'Putz! Dormi demais. Estou atrasado para o trabalho!'
    else:
        return 'Continuo cansado após dormir apenas 4 horas :('


# A partir daqui, faz parte da aula 149:


def eh_engracada(pessoa):
    comediantes = ['Jim Carrey', 'Bozo']
    if pessoa in comediantes:
        return True
    return False
