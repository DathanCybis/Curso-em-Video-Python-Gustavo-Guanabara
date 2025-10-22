#crie um programa que leia vários números inteiros. O programa só vai parar quando o usuario digitar 999. No final, 
#mostre quantos números foram digitados e qual foi a soma entre eles.

usuario = 0
soma = 0
qnt = 0
while usuario != 999:
    usuario = int(input("Digite um valor inteiro [999 pra parar]: "))
    if usuario != 999:
        qnt += 1
        soma += usuario

print("Foram digitados {} números e a soma entre eles é {}".format(qnt, soma))