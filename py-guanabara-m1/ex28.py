#crie um programa que faça o computador "pensar" em um número inteiro de 1 a 5 
#e peça pro usuário descobrir qual o número e digitar se acertou ou errou.

from random import randint

num = randint(1, 5)

print("-=-" * 18)
print('Vou "pensar" em um número de 1 a 5, tente adivinhar...')
print("-=-" * 18)

num2 = int(input("Qual número estou pensando?: "))

if num == num2:
    print('Parabéns! Você acertou!!')
else:
    print("Infelizmente você não acertou o número, tente novamente!\nEu estava pensando no número {}".format(num))