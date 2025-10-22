#crie um programa que leia o primeiro termo e a razão de uma PA, e mostre os 10 primeiros termos dessa progressão

termo = int(input("Digite o primeiro termo: "))
razão = int(input("Digite a razão: "))


for i in range(1, 11):
    pa = termo + (i - 1) * razão
    print(pa, end = " -> ")
    
print("FIM")

