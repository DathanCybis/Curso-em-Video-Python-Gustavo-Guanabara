#crie um programa que leia um número inteiro e mostre a sua tabuada

num = int(input("Digite um número para descobrir sua tabuada: "))

print("{} x 1 = {}".format(num, (num)))
print("{} x 2 = {}".format(num, (num*2)))
print("{} x 3 = {}".format(num, (num*3)))
print("{} x 4 = {}".format(num, (num*4)))
print("{} x 5 = {}".format(num, (num*5)))
print("{} x 6 = {}".format(num, (num*6)))
print("{} x 7 = {}".format(num, (num*7)))
print("{} x 8 = {}".format(num, (num*8)))
print("{} x 9 = {}".format(num, (num*9)))
print("{} x 10 = {}".format(num, (num*10)))



num1 = int(input("Digite um número e descubra sua tabuada: "))

for num2 in range(1, 11):
    resultado = num1 * num2
    print("{} x {} = {}".format(num1, num2, resultado))