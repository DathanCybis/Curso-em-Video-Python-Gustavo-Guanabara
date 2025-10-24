#crie um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar 
#três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada
from time import sleep
def lin():
    print("=-"*25)


def contador():
    print()
    lin()
    print("Contagem de 1 até 10 de 1 em 1")
    for i in range(1, 11):
        print(f"{i}", end=" ", flush=True)
        sleep(0.4)
    print("FIM!")
    lin()
    print("Contagem de 10 até 0 de 2 em 2")
    for i in range(10, -1, -2):
        print(f"{i}", end = " ", flush=True)
        sleep(0.4)
    print("FIM!")
    lin()
    print("Agora é a sua vez de personalizar a contagem!")
    inicio = int(input("Início: "))
    fim = int(input("Fim: "))
    passo = int(input("Passo: "))
    lin()
    if passo == 0 or passo == -1:
        passo = 1
    elif passo < 0:
        passo = -passo
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if fim == 0:
        fim = -1
    if inicio > fim:
        passo = -passo
        fim = fim - 1
    else:
        fim = fim + 1
    for i in range(inicio, fim, passo):
        sleep(0.4)
        print(f"{i}", end = " ", flush=True)
    print("FIM!")
    print()

contador()
