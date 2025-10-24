#crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso já exista, 
#ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente 18m - 10m - fizem8m

lista = []

while True:
    valor = int(input("Digite um número: "))

    if valor not in lista:
        lista.append(valor)
    else:
        print("Valor já existente, tente outro valor...")

    sn = str(input("Você quer continuar? [S/N]: ")).upper().strip()
    if sn in "N":
        break
print("Fim do programa!")
lista.sort()
print(f"Os valores únicos digitados foram {lista}")
