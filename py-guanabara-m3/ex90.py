#crie um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
#abaixo de 5 reprovado, abaixo de 7 recuperação, 7 ou mais é aprovado.

prova = {}

prova['nome'] = str(input("Nome: "))
prova['media'] = float(input("Média: "))

if prova['media'] < 5:
    prova['situacao'] = "Reprovado"
elif prova['media'] < 7:
    prova['situacao'] = "Recuperação"
elif prova['media'] <= 10:
    prova['situacao'] = "Aprovado"
print("=-"*30)
for c, v in prova.items():
    print(f" - {c} é igual a {v}")
print("-="*30)
