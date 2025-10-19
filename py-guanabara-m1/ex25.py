#crie um programa que leia um nome e diga se tem "SILVA" no nome

nome = str(input("Digite um nome: ")).strip()

print("{}".format("SILVA" in nome.upper()))