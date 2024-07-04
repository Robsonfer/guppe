"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste curso são
módulos Python prontos para serem utilizados.
"""

# Importando uma função específica do nosso módulo. A função importada é a gera_aleatorio():
from aula083_modulo_de_teste import gera_aleatorio

gera_aleatorio()


# Importando um módulo inteiro:
import aula083_modulo_de_teste as mt

# from aula083_modulo_de_teste import *
mt.gera_aleatorio_uniform()


"""
OBSERVAÇÃO IMPORTANTE: Na aula o professor usa uma aula antiga para importar uma função, mas tive problemas com o
print das funções e como não quero mudar a estrutura das aulas para que possa voltar e revisar o conteúdo, então eu
criei um arquivo novo completamente do zero (aula083_modulo_de_teste.py) para fazer esta aula e entender como
funciona todo o processo do começo ao fim!

OBSERVAÇÃO IMPORTANTE: Neste segundo exemplo eu importei usando alias, mas tbm poderia importar usando *. Importar
usando o * deixaria o código mais limpo porque evitaria ficar chamando o módulo antes da função
(mt.gera_aleatorio_uniform()), visto que nós estamos importando o módulo inteiro.
"""


# Acessando e imprimindo variáveis de outro módulo:
print(f'Esta lista vem de outro módulo: {mt.lista}')
print(f'Esta tupla vem de outro módulo: {mt.tupla}')

# Usando uma função e uma variável importadas de outro módulo simultaneamente:
print(f'Essa é a soma dos números ímpares da lista do outro módulo: {mt.soma_impares(mt.lista)}')

# Peguei mais funções de outros módulos e colei no módulo de teste:
print(f'Mais um caso de função e variável de outro módulo: {list(map(mt.c_to_f, mt.cidades))}')
