"""
Levantando os próprios erros com raise.

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.
Para simplificar, pense no raise como uma utilidade para criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de Erro')

OBS: O raise, assim como o return, finaliza a função, ou seja, nada após o raise é executado.
"""


# Exemplo 1:
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'azul')

"""
Explicando:
A função colore recebe dois parâmetros, texto e cor. É feita uma validação das entradas referente ao texto e a cor e se o usuário entrar com os argumentos com um tipo diferente do determinado pelo desenvolvedor, que seria string, o Python devolve um TypeError!
"""


# Exemplo 2 - Vamos refatorar nosso exemplo 1 e deixá-lo mais interessante:
def colorir(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colorir('Geek University', 'verde')
