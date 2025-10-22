cont = soma = 0
while True:
    num = int(input("Digite um número inteiro: [999 para parar] "))
    if num == 999:
        break
    cont += 1
    soma +=num
print("Foram {} números digitados, e a soma deles é {}".format(cont, soma))

nome = "José"
idade = 33

print(f"{nome} tem {idade} anos")