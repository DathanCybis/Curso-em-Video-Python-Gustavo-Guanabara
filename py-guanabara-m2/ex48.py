#crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
from time import sleep
soma = 0
quant = 0
for i in range(3, 500, 6):
    soma = soma + i
    quant = quant + 1
print("A soma de todos os {} números ímpares múltiplos de 3 entre 1 a 500 é {}".format(quant, soma))

