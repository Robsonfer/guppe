"""
Sistema de Arquivos - Manipulação

Documentação: https://docs.python.org/3/libray/os.html?highlight=os#module-os

import os



# Descobrindo se um arquivo ou diretório existe:

# Arquivos
print(os.path.exists('arquivo.txt'))              # Retorno: False
print(os.path.exists('frutas.txt'))               # Retonro: True

# Diretórios:

# Paths relativos:
print(os.path.exists('geek'))                     # Retorno: True
print(os.path.exists('geek/university'))          # Retorno: True
print(os.path.exists('outro'))                    # Retorno: True
print(os.path.exists('geek/university/geek3.py')) # Retorno: True

# Paths absolutos:
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university')) # Retorno: True
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/university'))      # Retorno: False
print(os.path.exists('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university/geek4.py')) # Retorno: True




# Criando arquivos:

# Forma 1:
open('arquivo_teste.txt', 'w').close()

# Forma 2:
open('arquivo_teste2.txt', 'w').close()

# Forma 3:
with open('arquivo_teste3.txt', 'w') as arquivo:
    pass
# Esse pass serve somente para que seja obedecida a indentação, pois ':' abre um bloco de código.
Com o with o arquivo fecha ao final do bloco.




# Melhor forma de criar arquivos, mas que não funciona no Windows:
os.mknod('arquivo-teste4.txt')
os.mknod('C:/Users/robsonfer/OneDrive - Armco do Brasil S.A/Perfil/Desktop/ROBSON/UDEMY/guppe/geek/university.txt')

OBSERVAÇÃO IMPORTANTE: Este comando mknod() NÃO FUNCIONA NO WINDOWS!
Para Windows use sempre uma das formas entre 1 e 3 mencionados acima

OBS: Criando um arquivo via mknod(), se o arquivo já existir, teremos o erro FileExistisError.
Mas sabemos como tratar erros.




# Criando diretórios Únicos:

# Path Relativo
try:
    os.mkdir('templates')
except FileExistsError:
    print('ATENÇÃO, ESTE DIRETÓRIO JÁ EXISTE, TENTE OUTRO NOME OU CAMINHO!')
# Esse diretório será criado onde o Python está a ser executado. E caso já exista, teremos um FileExistsError.
# Mas já tratamos com try/except o exemplo acima.

# Path Absoluto:
try:
    os.mkdir('C:/Users/robso/PycharmProjects/guppe/geek/templates')
except FileExistsError:
    print('ATENÇÃO, ESTE DIRETÓRIO JÁ EXISTE, TENTE OUTRO NOME OU CAMINHO!')

# OBS: Se não tivermos permissão para criar o diretório, teremos um PermissionError




# Criando diretórios múltiplos (árvore de diretórios):
os.makedirs('templates/geek/university')

# OBS: Caso todo o diretório criado já exista, teremos um FileExistisError
# Caso você queira criar mais uma pasta nesete diretório, basta acrescentar a pasta no final e não dará erro.




# Tratando erros na criação de diretórios de maneira direta:

# Basta colocar um parâmetro a mais conforme abaixo e mesmo que já exista o diretório, não apresentará erro:
os.makedirs('templates2/novo2/outro2', exist_ok=True)




# Renomeando arquivos e diretórios:

# Diretórios:
os.rename('templates2', 'geek2')

# Renomeando vários arquivos e diretórios ao mesmo tempo:
os.rename('geek2/novo2', 'geek2/novo')

# OBS: Se o diretório não existe, haverá um FileNotFoundError
# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Arquivos:
os.rename('geek2/novo/outro2/arquivo_teste2.txt', 'geek2/novo/outro2/arquivo_teste3.txt')
# É importante colocar o Path completo.




# Deletando arquivos:

os.remove('geek2/novo/outro2/arquivo_teste4.txt')

OBSERVAÇÕES IMPORTANTES:

1 - Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
2 - Se o arquivo não exista, teremos o FileNotFoundError.
3 - Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError.
    os.remove() é somente para arquivos e não diretórios.

ATENÇÃO: TOMEM CUIDADO COM OS COMANDOS DE DELEÇÃO. AO DELETAR UM ARQUIVO OU DIRETÓRIO.
OS ARQUIVOS DELETADOS VIA OS NÃO VÃO PARA A LIXEIRA, ELES SOMEM.




# Deletando diretórios vazios:

# os.rmdir('templates/geek/university') # remove o diretório university
# os.rmdir('templates/geek') # remove o diretório geek
# os.rmdir('geek2/novo/outro2') # remove o diretório outro2
# os.rmdir('geek2/novo') # remove o diretório novo

# Se o diretório tiver qualquer conteúdo, teremos um OSError.
# Se o diretório não existir, teremos um FileNotFoundError




# Removendo uma árvore de diretórios vazios:
# os.removedirs('geek2/outro/outro2')
# os.removedirs('geek2/outro2/outro3')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.




# Removendo uma árvore de arquivos:
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)


        

# Podemos usar uma biblioteca de terceiros, desta forma os arquivos deletados podem ser enviados para a lixeira!

from send2trash import send2trash

# Deletando arquivos para a lixeira com send2trash

send2trash('teste.txt') # Desta forma tudo o que for deletado vai direto para a lixeira.
# OBS: Se o arquivo não existir, teremos OSError.

# Deletando diretórios para a lixeira com send2trash
send2trash('templates')




# Trabalhando com arquivos e diretórios temporários (tempfile):

# Criando um dirertório temporário:
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

Traduzindo:
    1 - Com o with tempfile.TerporaryDirectory() as tmp nós criamos um diretório para arquivoso temporários que só vai existir
        enquanto o bloco do with existir.
    2 - Com o with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo, criamos um arquivo dentro deste diretório
        temporário e logo em seguida escrevemos uma frase dentro dele.
    3 - O input() foi criado somente para que possamos enxergar o arquivo temporário antes que ele desapareça, pois assim que
        sairmos do bloco do with o diretório temporário é excluído.



# Criando um arquivo temporário:
with tempfile.TemporaryFile() as tmp:
   tmp.write(b'Geek University\n')
   tmp.seek(0)
   print(tmp.read())

Traduzindo:
    1 - Com o with tempfile.TeporaryFile() as tmp nós criamos um arquivo temporário. Funciona igual ao exemplo acima;
    2 - Em tmp.write(b'Geek University\n'), repare que usamos um b antes da string. Isto acontece porque para arquivos, o Python
        não aceita escrever em string, somente em binário (b de bites);
    3 - Em tmp.seek(0) nós posicionamos o cursor no início do arquivo para viabilizar a leitura;
    4 - Por fim, imprimimos o arquivo temporário.



    
# Não somos obrigados a usar with:
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Podemos fazer de outra forma também:
arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)
print(arquivo.read())
input()

arquivo.close()
"""
