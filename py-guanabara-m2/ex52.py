#crie um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input("Digite um número: "))
vezes = 0

for i in range(1, num+1):
    
    if num % i == 0:
        print("==== {} ====".format(i))
        vezes += 1

print("O número {} foi divisível {} vezes".format(num, vezes))
if vezes == 2:
    print("Por isso ele é PRIMO")
else:
    print("Por isso ele não é PRIMO!")




















#fiz as duas soluções sem o vídeo, graças a Deus!

"""num = int(input("Digite um número: "))

for i in range(1, num+1):
    
    if i % 2 == 0:
        print(i, end = " ")
    elif i % 3 == 0:
        print(i, end = " ")
    elif i % 5 == 0:
        print(i, end = " ")
    else:
        print("{} é primo".format(i), end = " ")"""