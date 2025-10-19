#crie um programa que leia a distância de uma viagem em km. cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para as mais longas

dist = float(input("Qual a distância da viagem?: "))

if dist <= 200:
    cobrar = 0.50 * dist
    print ("Sua viagem de {:.1f}Km vai lhe custar R${:.2f}".format(dist, cobrar))
else:
    cobrar = 0.45 * dist
    print ("Sua viagem de {:.2f}Km vai lhe custar R${:.2f}".format(dist, cobrar))