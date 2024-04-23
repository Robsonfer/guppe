"""
FUNÇÕES - São pequenos trechos de código que realizam tarefas específicas.
        - Pode ou não receber entradas de dados e retornar uma saída de dados.
        - Muito úteis para executar procedimentos similares por repetidas vezes.
OBS: Se você escrever uma função que realize várias tarefas dentro dela, é melhor realizar uma verificação para simplificar essa função.

Desde o início do curso, nós já utilizamos várias funções:
    - print()
    - len()
    - max()
    - count()
e muitas outras.
"""

# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python - print():
print(cores)

curso = 'Programação em Python Essencial'
print(curso)

# Mais um exemplo de função aplicada dentro da lista cores:
cores.append('roxo')
print(cores)

"""
Se tentarmos criar uma função curso.append('texto'), teremos um erro, pois o tipo string não tem o atributo append.
Isso quer dizer que algumas funções podem ser utilizadas com qualquer tipo de dados e simplemente chamadas.
Outras funções estão agregadas somente a alguns tipos de dados, como é o exemplo do append().
"""

# Existem funções que não recebem dados de entrada como acontece com print(), veja o exemplo do clear():
cores.clear()
print(cores)

"""
Princípio DRY - Don't Repeat Yourself: Define funções nativas como o print() para evitar que toda vez tenhamos que criar essas funcionalidades básicas novamente.

Mas como definir funções?

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
    - nome_da_funcao -> Sempre com letras minúsculas e se nome composto, sempre separado por underline (Snake Case);
    - parametros_de_entrada -> São opcionais. Tendo mais de um, são separados por vírgula;
    - bloco_da_funcao -> Também chamado de corpo da função ou implementação. É onde o processamento da função acontece. Neste bloco, pode haver ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também deve-se abrir o bloco de código com dois pontos : utilizados em Python para definir blocos.
"""

# Defindo nossa primeira função:
def diz_oi():
    print('Oi!')

"""
OBSERVAÇÕES IMPORTANTES:
    1 - Veja que dentro das nossas funções, podemos utilizar outras funções;
    2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
    3 - Veja que esta função não recebe nenhum parâmetro de entrada;
    4 - Veja que esta função não retorna nada.
"""

# Chamada de execução:
diz_oi()

# Atenção, nunca esqueça de utilizar os parênteses ao executar uma função!

# Exemplo 2:
def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens()

# Podemos repetir a função pra cantar duas vezes ou fazer um loop:
for n in range(2):
    print('-----')
    cantar_parabens()

# Em Python, podemos criar variáveis do tipo função e executar a função através da variável:
canta = cantar_parabens
canta()
# Isso é só pra curiosidade mesmo, pois é melhor sempre chamar a função!
