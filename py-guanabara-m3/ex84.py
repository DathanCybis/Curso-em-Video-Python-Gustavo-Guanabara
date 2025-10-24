#crie um programa que leia o nome e peso de várias pessoas e guarde-os em uma lista, no final mostre: 
#a) quantas pessoas foram cadastradas b) Uma listagem das pessoas mais pesadas c) Uma listagem das pessoas mais leves
lista = []
dados = []
while True:
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()

    sn = str(input("Quer continuar? [S/N]: "))
    if sn in "Nn":
        break

print(lista)
maiorpeso = menorpeso = 0
pesado = leve = ""

for i, v in enumerate(lista):
    if i == 0:
        maior = menor = lista[i][1]
        pesado = leve = lista[i][0]
        
    else:
        if lista[i][1] > maior:
            maior = lista[i][1]
            pesado = lista[i][0]
            

        elif lista[i][1] < menor:
            menor = lista[i][1]
            leve = lista[i][0]
            

print(f"{len(lista)} pessoas foram cadastradas.")
print(f"O maior peso foi {maior}, peso de {pesado}")
print(f"O menor peso foi {menor}, peso de {leve}")
