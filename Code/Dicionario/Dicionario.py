pessoa ={
    'primeiro nome':'ray',
    'segundo nome':'corleone',
    'idade':'18',
    'cidade':'xiquexique bahia'
}
print(pessoa['primeiro nome'].title())
print(pessoa['segundo nome'].title())
print(pessoa['idade'].title())
print(pessoa['cidade'].title())


numerofav = {
    'Flor': 5,
    'Gabriel': 7,
    'tiago': 8,
    'Pedro': 7.2,
    'Thiaguinho': -8 
}
for nome,numero in numerofav.items():
    print(nome ,'seu nome favorito é', numero)
    

Glossario = {
    'Laço':'O Laço é o comando For, que faz um ciclo pre determinado',
    'Variavel':'A variavel pode ser tudo do nosso mundo, uma frase, um numero e um objeto',
    'Lista':'A lista e o agrupamento que determinamos de variveis',
    'If':'O camando if, ultiliza a logica booleana para verificar se e True e False',
    'Dicionairo':'O dicionario e uma forma mais complexa para armazenar dados'
}    

print('\n',
    Glossario['Dicionairo'],'\n',
    Glossario['If'],'\n',
    Glossario['Laço'],'\n',
    Glossario['Lista'],'\n',
    Glossario['Variavel'],'\n',
)

