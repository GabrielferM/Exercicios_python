aprendizado = 'Code\Leitura_de_dados\Aprendizado_em_python.txt'

with open(aprendizado) as arquivo_aberto1:
    conteudo = arquivo_aberto1.read()
    print(conteudo)
    print('\n')
    
with open(aprendizado) as arquivo_aberto2:
    for linhas in arquivo_aberto2:
        print(linhas.rstrip())
    print('\n')
     
with open(aprendizado) as arquivo_aberto3:
    linhas = arquivo_aberto3.readlines()
    for linha in linhas:
        print(linha.rstrip())
        

    