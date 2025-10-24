#crie um programa que vai ler vários números e colocá-los em uma lista. Depois mostre: 
#a) Quantos números foram digitados b) A lista de valores ordenada de forma decrescente c) se o valor 5 foi digitado ou não.
lista = []
qnt = 0
while True:
    lista.append(int(input("Digite um número: ")))
    qnt += 1
    sn = str(input("Quer continuar? [S/N]: ")).strip()
    if sn in "Nn":
        break

print("\nFim do programa, volte sempre!\n")

print(f"Foram digitados {qnt} números") #ou com len(lista)
print(f"Os números foram: {lista}")

if 5 in lista:
    print(f"O número 5 foi digitado na lista na posição {lista.index(5)}")
else:
    print("O número 5 não foi digitado na lista")

lista.sort(reverse=True)
print(f"A lista ordenada de forma decrescente é: {lista}")
