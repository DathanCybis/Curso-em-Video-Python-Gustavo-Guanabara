#crie um programa que sorteie um número de 0 a 10. O jogador tem que adivinhar até acertar e o programa dizer se é mais ou menos, 
#mostrando no final quantos palpites foram necessários.
from random import randint

print("========== JOGO DA ADIVINHAÇÃO ==========")
random = randint(0, 10)
joga = 11
quant = 0
print("Acabei de sortear um número de 0 a 10, tente adivinhar qual foi!")
while random != joga:
    joga = int(input("Digite o seu palpite: "))
    quant += 1
    if random > joga:
        print("O valor sorteado é maior...")
    elif random < joga:
        print("O valor sorteado é menor...")


print("Parabéns, você acertou com {} tentativa(s)!".format(quant))
