#crie um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci

termo = int(input("Digite quantos termos você quer mostrar: "))
cont = 1
ante = 0
suce = 1
soma = 0

while cont <= termo:
    print("{} -> ".format(ante), end = "")
    cont += 1
    soma = ante + suce
    ante = suce
    suce = soma

print("FIM")
