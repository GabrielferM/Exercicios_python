convidado = ['mikey jakson','edward','kirin']
print('Eu convido para minha festa:',convidado[0])
print('Eu convido para minha festa:',convidado[1])
print('Eu convido para minha festa:',convidado[2])
print('Mas o ',convidado[0],'não podera ir')
convidado[0] = 'Bolsonario'
print('então vou convidar o',convidado[0])
#chegou mais gente
convidado.insert(0,'minions do mal')
convidado.insert(2,'the rock')
convidado.append('Jesus')
print(convidado)
print('infelimente eles nn virão')
nome_da_pessoa = convidado.pop()
print(nome_da_pessoa,'infelizmente não vira')
nome_da_pessoa = convidado.pop()
print(nome_da_pessoa,'infelizmente não vira')
nome_da_pessoa = convidado.pop()
print(nome_da_pessoa,'infelizmente não vira')
nome_da_pessoa = convidado.pop()
print(nome_da_pessoa,'infelizmente não vira')
print('só sobrou o',convidado)
del convidado[0]
del convidado[0]
print(convidado)
print('Estou convidado',len(convidado))