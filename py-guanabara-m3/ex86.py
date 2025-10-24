#crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
#No final mostre a matriz na tela, com a formatação correta
#[1] [2] [3]
#[4] [5] [6]
#[7] [8] [9]
from time import sleep
lista = []

print("=-"*30)
print(f"{"GERADOR DE MATRIZ 3X3":^60}")
print("=-"*30)

for i in range (1, 10):
    num = int(input(f"Digite o {i}º número: "))
    lista.append(num)

print("GERANDO MATRIZ 3X3...")
sleep(1)
for i in range (0, 9):
    if i < 3:
        print(f"[{lista[i]:^5}]", end = " ")
        if i == 2:
            print()
    elif i < 6:
        print(f"[{lista[i]:^5}]", end = " ")
        if i == 5:
            print()
    else: 
        print(f"[{lista[i]:^5}]", end = " ")
print("\n", end = "")
print("Matriz gerada com sucesso!".upper())
