"""
Aula 131 - Exercício 1

Crie a classe Veiculo, contendo marca e modelo.
Crie as propriedades getters e setters para os atributos e um método para imprimir os dados de um veículo.
Crie também o construtor da classe.
"""

class Veiculo:
    def __init__(self, marca, modelo) -> None:
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    
    def imprimir(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
