#crie um programa que leia o nome de quatro alunos e mostre a ordem sorteada

from random import shuffle

n1 = str(input("Digite o nome 1: "))
n2 = str(input("Digite o nome 2: "))
n3 = str(input("Digite o nome 3: "))
n4 = str(input("Digite o nome 4: "))

lista = [n1, n2, n3, n4]

shuffle(lista)

print(f"A ordem sorteada foi: {lista}")