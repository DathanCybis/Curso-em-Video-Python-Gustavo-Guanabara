#crie um programa que leia um número e mostre o dobro, triplo e a raiz quadrada do mesmo.

num = float(input("Digite um número: "))

print("O dobro de {:.0f} é {:.0f}".format(num, (num*2)))
print("O triplo de {:.0f} é {:.0f}".format(num, (num*3)))
print("A raiz quadrada de {:.0f} é {:.2f}".format(num, (num**(1/2))))