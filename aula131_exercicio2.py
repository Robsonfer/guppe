"""
Aula 131 - Exercício 2

Crie a classe Carro que herda a classe Veiculo e possui o atributo portas.
Crie as propriedades getters e setters para o atributo.
Crie também o construtor da classe.
Sobrescreva o método de imprimir os dados do veículo de forma a apresentar também a quantidade de portas do carro.
"""

from aula131_exercicio1 import Veiculo


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self.__portas: int = portas
    
    @property
    def portas(self) -> int:
        return self.__portas
    
    @portas.setter
    def portas(self, portas):
        self.__portas = portas
    
    def imprimir(self) -> None:
        super().imprimir()
        print(f'Portas: {self.portas}')
