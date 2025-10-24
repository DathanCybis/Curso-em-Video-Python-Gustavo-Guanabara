#crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, 
#mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
lista = []
temp = []
media = cont = 0
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    cont+=1
    media = (n1 + n2) / 2
    temp.append(nome)
    temp.append(n1)
    temp.append(n2)
    temp.append(media)
    lista.append(temp[:])
    temp.clear()

    sn = str(input("Quer continuar? [S/N]: "))
    if sn in "Nn":
        break
print()
print(f"{"Nº.":<4}{"NOME":<10}{"MEDIA":>8}")
print("--"*15)
for i in range(0, cont):
    print(f"{i:<4}{lista[i][0]:<10}{lista[i][3]:>6.1f}")
print("--"*15)
print()
while True:
    mostrar = int(input("Mostrar a nota de qual aluno? (999 para fim): "))
    if mostrar == 999:
        break
    elif mostrar < 0:
        print("Número inválido, tente novamente")
    elif mostrar < len(lista):
        print(f"As notas de {lista[mostrar][0]} foram: {lista[mostrar][1], lista[mostrar][2]}")
    elif mostrar > len(lista):
        print("Número inválido, tente novamente!")

print("Fim do programa!")
