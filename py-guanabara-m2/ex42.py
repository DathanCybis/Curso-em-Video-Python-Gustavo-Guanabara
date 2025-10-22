#crie um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo, acrescentando o recurso de 
#mostrar que tipo será formado, equilátero: todos os lados iguais, isósceles: dois lados iguais, escaleno: todos os lados diferentes.

r1 = int(input("Digite a 1º reta: "))
r2 = int(input("Digite a 2º reta: "))
r3 = int(input("Digite a 3º reta: "))

eq = r1 == r2 == r3
iso = r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2
#esc = r1 != r2 and r1 != r3

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    if eq == True:
        print("Um triângulo EQUILÁTERO PODE ser formado.")
    elif iso == True:
        print("Um triângulo ISÓSCELES PODE ser formado")
    else:
        print("Um triângulo ESCALENO PODE ser formado")
else:
    print("Um triângulo NÃO PODE ser formado")