#crie um programa que pergunte o salário de um funcionário e calcule o seu aumento. salários acima de 1250 + 10% - inferiores ou iguais, 15%.

sal = float(input("Digite um salário: R$"))

if sal <= 1250:
    aum = (sal * 15) / 100
    sal = aum + sal

else:
    aum = (sal * 10) / 100
    sal = aum + sal

print("Seu salário após o aumento passou a ser de R${:.2f}".format(sal))