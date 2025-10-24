#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep
jogo = {}
rank = {} #ou [] - não muda o resultado
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
print("-=" * 30)
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.7)
print("=-" * 30)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
cont = 1
for k, v in rank:
    print(f"{cont}º lugar: {k} com {v}.")
    cont+=1
    sleep(0.5)
print("-=" * 30)
