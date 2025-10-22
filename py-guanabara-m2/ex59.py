#crie um programa que leia 2 valores e mostre o menu de opções: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair
from time import sleep

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
escolha = 0

while escolha != 5:
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    """)
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
        sleep(2)
    elif escolha == 2:
        print("A multiplicação entre {} e {} é {}".format(n1, n2, n1 * n2))
        sleep(2)
    elif escolha == 3:
        if n1 > n2:
            print("O maior número entre {} e {} é {}".format(n1, n2, n1))
            sleep(2)
        elif n2 > n1:
            print("O maior número entre {} e {} é {}".format(n1, n2, n2))
            sleep(2)
        else:
            print("Não existe um número maior pois os valores são iguais")
            sleep(2)
    elif escolha == 4:
        print("Informe novamente os números")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        sleep(2)
    elif escolha == 5:
        print("Finalizando o programa...")
        sleep(3)
        print("Fim do programa, bom aprendizado!")
    else:
        print("Digite um valor válido!")
        sleep(1)