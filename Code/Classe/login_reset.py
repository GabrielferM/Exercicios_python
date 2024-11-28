class Logins():
    
    def __init__(self):
        self.tentativa_de_login = 1
        
    def ingrementador_login(self):
        self.tentativa_de_login += 1
        print('Foi incrementado 1 no login, total:',self.tentativa_de_login)
        
    def reset_login(self):
        self.tentativa_de_login = 0
        print('O login foi resetado', self.tentativa_de_login)
        
        
meu_login = Logins()        
meu_login.ingrementador_login()
meu_login.ingrementador_login()
meu_login.reset_login()

        
        
        