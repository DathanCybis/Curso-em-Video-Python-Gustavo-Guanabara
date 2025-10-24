#crie um programa que leia 4 valores e guarde em uma tupla e mostre: 
#a) quantas vezes apareceu o valor 9 b) em que posição foi digitado o primeiro valor 3 c) quais foram os números pares

#n1 = int(input("Digite um número: "))
#n2 = int(input("Digite um número: "))
#n3 = int(input("Digite um número: "))
#n4 = int(input("Digite um número: "))

#lista = (n1, n2, n3, n4)

lista = tuple(int(input("Digite um número: ")) for i in range(4))

print(f"O número 9 apareceu {lista.count(9) } vezes")
if 3 in lista:
    print(f"O número 3 foi digitado na posição {lista.index(3)+1}")
else:
    print("O número 3 não foi digitado")
par = 1
for i in lista:
    if i % 2 == 0:
        par = i
if par % 2 == 0:
    print("Os valores pares foram: ", end = "")
else:
    print("Nenhum número par foi digitado")

for c in lista:
    if c % 2 == 0:
        print(c, end = " ")
