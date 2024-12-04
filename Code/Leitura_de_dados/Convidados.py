listagem = 'Code\Leitura_de_dados\Textos\guest_book.txt'
flag = True
lista_nomes = []

with open(listagem, 'w') as listagem_aberta:
    # Poderia ter feito uma simples concatenação 
    while flag == True:
        nome = input('Escreva um nome para a lista:')
        lista_nomes.append(nome)
        op = input('Deseja continuar?:')
        if op == 'não':
            flag = False
    for n in lista_nomes:     
        n += '\n'
        listagem_aberta.write(n)
        