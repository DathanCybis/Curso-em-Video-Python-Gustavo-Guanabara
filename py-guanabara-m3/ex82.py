#crie um programa que leia vários números e coloque-os em uma lista. Depois crie mais duas listas que vão conter apenas valores pares e ímpares. 
#Ao final mostre as três listas

lista = []
impar = []
par = []

while True:
    lista.append(int(input("Digite um número: ")))

    sn = str(input("Quer continuar? [S/N]: "))
    if sn in "Nn":
        break

print("\nFim do programa!")

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"Os valores digitados foram {lista}")
print(f"Os valores pares foram {par}")
print(f"Os valores ímpares foram {impar}\n")
