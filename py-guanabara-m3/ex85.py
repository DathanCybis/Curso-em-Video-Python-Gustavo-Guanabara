#crie um programa onde o usuário possa digitar 7 números e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final mostre os valores pares e ímpares em ordem crescente
temp = []
impar = []
par = []
for i in range (0, 7):
    num = int(input("Digite um número: "))
    temp.append(num)

for i in temp:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
par.sort()
impar.sort()
temp.clear()
temp.append(par[:])
temp.append(impar[:])
print(temp)
print(f"Os valores pares digitados foram: {temp[0]}")
print(f"Os valores ímpares digitados foram: {temp[1]}")
