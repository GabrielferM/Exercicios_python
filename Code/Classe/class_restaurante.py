class Restaurante():
    
    def __init__(self,nome_restaurante,tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.numero_servido = 5
        
    def descricao_restaurante(self):
        print(self.nome_restaurante.title() +' serve '+ self.tipo_cozinha.title())  
              
    def restaurante_aberto(self):
        print(self.nome_restaurante.title() + ' esta aberto')   
    
    def restaurante(self,pedidos):
        self.numero_servido = pedidos 
        print(self.numero_servido)
    
    def novo_restaurantes(self,acrecimo):
        self.numero_servido += int(acrecimo)
        print(self.numero_servido)
        
restaurante = Restaurante('bloblor','pastel')
restaurante.restaurante_aberto()
restaurante.descricao_restaurante()
print(restaurante.nome_restaurante.title(),'e muito bom')
print(restaurante.nome_restaurante.title(),'vende',restaurante.tipo_cozinha.title())
restaurante.restaurante(16)
numero = input('escreva um numero pra encrementar')
restaurante.novo_restaurantes(numero)