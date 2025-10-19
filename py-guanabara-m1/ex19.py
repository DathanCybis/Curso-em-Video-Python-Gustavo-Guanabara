#crie um programa que leia o nome de 4 alunos, sorteie e escreva o nome do escolhido.

'''import random

n1 = str(input("Digite o nome 1: "))
n2 = str(input("Digite o nome 2: "))
n3 = str(input("Digite o nome 3: "))
n4 = str(input("Digite o nome 4: "))

a = random.randint(1, 4)

if a == 1:
    print("O escolhido foi: ",n1)
elif a == 2:
    print("O escolhido foi: ",n2)
elif a == 3:
    print("O escolhido foi: ",n3)
elif a == 4:
    print("O escolhido foi: ",n4)'''

from random import choice

n1 = str(input("Digite o nome 1: "))
n2 = str(input("Digite o nome 2: "))
n3 = str(input("Digite o nome 3: "))
n4 = str(input("Digite o nome 4: "))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print(f"O escolhido foi {escolhido}")