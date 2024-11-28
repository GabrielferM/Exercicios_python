convidado = ['mikey jakson','edward','kirin','ortriel','slug']
print(convidado[2:])
print(convidado[:4])
print(convidado[-2:])

minhapizzas = ['Pepperoni','4 queijo', 'portuguesa','chocolate']
amigo_pizzas = minhapizzas[:]
amigo_pizzas.append('Calabresa')

print('minhas lista favorias sao')
for pizza in minhapizzas:
    print(pizza)
print('\namigo pizza favorias sao')
for pizza in amigo_pizzas:
    print('\n',pizza)

    
    


