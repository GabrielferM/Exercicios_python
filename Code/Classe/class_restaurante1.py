class Restaurante():
    
    def __init__(self,nome_restaurante,tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
    def descricao(self):
        print(self.nome_restaurante.title(),'vende', self.tipo_cozinha.title())

meu_restaurante = Restaurante('fome','mechido')
seu_restaurante = Restaurante('bebedeira','suco')

meu_restaurante.descricao()
seu_restaurante.descricao()