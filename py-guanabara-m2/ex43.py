#crie um programa que leia o peso e altura de uma pessoa, calcule o imc e mostre o status de acordo com: 
#abaixo de 18.5 - abaixo do peso, Entre 18.5 e 25 - peso ideal, 25 até 30 - sobrepeso, 30 até 40 - obesidade, acima de 40 - obesidade mórbida

peso = float(input("Digite um peso: "))
altura = float(input("Digite uma altura: "))

imc = peso / (altura ** 2)
print("O IMC é {:.1f}".format(imc))
if imc < 18.5:
    print("O status é Abaixo do peso")
elif imc <= 25:
    print("O status é Peso ideal")
elif imc <= 30:
    print("O status é Sobrepeso")
elif imc <= 40:
    print("O status é Obesidade")
else:
    print("O status é Obesidade mórbida")
