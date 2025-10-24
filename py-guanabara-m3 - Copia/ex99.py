#crie um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    print("=-" * 20)
    cont = maior = 0
    for i in num:
        cont += 1
        print(f"{i}", end = " ")
        if cont == 1:
            maior = i
        else:
            if i > maior:
                maior = i
    print(f"|> {len(num)} valores ao todo!")
    print(f"O maior valor informado foi {maior}")


maior(2, 4, 5)
maior(0)
maior()
maior(9, 4, 3, 2, 5)
maior(6)
maior(3, 7, 1)
