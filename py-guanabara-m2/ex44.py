#crie um programa que calcule o valor a ser pago de um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque 10% de desconto, à vista cartão 5%, em até 2x cartão valor normal, 3x ou mais 20% de juros

valor = float(input("Digite o valor a ser pago: R$"))

print("[1] - À vista dinheiro/cheque\n[2] - À vista cartão\n[3] - Cartão em até 2x\n[4] - Cartão 3x ou mais")

cond = int(input("Qual a forma de pagamento?: "))

if cond == 1:
    desc = valor - (valor * 10) / 100
    print("Você recebeu um desconto e agora o valor passou a ser R${:.2f}".format(desc))

elif cond == 2:
    desc = valor - (valor * 5) / 100
    print("Você recebeu um desconto e agora o valor passou a ser R${:.2f}".format(desc))

elif cond == 3:
    parcela = valor / 2
    print("O valor do pagamento é R${:.2f}, em 2x fica R${:.2f}".format(valor, parcela))
    
elif cond == 4:
    juros = valor + (valor * 20) / 100
    vezes = int(input("Em quantas vezes gostaria de pagar?: "))
    parcela = juros / vezes
    print("O valor do pagamento passa a ser R${:.2f}, em {} vezes no cartão o parcelamento fica R${:.2f}".format(juros, vezes, parcela))

else:
    print("Digite um valor válido.")