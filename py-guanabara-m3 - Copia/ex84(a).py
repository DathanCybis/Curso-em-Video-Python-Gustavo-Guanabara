#crie um programa que leia o nome e peso de várias pessoas e guarde-os em uma lista, no final mostre: 
#a) quantas pessoas foram cadastradas b) Uma listagem das pessoas mais pesadas c) Uma listagem das pessoas mais leves

lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")).capitalize().strip())
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados [1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()

    sn = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if sn == "N":
        break


print(f"Ao todo {len(lista)} pessoas foram cadastradas!")
print(f"O maior peso é {maior} e a listagem das pessoas mais pesadas: ", end = "")
for p in lista:
    if p[1] == maior:
        print(f"[{p[0]}]", end= " ")

print(f"\nO menor peso é {menor} e a listagem das pessoas mais leves: ",end = " ")
for p in lista:
    if p[1] == menor:
        print(f"[{p[0]}]", end=" ")
