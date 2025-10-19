#crie um programa que leia 3 números e mostre qual é o maior e qual é o menor

num1 = int(input("Digite o Primeiro Número: "))
num2 = int(input("Digite o Segundo Número: "))
num3 = int(input("Digite o Terceiro Número: "))

if num1 > num2 and num1 > num3:
    print("{} É maior".format(num1))
elif num2 > num1 and num2 > num3:
    print("{} É maior".format(num2))
else:
    print("{} É maior".format(num3))

if num1 < num2 and num1 < num3:
    print("{} É menor".format(num1))
elif num2 < num1 and num2 < num3:
    print("{} É menor".format(num2))
else:
    print("{} É menor".format(num3))