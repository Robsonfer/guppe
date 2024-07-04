"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos neste curso são
módulos Python prontos para serem utilizados.
"""

# Importando uma função específica do nosso módulo!
from aula083_modulo_de_teste import gera_aleatorio

gera_aleatorio()


# Importando nosso módulo inteiro:
import aula083_modulo_de_teste as mt

# from aula083_modulo_de_teste import *

mt.gera_aleatorio_uniform()

"""
OBSERVAÇÃO IMPORTANTE: Na aula o professor usa uma aula antiga para importar uma função. Eu criei um arquivo novo
para fazer o teste!

OBS: importei usando alias, mas tbm poderia importar usando *. Isso evitaria ficar chamando a função com o alias!
"""
