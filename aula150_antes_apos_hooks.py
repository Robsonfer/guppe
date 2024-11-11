"""
Unittests - Aula 150 - Antes e após hooks


Hooks são os testes em si, ou seja, a execução dos testes.

Para realizar este tipo de funcionalidade o unittest tem dois métodos para isso:

setup() -> É executado antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados.

teardown() -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com bancos de dados.

=======================================================================================================
ATENÇÃO - PARA ESTA AULA, NÓS CONTINUAREMOS UTILIZANDO OS ARQUIVOS robo.py E robo_testes.py
=======================================================================================================

"""

# Exemplo hipotético, não real destes métodos:

import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        # configurações do setUp
        pass


    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDonw vai rodar após o teste
        pass


    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDonw vai rodar após o teste
        pass


    def tearDown(self):
        # configurações do tearDown
        pass
