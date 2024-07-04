"""
O que são módulos?
    Em Python, módulos nada mais são do que outros arquivos Python.

E quais são as utilidades dos módulos?
    Os módulos são úteis para deixar nossos programas mais simples e para que possamos reutilizar os códigos.

Os módulos podem ser escritos por qualquer programador e depois compartilhado pela comunidade. Geralmente são criados
pacotes de módulos. Nós veremos isso mais à frente, mas é em formato de pacotes que os programadores compartilham suas
soluções para que outros possam usá-las.

Para usar os módulos é necessário instalá-los, se for o caso e importá-los. O módulo random, que estudaremos nessa aula
faz parte dos módulos integrados da linguagem Python. Isto significa que não precisa ser instalado, esse módulo já está
pronto para ser utilizado, basta importar.

O Módulo Random
    Possui várias funções para geração de números pseudo-aleatórios, ou seja, pode ser que não seja tão aleatórios
    assim, pode haver repetições.

Nesta aula conheceremos as principais funções deste módulo.
"""

# Existem duas formas de utilizar um módulo ou função deste!

# Forma 1 - Importando todo o módulo (não recomendado):

import random

"""
OBS: Ao realizar todo o módulo, todas as funções, atributos, classes, e propriedades que estiverem dentro do múdulo
    ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa deste módulo, então esta não
    seria a forma ideal de utilização.
    
Mas, então como saber quais funções existem dentro do módulo random?
    Como aprendemos no início do curso, basta usar dir(random) que será listado todas as propriedades que podemos
    utilizar de random!

Ok, mas como eu vejo como utilizá-las?
    Podemos utilizar o help(random) ou help(random.random)
"""

print('------------------- Primeiro exemplo de random --------------------')
# Função random() -> Gera um número aleatório entre 0 e 1.
print(f'Este é um número aleatório gerado pela função random: {random.random()}')

"""
Note que para usar a função random() do pacote random, nós colocamos no nome do pacote e o nome da função separados 
    por ponto: random.random()?

OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma
    função dentro do módulo random.

DICA: Se estiver no Pycharm, pode segurar o botão Ctrl e clicar em cima da palavra que representa o módulo random que
    seremos direcionados para o código fonte do random.
"""

# Forma 2 - Importando uma função específica do módulo (Forma recomendada):
from random import random

# Traduzindo: Do módulo random, importe a função random()

# Exemplo:
print('------------------- Segundo exemplo de random ---------------------')
for i in range(10):
    print(random())

print('--------- Gerando número aleatório de 0 a 100 com random() ---------')


# Gerando um número aleatório de 0 a 100:
def gera_aleatorio():
    print(round(random() * 100))


gera_aleatorio()

# Função uniform() - Gera um número pseudo-aleatório entre os valores estabelecidos:
from random import uniform

print('--------------------- Exemplo usando uniform() --------------------')
for i in range(10):
    print(uniform(3, 7))  # O 7 não é incluído!
# O uniform() é um random que vc escolhe o início e o fim do range de números. Se usar 0 e 1 é idêntico ao random


print('-------- Gerando número aleatório de 0 a 100 com uniform() --------')


# Gerando um número aleatório de 0 a 100:
def gera_aleatorio_uniform():
    print(round(uniform(1, 101)))


gera_aleatorio_uniform()

# Função randint() - Gera valores pseudo-aleatórios entre os valores estabelecidos:
print('-- Gerando números aleatórios para uma aposta na mega-sena com randint() --')
# Gerador de apostas para a Mega-sena:
from random import randint

for i in range(6):
    print(randint(1, 61), end=' ')  # Começa em 1 e vai até 60
print('')

print('-- Gerando jogadas aleatórias de joquempô com choice() --')
# Função choice() - Mostra um valor aleatório entre um iterável:
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

print('-- Gerando valores aleatórios de uma string com choice() --')
# Se fizermos a mesmas coisa com uma string:
print(choice('Geek University'))

print('------------- Embaralhando dados com shuffle() -------------')
# Função Shuffle() - Tem a função de embaralhar dados:
from random import shuffle

cartas = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

print(cartas)
shuffle(cartas)
print(cartas)

print('-- Tirando uma carta do baralho e mostrando com shuffle() --')
print(cartas[5])
