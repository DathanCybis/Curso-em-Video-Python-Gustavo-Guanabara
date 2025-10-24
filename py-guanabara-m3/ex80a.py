#crie um programa que o usuário digite 5 valores e cadastre-os em uma lista, já na posição correta, 
#no final mostre a lista ordenada na tela. #proibido usar o .sort()
lista = []
for i in range(1, 6):
    num = int(input("Digite um número: "))
    if i == 1 or num > lista[-1]:
        lista.append(num)
        print("Valor adicionado na última posição da lista...")
    else:
        pos = 0
        while pos <= len(lista):
            if num < lista[pos]:
                print(f"Valor adicionado na posição {pos} da lista...")
                lista.insert(pos, num)
                break
            pos += 1

print(f"A lista com os valores digitados de forma ordenada é {lista}")