import os
pedidos = []
vdd = True
nome = input('Escreva o seu nome')

while vdd:
    
    os.system('cls')
    
    if len(pedidos) > 0:
        for p in pedidos:
            print(p['nome'],'-',p['pedido'])
    print('____________________________')
    
    pedido = (input('Escreva o seu pedido:'))    
    if pedido == 'sair':
        vdd = False
    
    pedidos.append({
        'nome': nome,
        'pedido': pedido
    })
    