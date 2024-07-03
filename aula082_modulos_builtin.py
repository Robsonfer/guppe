"""
Trabalhando com Módulos Built-in (Módulos Integrados)

 Quando instalamos o Python, os módulos built-in vêm todos juntos com o Python, entretanto, enquanto usamos o Python
 puro, estes módulos não são carregados durante esse uso, eles só são carregados mediante o um comando de import.

 Uma forma interesssante mostrada em aula foi que ao abrir o terminal do Python, o professor deu um comando dir() e o
 que o Python trouxe foram sete módulos>

dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

Mas quando fazemos um import do random por exemplo, aí já temos um módulo a mais que é o próprio random:

import random
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'random']

Desta forma, estes módulos já estão na máquina, porém não são utilizados. Isto faz parte da otimização do Python para
que a memória de utilização do Python não se sobrecarregue. O Python é uma linguagem otimizada de todas as formas.

Lista de Módulos Built-in dentro do Python:
https://docs.python.org/3/py-modindex.html
"""

# Utilizando alias (apelidos) para módulos/funções
"""
import random as rdm

print(rdm.random())
"""

# Podemos importar todas as funções de um módulo utilizando o *
from random import *

