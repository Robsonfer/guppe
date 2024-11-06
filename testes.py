"""
Módulo para a aula 148 de Testes Unitários
"""

import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer(comida='quiabo', eh_saudavel=True),
            'Estou comendo quiabo porque quero manter a forma!'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida não saudável"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez!'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com menos de 8 horas de sono"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir apenas 4 horas :('
        )

    def test_dormir_muito(self):
        """Testando o retorno com mais de 8 horas de sono"""
        self.assertEqual(
            dormir(10),
            'Putz! Dormi demais. Estou atrasado para o trabalho!'
        )

    # A partir daqui, faz parte da aula 149:

    def test_eh_engracada(self):
        """Testando o retorno com pessoas engraçadas"""
        # self.assertEqual(eh_engracada('Sergio Malandro'), False)
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado!')


if __name__ == '__main__':
    unittest.main()
