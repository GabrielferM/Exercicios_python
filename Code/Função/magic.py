def mostrar_magicos(list):
    for nome in list:
        print(nome) 

def grande(lists):
    #o Len vai ver o tamanho da lista, se ele tem 1 produto, 2 protudos etc
    #Range vai de 1 em 1 andando dentro da lista
    
    for i in range(len(lists)):
        lists[i] = lists[i] + ' o grande'
        print(lists[i])

magicos = ['mao negra','mortinho','dividido ao meio']
mostrar_magicos(magicos)
#Os dois pontos na varivel magicos faz uma copia que nao permite a funcao Grande fazer alterasao na nossa lista

grande(magicos[:])
print (magicos)