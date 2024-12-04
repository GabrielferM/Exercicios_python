
with open('Code\Leitura_de_dados\Textos\Banana.txt') as arquivo_aberto:
    arquivo_passado = arquivo_aberto.readlines()
    for linha in arquivo_passado:
        print(linha.replace("banana","maça"))
     