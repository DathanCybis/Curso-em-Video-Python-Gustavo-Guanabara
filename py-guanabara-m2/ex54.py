#crie um programa que leia o ano do nascimento de 7 pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantos já.
contmaior = 0
contmenor = 0
ano = 2025


for i in range (1, 8):
    nasc = int(input("Digite o ano do nascimento: "))
    idade = ano - nasc
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

print("Nesse grupo de 7 pessoas, {} são de maior, e {} de menor".format(contmaior, contmenor))