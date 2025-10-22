#crie um programa que faça uma contagem regressiva de 0 a 10 com uma pausa de 1s entre eles.
from time import sleep
from emoji import emojize

for c in range(10, 0-1, -1):
    print(c)
    sleep(1)
print("BOOOOOOOOOOMMMMMMMMM!!")
print(emojize(":fireworks::fireworks::fireworks::fireworks::fireworks::fireworks:"))
