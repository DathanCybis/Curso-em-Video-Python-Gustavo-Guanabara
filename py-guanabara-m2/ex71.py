#crie um programa que simule o funcionamento de um caixa eletrônico. Pergunte ao usuário o valor a ser sacado, e o programa vai informar
#quantas cédulas de cada valor serão entregues. Considere que o caixa possui apenas cédulas de 50, 20, 10, e 1.
cinq = vinte = dez = um = 0
valor = int(input("\nDigite o valor a ser sacado: R$"))
while True:

    if valor >= 50:
        valor -= 50
        cinq += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    else:
        if cinq > 0:
            print(f"{cinq} cédula(s) de R$50,00 serão entregue(s)")
        if vinte > 0:
            print(f"{vinte} cédula(s) de R$20,00 serão entregue(s)")
        if dez > 0:
            print(f"{dez} cédula(s) de R$10,00 serão entregue(s)")
        if um > 0:
            print(f"{um} cédula(s) de R$1,00 serão entregue(s)")
        break

print("=== Fim do programa! ===\n")
