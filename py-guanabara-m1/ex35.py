#crie um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo
"""""
a = float(input("Digite o 1º comprimento: "))
b = float(input("Digite o 2º comprimento: "))
c = float(input("Digite o 3º comprimento: "))

maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

if maior == a:
    soma = b + c
    dif = soma > a
elif maior == b:
    soma = a + c
    dif = soma > b
elif maior == c:
    soma = a + b
    dif = soma > c

if dif == True:
    print("PODE formar um triângulo")
else:
    print("NÃO PODE formar um triângulo")"""


a = float(input("Digite o 1º comprimento: "))
b = float(input("Digite o 2º comprimento: "))
c = float(input("Digite o 3º comprimento: "))

if a < b + c and b < a + c and c < a + b:
    print("PODE formar um triângulo")
else:
    print("NÃO PODE formar um triângulo")