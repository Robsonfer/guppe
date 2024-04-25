"""
Documentando funções com Docstrings

OBS: Podemos ter acesso à documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso à documentação com a função help()
"""

# Exemplo 1:
def diz_oi():
    """
    Uma função simples que retorna a string 'Oi! '
    :return: 'Oi! '
    """
    return 'Oi! '

from Aula048_docstrings import diz_oi

print(diz_oi())

help(diz_oi) # Acessando o help da nossa função!

print(diz_oi.__doc__) # Acessando a documentação da nossa função!

# Exemplo 2:
def exponencial(numero, potencia=2):
    """
    Função que calcula o quadrado de um número qualquer ou da potência informada.
    :param numero: Número desejado como base da potência
    :param potencia: Número desejado como potência (padrão = 2)
    :return: Retorna o cálculo de potência de acordo com os números informados pelo usuário.
    """
    return numero ** potencia
print(exponencial.__doc__)

print(help(exponencial))
