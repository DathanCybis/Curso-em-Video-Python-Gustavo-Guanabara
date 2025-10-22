#crie um programa que leia um número e calcule o seu fatorial

'''num = int(input("Digite um número: "))
fatorial = num
c = 1
while fatorial > 0:
    print("{}".format(fatorial), end = "")
    print(" x " if fatorial > 1 else " = ", end = "")
    c *= fatorial
    fatorial -= 1
    
print(c)'''



'''n = int(input("Digite um número: "))
c = 1

for n in range(1, n+1):
    c *= n

print("O fatorial de {} é {}".format(n, c))'''



n = int(input("Digite um número inteiro: "))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1

print("O fatorial de {} é {}".format(n, f))
