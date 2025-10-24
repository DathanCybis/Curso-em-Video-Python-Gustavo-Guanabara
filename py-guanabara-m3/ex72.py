#crie um programa que tenha uma tupla totalmente preenchida por números extensos de 0 a 20. 
#O programa deverá ler um número dentro desse intervalo e mostrá-lo por extenso.

exten = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", 
         "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:

    num = int(input("Digite um número de 0 a 20: "))
    while num < 0 or num > 20:
        num = int(input("Número inválido, Digite um número de 0 a 20: "))
    print(f"Você digitou o número {exten[num]}")
    sn = " "    
    while sn not in "SsNn":
        sn = str(input("Você quer continuar? [S/N]: "))
    if sn in "Nn":
        break
print("Fim do programa")