#crie um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.

larg = float(input("Quantos metros de largura tem a parede?: "))
alt = float(input("Quantos metros de altura tem a parede?: "))

area = (alt * larg)
tinta = (area) / 2

print("A parede tem a área de {}m²".format(area))
print("Serão necessários {} litros de tinta para pintar toda parede".format(tinta))