#crie um programa que leia o peso de 5 pessoas e mostre qual foi o maior e o menor
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input("Digite o valor do {}º peso: ".format(i)))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print("O maior peso digitado foi: {:.1f}".format(maior))
print("O menor peso digitado foi: {:.1f}".format(menor))