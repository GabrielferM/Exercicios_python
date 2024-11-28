class Restaurante():
    
    def __init__(self,nome_restaurante,tipo_comida,sabor):
        self.nome_restaurante = nome_restaurante
        self.tipo_comida = tipo_comida
        self.sabor = sabor
        
        
    def descricao(self):
        print(self.nome_restaurante.title(),'vende', self.tipo_comida.title())

class Sorveteria_ice(Restaurante):
    
    def __init__(self,nome_restaurante,tipo_comida,sabor):
        super().__init__(nome_restaurante,tipo_comida,sabor)
        self.sabores = []
        self.sabores.append = (self.sabor)
        
    def mostrar_lista(self):
        print(self.sabores) 


sorveteria = Sorveteria_ice('fome','mechido','Baunilha','')
#sorveteria = Sorveteria_ice('Blue berry')
#sorveteria = Sorveteria_ice('Amoras')
sorveteria.mostrar_lista()