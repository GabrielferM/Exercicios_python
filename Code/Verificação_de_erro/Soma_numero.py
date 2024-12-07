Flag = True

while Flag == True:
    num1 = input('Escreva um numero:')
    num2 = input('Escreva um numero:')
    if num1 == 'q' or num2 == 'q':
        Flag = False
        
    try:
        soma = (num1 + num2 + 3)
        print(soma)
    except TypeError:
        if num1 == 'q' or num2 == 'q':
            pass
        else:
            print('O numero nao foram convertido')