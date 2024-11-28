prompt = '\nQual ingrediente voce deseja colocar na pizza'
prompt += '\nCaso queria sair digite "sair":'

#Comando While com a logica booleana
definido = True
mensagem = ' '
while definido:
    
    mensagem = input(prompt)
    if mensagem == 'sair':
        definido = False
        print('encerrar programa')
    else:
        print(mensagem)