#crie um programa que leia o ano de nascimento de um atleta de natação e mostre sua categoria, de acordo com: 
#até 9 - mirim, até 14 - infantil, até 19 - junior, até 25 - sênior, acima de 25 - master.
from datetime import date

ano = int(input("Digite o ano do nascimento: "))
atual = date.today().year

categ = atual - ano

if categ <= 9:
    print("Você tem {} anos e se encaixa na categoria - Mirim".format(categ))
elif categ <= 14:
    print("Você tem {} anos e se encaixa na categoria - Infantil".format(categ))
elif categ <= 19:
    print("Você tem {} anos e se encaixa na categoria - Junior".format(categ))
elif categ <= 25:
    print("Você tem {} anos e se encaixa na categoria - Sênior".format(categ))
else:
    print("Você tem {} anos e se encaixa na categoria - MASTER".format(categ))