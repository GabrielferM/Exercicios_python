with open('Code\Leitura_de_dados\pi.txt') as arquivo_aberto:
    linhas = arquivo_aberto.readline()

pi_linha = ''
for linha in linhas:
    pi_linha += linha.lstrip()
    
print(pi_linha)
    
aniversario = input('Coloque o nome do seu aniversário tudo junto em DDMMAA:')
if aniversario in pi_linha:
    print('A data do seu aniversário está em Pi!!!!')
else:
    print('Infelizmente a data do seu aniversário ;-;')
