#crie um programa que leia uma frase qualquer e diga se ela é ou não um palíndrimo, desconsiderando os espaços

frase = str(input("Digite uma frase: ")).strip()
frase = frase.upper()
frase = frase.replace(" ", "")
frasein = frase[::-1]
print("O inverso de {} é {}".format(frase, frasein))

if frase == frasein:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")