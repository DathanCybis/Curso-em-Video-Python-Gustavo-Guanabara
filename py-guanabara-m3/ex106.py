#crie um mini-sistema que utilize o interactive help no python. O usuário vai digitar o comando e o manual vai aparecer. 
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará. obs: use cores
from time import sleep
c = ['\33[m',        # 0 - sem cor
     '\33[0;30;41m', # 1 - vermelho
     '\33[0;30;43m', # 2 - amarelo
     '\33[0;30;45m', # 3 - roxo
     '\33[0;30;46m'  # 4 - azul
     ]


def titulo(msg, cor=0):
    f = len(msg) + 4
    print(c[cor], end='')
    print("~" * f)
    print(f'  {msg}  ')
    print("~" * f)
    print(c[0], end='')
    sleep(0.5)


def helpy(txt):
    titulo(f'Acessando o manual do comando \'{txt}\'', 4)
    help(txt)
    sleep(1)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)

    foub = str(input("Digite uma Função ou Biblioteca > "))
    if 'fim' in foub.lower():
        break
    else:
        helpy(foub)

titulo("Programa Finalizado!", 2)
