#também deverá mostrar o tempo que falta ou que passou do prazo.
#crie um programa que leia o ano de nascimento de um jovem e informe: se ele ainda vai se alistar, se já é hora ou se já passou. 
from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
sexo = str(input("Digite o seu sexo [m/f]: "))

atual = date.today().year
quant = atual - ano

if sexo == "m":
    if quant < 18:
        falta = 18 - quant
        print("Você ainda vai se alistar, faltam {} anos".format(falta))
    elif quant == 18:
        print("Já é hora de se alistar")
    else:
        passou = quant - 18
        print("Já passou do seu tempo de se alistar, passou {} ano(s)".format(passou))
else:
    print("Não é necessário que você se aliste")
    print("Você tem {} anos".format(quant))