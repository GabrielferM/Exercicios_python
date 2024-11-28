prompt = '\nQual idade voce possui'
prompt += '\nCaso queria sair so digitar "sair":'
definido = True

#comando While com Break

while definido:
    idade = input(prompt)
    if idade == 'sair':
        break
    if int(idade) <= 3:
        print('Sua entrada sera gratuita')
    elif int(idade) <= 12:
        print('Tera que pagar 15 reais')
    elif int(idade) > 12:
        print('Tera que pagar 25 reais')

