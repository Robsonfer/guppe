"""
Dunder Main e Dunder Name

Dunder = Double Under
Dunder Name = __name__
Dunder Main = __main__

Em Python são utilizados dunder para criar funções, atributos, propriedades e etc utilizando double under para não
gerar conflitos com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:
int main(){
    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main (string[] args){

}

Nesses dois exemplos acima estão trechos essenciais para o funcionamento das linguagens C e Java. Sem essas funções,
as linguagens citadas não iniciam e não executam, em Python não temos isso porque não precisa disso.

Se exeutarmos um módulo Python diretamente na linha de comando, internamente o Python atribuirá à variável __name__
o valor __main__ indicando que este módulo é o módulo de execução principal.

"""

# Ir até a aula083_modulo_de_teste.py e verificar que foi incluído um condicional com __name__ e __main__
# Isso fez com que importar o módulo aqui parasse de imprimir tudo o que tem lá
"""
from aula083_modulo_de_teste import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))
"""

# Segundo exemplo, primeiro.py e segundo.py:
import primeiro
import segundo
