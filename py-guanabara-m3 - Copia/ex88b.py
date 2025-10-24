#crie um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar 
#quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
lista = []
cont = 0
print("=-"*30)
print(f"{"JOGUE NA MEGA SENA":^60}")
print("=-"*30)
jogos = int(input("Digite quantas vezes quer jogar: "))
print("GERANDO OS JOGOS VENCEDORES...")
for i in range(0, jogos):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    sleep(0.8)
    print(f"Jogo {i+1}: {lista}")
    lista.clear()
    cont = 0
print("====== Boa sorte! ======".upper())
