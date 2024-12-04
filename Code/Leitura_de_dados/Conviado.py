registro = 'Code\Leitura_de_dados\Textos\guest.txt'

with open(registro, 'w') as registro_aberto:
    nome = input('Escreva o seu nome:')
    registro_aberto.write(nome)
    