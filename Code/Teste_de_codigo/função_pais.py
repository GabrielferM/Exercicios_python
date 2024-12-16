def pais_e_cidade(cidade='Franca', pais='Brasil',populasao='200000'):
    if populasao:
        full_string = (cidade + ',' + pais + ',' + populasao)
    else:
        full_string = (cidade + ',' + pais)
    return full_string.title()