import unittest
from função_pais import pais_e_cidade

class Test_cidade(unittest.TestCase):
    
    #def test_cidade_pais(self):
     #   nome_formatado = pais_e_cidade('Franca','Brasil')
     #   self.assertEqual(nome_formatado,'Franca,Brasil')
        
    def test_cidade_pais_populasao(self):
        nome_formatado = pais_e_cidade('Franca','Brasil','200000')
        self.assertEqual(nome_formatado,'Franca,Brasil,200000')
        
unittest.main()