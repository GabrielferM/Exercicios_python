def contrucao(primeiro,segundo,**informacoes):
    perfil = {}
    perfil['Primeiro nome'] = primeiro
    perfil['Segundo nome'] = segundo
    for chave,valor in informacoes.items():
        perfil[chave] = valor
    return perfil