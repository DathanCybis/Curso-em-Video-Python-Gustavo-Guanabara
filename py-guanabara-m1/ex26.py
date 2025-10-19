#crie um programa que leia uma frase e mostre quantas vezes aparece a letra A, em que posição aparece pela primeira e última vez

frase = str(input("Digite uma frase: ")).strip().upper()

print("A letra A apareceu {} vezes".format(frase.count("A")))
print("A letra A apareceu pela primeira vez na posição: {}".format(frase.find("A")))
print("A letra A apareceu pela última vez na posição: {}".format(frase.rfind("A")))