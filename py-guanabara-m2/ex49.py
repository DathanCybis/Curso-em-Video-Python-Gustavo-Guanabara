#crie um programa que leia um número e mostre a tábuada do mesmo.

num = int(input("Digite um valor para receber sua tabuada: "))

for i in range(1, 11):
    print("{} x {} = {}".format(num, i, i * num))