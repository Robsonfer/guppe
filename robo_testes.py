"""
Módulo de testes para a aula 150 de Testes Unitários - Antes e após hooks
"""

import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):
    def teste_carregar(self):
        megaman = Robo(nome='Mega Man', bateria=50)
        megaman.carregar()
        self.assertEqual(megaman.bateria, 100)


if __name__ == '__main__':
    unittest.main()
