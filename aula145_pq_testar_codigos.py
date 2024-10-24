"""
Aula 145 - Por que testar o nosso código?

Testes Automatizados!

APLICAÇÃO WEB
    > FRONTEND
    > BACKEND
    > TESTES AUTOMATIZADOS

Testes automatizados são como legumes:
    Todos sabem que é bom e importante para a saúde comer legumes, mas quase ninguém quer comer.

Por que testar o nosso código?
    - Reduzir bugs (problemas) existentes no código;
    - Testes garantem que novos recursos da sua aplicação não quebrem (alterem) recursos antigos;
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuem corrigidos;
    - Testes garantem que a refatoração não tragam novos bugs (problemas).

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com TDD são utilizados estágios de desenvolvimento:
    - Escrever o teste primeiro;
    - Escrever o código mínimo suficiente para fazer o teste passar, ou seja, executado com sucesso;
    - Refatorar o código para realizar a funcionalidade e testar novamente;
    - Uma vez que o teste passe, o recurso é considerado completo.

Estes estágios do Desenvolvimento do TDD são seguidos pelos desenvolvedores quase como um mantra:
    - Red: Quando o código é gerado com erro;
    - Green: Quando o teste passa;
    - Refactor: Reescrever o código para que ele funcione corretamente.

Basicamente no Red, você escreve o teste para falhar, você sabe que vai falhar. Como instanciar um objeto e
    chamar uma propriedade ou método de uma classe sem construir a classe antes.

No Green você vê o erro ocasionado no Red e faz basicamente faz o que o Traceback te informa que falta
"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Felix')

felix.miar()

print(felix.nome)
