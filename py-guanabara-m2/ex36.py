#crie um programa para aprovar um empréstimo bancário, receba o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#o valor da prestação mensal não pode exceder 30% do salário ou então será negado.

casa = float(input("Digite o valor da casa: "))
sal = float(input("Digite o seu salário: "))
anos = int(input("Digite em quantos anos vai pagar: "))

prest = casa / (anos*12)
porcent = (sal * 30) / 100

print("Para quitar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}".format(casa, anos, prest))

if prest <= porcent:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO!")

