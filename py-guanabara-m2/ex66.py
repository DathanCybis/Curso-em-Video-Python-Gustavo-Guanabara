#crie um programa que leia vários números inteiros. O programa vai parar quando 999 for digitado, 
#e no final mostre quantos números foram digitados e qual foi a soma entre eles, desconsiderando o flag.

cont = soma = 0

while True:
    num = int(input("Digite um número inteiro [999 para parar]: "))
    if num == 999:
        break
    cont += 1
    soma += num

print(f"A soma dos {cont} números digitados foi {soma}")