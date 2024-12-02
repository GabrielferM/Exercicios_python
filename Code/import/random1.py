from random import randint

class Dado():
    
    def __init__(self,face):
        self.face = face
        
    def rolar(self):
        print('O dado rolado:',self.face)
        
num = randint(1,6)
meu_dado = Dado(num)
meu_dado.rolar()