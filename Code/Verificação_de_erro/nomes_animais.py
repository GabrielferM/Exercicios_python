gato = 'Code\Verificação_de_erro\Gatos.txt'
cachorro = 'Cachorrii.txt'

try:
    with open(gato) as gato_nome:
        palavras = gato_nome.read()
        print(palavras)
    
    with open(cachorro) as cachorro_nome:
        print(cachorro_nome)
except FileNotFoundError:
    print('Arquivo Cachorro nao encontrado')