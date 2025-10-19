#crie um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, 
#calcule e mostre o comprimento da hipotenusa

'''ca_oposto = float(input("Digite o comprimento do cateto oposto: "))
ca_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

a = (ca_oposto ** 2)
b = (ca_adjacente ** 2)

soma = a + b

hipotenusa = soma**(1/2)

print("O comprimento do cateto oposto é {} do adjacente é {} e da hipotenusa é: {:.2f}".format(ca_oposto, ca_adjacente, hipotenusa))'''

from math import hypot

ca_oposto = float(input("Digite o comprimento do cateto oposto: "))
ca_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(ca_oposto, ca_adjacente)

print("O comprimento do cateto oposto é {} do adjacente é {} e da hipotenusa é: {:.2f}".format(ca_oposto, ca_adjacente, hipotenusa))