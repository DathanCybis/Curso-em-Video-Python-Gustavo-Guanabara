#crie um programa que leia um ano e diga se ele é ou não bissexto.
from datetime import date

ano = int(input("Digite um ano para analisar ou 0 para analisar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print("{} É um ano bissexto.".format(ano))
else:
    print("{} NÃO é um ano bissexto.".format(ano))