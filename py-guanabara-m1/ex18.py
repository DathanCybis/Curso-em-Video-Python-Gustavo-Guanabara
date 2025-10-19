#crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = int(input("Digite o ângulo: "))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print("O ângulo {} tem o:\nSeno de {:.2f}\nCosseno de {:.2f}\nTangente de {:.2f}".format(ang, seno,cos,tang))