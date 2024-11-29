#classe Pai
class usuario():
    
    def __init__(self, primeiro_nome,ultimo_nome,idade):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        
    def descricao(self):
        nome_inteiro = ('Me chamo ' + self.primeiro_nome.title() + ' ' + self.ultimo_nome.title() + ' tenho ' + self.idade + ' de idade')
        return print(nome_inteiro)
    
    def entrada(self):
        saudacao = ('Ola ' + self.primeiro_nome.title() + ' e um prazer te receber no APP')
        print(saudacao)

#classe filho        
class Adm(usuario):
    
    def __init__(self, primeiro_nome, ultimo_nome, idade):
        super().__init__(primeiro_nome, ultimo_nome, idade)
        #Atribui uma intancia para a Classe privilegios, podendo utilizar o metodos de Privilegios sem necessariamente chamar a classe
        self.privilegios = Privilegios()

#Sub-classe da classe filho
class Privilegios(Adm):
    
    def __init__(self, privilegios = ['Pode add um post','Pode banir','Pode deletar um post'] ):
        self.privilegios = privilegios
    
    def Mostrar_privilegios(self):
        print('\n')
        for p in self.privilegios:
            print(p)
        
        
meu_usuario = usuario('gabriel','marra','19')
meu_usuario.descricao()
meu_usuario.entrada()


Meu_adm = Adm('gabriel','marra','19')
Meu_adm.privilegios.Mostrar_privilegios()