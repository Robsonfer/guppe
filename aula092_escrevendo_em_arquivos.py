"""
Escrevendo em arquvos

Até aqui aprendemos que por padrão a função open() abre os arquivos no modo 'r' de leitura. Aqui então aprenderemos
como abrir um arquivo para edição.

OBSERVAÇÃO IMPORTANTE: Quando abrimos um arquivo para leitura, não podemos realizar escrita nele, somente ler.
Da mesma forma, quando abrimos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Diferenças entre abrir um arquivo para leitura e um arquivo para escrita:
- A primeira diferença que podemos notar é que ao abrir um arquivo para escrita um novo arquivo é criado.
- A Segunda diferença é que informamos o modo como segundo parâmetro da função open. No caso da leitura,
já é padrão vir como modo r, então não precisamos informar o modo, já no caso da escrita, é essencial informar.

Para escrevermos dados em um arquivo, após abrir o arquivo, utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário, teremos um TypeError.

Abrindo um arquivo já existente para escrita com o modo 'w', o conteúdo anterior será apagado e um novo conteúdo será
criado. Dessa forma, o conteúdo anterior é perdido.
"""

# Exemplo de escrita - modo 'w' (write)
"""
with open('novo.txt', 'w') as arquivo:
    arquivo.write('É muito fácil escrever dados em um arquivo.\n')
    arquivo.write('Pdemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.\n')
"""

# Somente para provar que não há diferença, vamos criar um exemplo na forma tradicional, sem with:
"""
arquivo = open('mais.txt', 'w')
arquivo.write('+--------------------------------------------------------------+\n')
arquivo.write('|                  TABELA DE DADOS DA FAMÍLIA                  |\n')
arquivo.write('|--------------------------------------------------------------|\n')
arquivo.write('|        Nome        |      Sobrenome     |        Idade       |\n')
arquivo.write('|--------------------------------------------------------------|\n')
arquivo.write('|      Robson        |      Ferreira      |         43         |\n')
arquivo.write('|--------------------------------------------------------------|\n')
arquivo.write('|      Gabriel       |      Santini       |         14         |\n')
arquivo.write('|--------------------------------------------------------------|\n')
arquivo.write('|      Rosângela     |      Santini       |         42         |\n')
arquivo.write('+--------------------+--------------------+--------------------+\n')
arquivo.close()
"""

# Podemos fazer também o texto multiplicado. É uma propriedade do tipo string:
"""
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Estou repetindo este texto trinta vezes!\n' * 30)
"""

# Podemos também fazer da seguinte forma:
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ').lower()
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
