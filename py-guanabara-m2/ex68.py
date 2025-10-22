#crie um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador perder, 
#mostrando o total de vitórias consecutivas no final.

from random import randint
cont = 0

while True:
    comp = randint(1, 10)
    joga = int(input("Digite um valor de 1 a 10: "))
    while True:
        pi = str(input("Par ou Ímpar? [P/I]: "))
        if pi in "PpIi":
            break
    if pi in "Pp":
        soma = joga + comp
        if soma % 2 == 0:
            print(f"J = {joga}, C = {comp}, Jogador vence com PAR!")
            cont += 1
        else:
            print(f"J = {joga}, C = {comp}, Computador vence com ÍMPAR!")
            break
    if pi in "Ii":
        soma = joga + comp
        if soma % 2 == 1:
            print(f"J = {joga}, C = {comp}, Jogador vence com ÍMPAR!")
            cont += 1
        else:
            print(f"J = {joga}, C = {comp}, Computador vence com PAR!")
            break

print(f"Fim do jogo! você venceu {cont} vezes!")
