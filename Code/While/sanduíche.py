prompt = 'Qual sanduichi voce deseja pedir?: '
name = 'Qual e o seu nome?: '
pedidos_lanches = []
continuar = True

nome = input(name)
while continuar:
    pedidos_lanches.append(input(prompt)) 
    terminar = input('Deseja continuar? sim/nao: ')
    if terminar == 'nao':
        continuar = False
        
print('\n----------pedidos finalizado----------')
if 'queijo' in pedidos_lanches:
    print('infelizmente estamos sem sanduiche de queijo, removeremos da lista\n')
    while 'queijo' in pedidos_lanches:
        pedidos_lanches.remove('queijo')
    
print(nome.title(),'foi finalizado o seu pedido das pizzas de-')
print
for pedidos_finalizados in pedidos_lanches:
    print('Preparado sua pizza de ' + pedidos_finalizados)
