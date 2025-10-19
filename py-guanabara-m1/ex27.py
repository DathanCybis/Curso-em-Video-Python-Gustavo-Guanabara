#crie um programa que leia o nome completo de uma pessoa e mostre o primeiro e último nome separadamente

nome = str(input("Digite um nome completo: ")).strip()

print("A primeira parte do nome é {}\nA última parte do nome é {}".format(nome.split()[0], nome.split()[-1]))