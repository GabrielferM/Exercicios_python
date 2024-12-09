import json
nome_numero = 'numero1.json'

#DEMONTRAR O NUMERO FAVORITO
def falar_numero():
    
    num_fav_fala = retirada_numero()
    if num_fav_fala:
        print('Seu numero favorito e:', num_fav_fala) 
           
    else:
        num_fav_fala = criar_numero_fav()
        print('Agora seu numero foi registrado')
    
#PEGAR O NUMERO FAV DO USUARIO
def retirada_numero():
    try:
        with open(nome_numero) as num_aberto:
            num_fav = json.load(num_aberto)
    except FileNotFoundError:
        return None
    else:
        return num_fav
    
#CRIAR UM NOVO NUMERO FAVORITO
def criar_numero_fav():
    num_fav = int(input('Escreva um numero favorito'))
    with open(nome_numero, 'w') as numero_aberto:
        json.dump(num_fav,numero_aberto)
        return num_fav
    
    
opsao = input('Deseja um novo numero N\S')
    
if opsao.title() == 'S':
    criar_numero_fav()
    falar_numero()
else:
    falar_numero()
        