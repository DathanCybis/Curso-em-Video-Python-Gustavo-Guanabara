#crie um programa que leia 5 valores númericos e guarde em uma lista, 
#e no final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

lista = []
menor = maior = cont = 0

for c in range(1, 6):
    lista.append(int(input(f"Digite o {c}º número: ")))
    
print(f"Você digitou os valores: {lista}")

#menor = min(lista)
#print(f"O menor valor digitado foi {min(lista)} nas posições {lista.index(menor)}")
#maior = max(lista)
#print(f"O maior valor digitado foi {max(lista)} nas posições {lista.index(maior)}")

for c in lista:
    cont+=1
    if cont == 1:
        maior = menor = c
    else:
        if c > maior:
            maior = c
        elif c < menor:
            menor = c

print(f"O menor valor digitado foi {menor} nas posições ", end="")

for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}", end = " ")

print(f"\nO maior valor digitado foi {maior} nas posições ", end="")

for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}", end=" ")
