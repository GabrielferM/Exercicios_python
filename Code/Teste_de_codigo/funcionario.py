import unittest


class Funcionario():
    
    def __init__(self,primeiro_nome,segundo_nome,salario_anual):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.salario_anual = salario_anual
        
    def novo_salario(self,aumento=5000):
        self.salario_anual += aumento
        
        
        
class Testefuncionario(unittest.TestCase):
    
    def setUp(self):
       self.colaborador = Funcionario('gabriel','ferreira',50000)
    
    def test_aumento_default(self):
        self.colaborador.novo_salario()
        self.assertEqual(self.colaborador.salario_anual,55000) 
        
    def test_aumento_definido(self):
        self.colaborador.novo_salario(7000)
        self.assertEqual(self.colaborador.salario_anual,57000)

unittest.main()
