def fazer_album(art,al,fx):
    albums = {
        'artista':art, 'album':al
    }
    if fx:
        albums['faixa'] = fx
    return albums


while True:
    artista = input('Escreva o nome de um artista:')
    album = input('Escreva o nome de algum album dele:')
    faixas  = input('Escreva o numero de faixas:')

    #Para encerrar o programa
    if artista == 'q':
        break
    if album == 'q':
        break
    if faixas == 'q':
        break
    
    descricao = fazer_album(artista,album,faixas)
    print(descricao) 