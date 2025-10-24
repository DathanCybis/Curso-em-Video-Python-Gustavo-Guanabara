#crie um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
#e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = []

def sorteia():
    print("Sorteando 5 valores em uma lista: ", end = "")
    for i in range(0, 5):
        nums = randint(1, 10)
        print(f"{nums}", end = " ")
        numeros.append(nums)
    print("- FIM!")


def somaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores pares de {numeros}, temos {soma}")


sorteia()
somaPar()