#crie um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, 
#mostre uma mensagem que ele foi multado, e R$7,00 por km excedido.

velo = int(input("Digite a velocidade que você passou na via: "))



if velo > 80:
    multa = (velo - 80) * 7
    print("Você foi multado e deverá pagar R${},00 de multa!".format(multa))
else:
    print("Você não foi multado!")