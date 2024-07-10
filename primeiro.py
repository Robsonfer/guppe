
def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado. {__name__}')

# OBS: Geralmente esse else não é usado. Aqui é só para demonstrar o momento de execução!
