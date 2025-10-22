#crie um programa que leia números inteiros e, no final da execução, mostre a média entre todos os valores e 
#qual foi o maior e o menor valor lido. O programa deve perguntar se ele quer ou não continuar.

num = soma = qnt = maior = menor = 0
sn = ""
num = int(input("Digite um número inteiro: "))
maior = menor = num
while sn != "N":

    sn = str(input("Quer continuar [S/N]?: ")).upper().strip()
    soma += num
    if sn != "N":
        num = int(input("Digite um número inteiro: "))
    qnt += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

media = soma / qnt

print("Foram digitados {} números, a média desses valores foi de {}, o maior foi {} e o menor {}".format(qnt, media, maior, menor))