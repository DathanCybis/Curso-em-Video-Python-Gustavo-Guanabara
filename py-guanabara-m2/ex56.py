#Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
#A média de idade do grupo, Qual é o nome do homem mais velho, Quantas mulheres tem menos de 20 anos. 
media = 0
fem = 0
maior = 0
velho = "a"
for i in range (1, 5):
    print("==== {}º PESSOA ====".format(i))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sx = str(input("Sexo [M/F]: ")).upper().strip()
    
    if sx == "F" and idade < 20:
        fem += 1
    elif sx == "M":
        if i == 1:
            maior = idade
            velho = nome
        elif idade > maior:
            maior = idade
            velho = nome
    
    if i == 1:
        media = idade
    elif i == 2:
        media = idade + media
    elif i == 3:
        media = idade + media
    else:
        media = idade + media
        media = media / 4

print("A média de idade do grupo é {:.2f}".format(media))
print("O homem mais velho tem {} anos e o nome dele é {}".format(maior, velho))
print("{} mulher(es) tem menos de 20 anos".format(fem))
