#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados, 
# ex: 1834 - unidade: 4, dezena: 3, centena: 8, milhar: 1.

#num = str(input("Digite um número de 0 a 9999: "))
#print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}".format(num[3], num[2], num[1], num[0]))


#crie um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados, 
# ex: 1834 - unidade: 4, dezena: 3, centena: 8, milhar: 1.

num = int(input("Digite um número de 0 a 9999: "))

if num < 10000 and num >= 0:

    uni = num // 1 % 10
    dez = num // 10 % 10
    cen = num // 100 % 10
    mil = num // 1000 % 10

    print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(mil, cen, dez, uni))

else:

    print("Digite um número positivo até 9999")
    