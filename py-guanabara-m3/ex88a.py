#crie um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar 
#quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
num = []
print("=-"*30)
print(f"{"JOGUE NA MEGA SENA":^60}")
print("=-"*30)
jogos = int(input("Digite quantos jogos quer que eu sorteie: "))
print("GERANDO OS JOGOS VENCEDORES...")
while len(num) != 6:
    for i in range(0, jogos):
        for n in range(0, 6):
            sorte = randint(1, 60)
            print(sorte)
            if sorte not in num:
                num.append(sorte)
        num.sort()
        sleep(0.7)
        print(f"Jogo {i+1}:  {num}")
        num.clear()
    print(f"=========================={len(num)}")
sleep(1)
print(" === BOA SORTE :D === ")
