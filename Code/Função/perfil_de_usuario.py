# Os dois asteriscos no informacoes faz cria um dicionario dentro dele mesmo
 
def contrucao(primeiro,segundo,**informacoes):
    perfil = {}
    perfil['Primeiro nome'] = primeiro
    perfil['Segundo nome'] = segundo
    for chave,valor in informacoes.items():
        perfil[chave] = valor
    return perfil

#A variavel usuario vai receber o valor da funcao contrucao
usuario = contrucao('gabriel','marra', 
localizacao='franca',
linguagem='python')

print(usuario)
