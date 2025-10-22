#crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#Quando um valor negativo for digitado o programa será interrompido.

while True:
    esc = int(input("Qual tabuada você quer ver?: "))
    print("=-"*20)
    if esc < 0:
        break
    for i in range(1, 11):
        print(f"{esc} x {i} = {esc * i}")
    print("=-"*20)  
print("Fim do programa!")