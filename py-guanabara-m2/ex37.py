#crie um programa que leia um número inteiro e peça ao usuário escolher qual será a base de conversão: 
# 1 para binário. 2 para octal. 3 para hexadecimal

num = int(input("Digite um número: "))
base = int(input("Escolha qual a base de conversão - 1(binário), 2(octal) ou 3(hexadecimal): "))
#if base < 1 or base > 3:
#    print("Não foi possível reconhecer seu comando, digite um valor de 1 a 3")

if base == 1:
    print("O número {} convertido para binário é {:b}".format(num, num))
elif base == 2:
    print("O número {} convertido para octal é {:o}".format(num, num))
elif base == 3:
    print("O número {} convertido para hexadecimal é {:x}".format(num, num))
else:
    print("Não foi possível reconhecer seu comando, digite um valor de 1 a 3.")