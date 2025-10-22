#crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

comp = randint(1,3)

print("""ESCOLHA SUA JOGADA -
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA""")
joga = int(input("Digite sua escolha: "))

print ("\nJO")
sleep(1)
print ("KEN")
sleep(1)
print ("PO!!!!")
sleep(1)

if joga == 1 or joga == 2 or joga == 3:
    
    if joga == 1 and comp == 3:
        print("\nJogador jogou PEDRA")
        print("Computador jogou TESOURA")
        print("=== JOGADOR VENCE ===\n")

    elif joga == 2 and comp == 1:
        print("\nJogador jogou PAPEL")
        print("Computador jogou PEDRA")
        print("=== JOGADOR VENCE ===\n")

    elif joga == 3 and comp == 2:
        print("\nJogador jogou TESOURA")
        print("Computador jogou PAPEL")
        print("=== JOGADOR VENCE ===\n")

    elif comp == 2 and joga == 1:
        print("\nJogador jogou PEDRA")
        print("Computador jogou PAPEL")
        print("=== COMPUTADOR VENCE ===\n")

    elif comp == 1 and joga == 3:
        print("\nJogador jogou TESOURA")
        print("Computador jogou PEDRA")
        print("=== COMPUTADOR VENCE ===\n")

    elif comp == 3 and joga == 2:
        print("\nJogador jogou PAPEL")
        print("Computador jogou TESOURA")
        print("=== COMPUTADOR VENCE ===\n")

    elif joga == 1 and comp == 1:
        print("\nJogador jogou PEDRA")
        print("Computador jogou PEDRA")
        print("=== EMPATE ===")
    elif joga == 2 and comp == 2:
        print("\nJogador jogou PAPEL")
        print("Computador jogou PAPEL")
        print("=== EMPATE ===")
    else:
        print("\nJogador jogou TESOURA")
        print("Computador jogou TESOURA")
        print("=== EMPATE ===")

else:
    print("\nDigite uma escolha válida!")