#média abaixo de 5.0 reprovado, entre 5.0 e 6.9 recuperação e média 7 ou acima aprovado.
#crie um programa que leia duas notas e calcule sua média. e exiba: 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print("Sua média foi de {:.1f}, você está reprovado".format(media))
elif media >= 5 and media < 7:
    print("Sua média foi de {:.1f}, você está de recuperação".format(media))
else:
    print("Sua média foi de {:.1f}, você está aprovado".format(media))