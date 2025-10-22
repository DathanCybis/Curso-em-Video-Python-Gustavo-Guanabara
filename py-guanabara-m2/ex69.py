#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou 
#não continuar, no final mostre: a) quantas pessoas tem mais de 18 anos. b) quantos homens foram cadastrados. 
#c) quantas mulheres tem menos de 20 anos
cont = qnt = fem = 0
while True:
    idade = int(input("Digite uma idade: "))
    sx = " "
    while sx not in "MmFf":
        sx = str(input("Digite o sexo [M/F]: "))

    if sx in "Mm":
        cont += 1
    if idade >= 18:
        qnt += 1
    if idade < 20 and sx in "Ff":
        fem += 1

    prox = " "
    while prox not in "SsNn":
        prox = str(input("Quer continuar? [S/N]: "))
    if prox in "Nn":
        break
           
print(f"Ao todo {qnt} pessoa(s) tem mais de 18 anos")
print(f"Ao todo {cont} homens foram cadastrados")
print(f"Ao todo {fem} mulher(es) tem menos de 20")
