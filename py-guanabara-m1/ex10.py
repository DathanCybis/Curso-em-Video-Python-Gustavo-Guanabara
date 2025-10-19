#crie um programa que leia quantos reais uma pessoa tem e quantos dólares ela pode comprar. considere dólar = R$3,27 ou não :D

reais = float(input("Digite quantos reais você tem e descubra quantos dólares teria: R$"))

dol = float((reais / 5.45))

print("Com {:.2f} reais, você teria {:.2f} dólares".format(reais, dol))