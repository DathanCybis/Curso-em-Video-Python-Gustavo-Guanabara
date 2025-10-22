#crie um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
#o primeiro é maior, ou o segundo, ou são iguais

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

if num1 > num2:
    print("O 1º número é maior")
elif num2 > num1:
    print("O 2º número é maior")
else:
    print("Os números são iguais")