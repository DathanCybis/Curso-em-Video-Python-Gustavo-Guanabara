"""num = [1, 2, 3, 4, 5]

num.append(6)
num.remove(5)
num.sort(reverse=True)
num.insert(1, 5)
num.sort(reverse=False)

if 7 in num:
    num.remove(7)
else:
    print("O número 7 não está na lista")


print(num)"""


#valores = []

#valores.append(5)
#valores.append(3)
#valores.append(1)

#valores = list()

#for cont in range (0, 5):
#    valores.append(int(input("Digite um valor: ")))

#for c, v in enumerate(valores):
#    print(f"Na posição {c} encontrei o valor {v}!")
#print("Cheguei ao final da lista!")

#a = [1, 2, 3, 4]
#b = a[:]
#b[2] = 5

#print(a)
#print(b)

valores = []
for cont in range(1, 6):
    valores.append(int(input(f"Digite o {cont}º número: ")))

for c, v in enumerate(valores):
    print(f"{c+1}. {v}")
print("Fim")