#crie um programa que leia 6 números inteiros e mostre a soma daqueles que forem pares.

soma = 0
quantpar = 0
quantimpar = 0

for i in range(1,7):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        soma += num
        quantpar += 1
    else:
        quantimpar +=1

print("Você digitou {} números pares e {} ímpares, a soma dos pares é {}".format(quantpar, quantimpar, soma))