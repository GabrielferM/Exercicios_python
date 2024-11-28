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
        
meu_usuario = usuario('gabriel','marra','19')

meu_usuario.descricao()
meu_usuario.entrada()