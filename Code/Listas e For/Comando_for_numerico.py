for valores in range(1,21):
    print(valores)
for valores in range(1,21,2):
    print(valores)
multiplo = []
for valores in range(3,31,3):
    multiplo.append(valores)
    print(multiplo)
for valores in range(1,11):
    cubo = valores**3
    print(cubo)
#lista comprimida, boa para diminuir os codigos
cubos = [valores**3 for valores in range(1,11)]
print(cubos)



#lista ate 1 milhao
#milhao = []
#for valor in range(1,10000001):
#    milhao.append(valor)
#print(min(milhao))
#print(max(milhao))
#print(sum(milhao))