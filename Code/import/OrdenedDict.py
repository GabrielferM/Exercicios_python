from collections import OrderedDict

Glossario = OrderedDict() 

Glossario['Laço'] = 'O Laço é o comando For, que faz um ciclo pre determinado'
Glossario['Variavel'] = 'A variavel pode ser tudo do nosso mundo, uma frase, um numero e um objeto'
Glossario['Lista'] = 'A lista e o agrupamento que determinamos de variveis'
Glossario['If'] = 'O camando if, ultiliza a logica booleana para verificar se e True ou False'
Glossario['Dicionairo'] = 'O dicionario e uma forma mais complexa para armazenar dados'

for comando,explicacao in Glossario.items():
    print(comando + ":" + explicacao + '\n')