#crie um programa que leia o primeiro termo e razão de uma pa, e mostre os 10 primeiros termos da progressão utilizando while.

prim = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
p = 0
while p < 10:
    p += 1
    f = prim + (p - 1) * razao
    print(f, end = " -> ")

print("FIM")