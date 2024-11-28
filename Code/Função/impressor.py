def print_modelo( *lists):
    imprimidos = []
    for itens in lists:
        impressao = itens
        
        print('/nEsta imprimindo o seguinte item',impressao)
        imprimidos.append(impressao)
    return print(imprimidos)
    
    