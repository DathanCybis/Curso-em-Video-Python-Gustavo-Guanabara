#crie um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar 
#três contagens através da função criada: a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) uma contagem personalizada
from time import sleep
def lin():
    print("=-"*25)


def contador(i, f, p):
    lin()
    if p == 0 or p == -1:
        p = 1
    elif p < 0:
        p = -p
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if f == 0:
        f = -1
    if i > f:
        p = -p
        f = f - 1
    else:
        f = f + 1
    for i in range(i, f, p):
        print(f"{i}", end=" ", flush=True)
        sleep(0.4)
    print("FIM!")
    lin()

contador(1, 10, 1)
#contador(10, -1, -2)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
