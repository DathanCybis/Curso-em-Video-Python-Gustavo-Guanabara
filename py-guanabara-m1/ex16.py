'''
import math
#crie um programa que leia um número real e mostre na tela sua porção inteira ex: 6.127 - tem a parte inteira 6.

num = float(input("Digite um número: "))

print("O número {} tem a parte inteira {}".format(num, math.trunc(num)))
'''

num = float(input("Digite um número: "))

print("O número {} tem a parte inteira {}".format(num, int(num)))