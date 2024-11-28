carros = ['Subaru','Bmw','Mercedes','Jaguar']
for carro in carros:
    if carro.lower() == 'mercedes':
        print(carro)
        print('Esse e a', carro,'\n')
    else:
        print(carro)
        print('Esse nao e a Mercedes\n')

#Verificacao se o numero digitado e menor ou maior que 5
print('teste de numeros')
num = int(input('Digite um numero:'))
if num <= 5:
    print('Esse numero e menor que 5')
else:
    print('Esse numero e maior que 5')

#Verificacao se o numero e igual 5    
print('Esse numero e igual a 5?\n')
if num == 5:
    print('sim, esse numero e igual a 5')
else:
    print('nao, esse numero nao e igual a 5')

#vericacao se esse numero e diferente de 5
print('Esse numero e diferente de 5?\n')
if num != 5:
    print('sim, esse numero e diferente a 5')
else:
    print('nao, esse numero e igual a 5')

#teste and e teste or
num1 = int(input('Digite um numero pro num1:'))
num2 = int(input('Digite um numero pro num2:'))
if num1 == num2:
    print('Os dois numeros sao iguais')
else:
    if num1 > num2:
        print('O num1 e maior que o num2')
    else:
        print('O num2 e maior que o num1')
