#crie um programa que o usuário digite 5 valores e cadastre-os em uma lista, já na posição correta, 
#no final mostre a lista ordenada na tela. #proibido usar o .sort()
lista = []
for c in range(1, 6):
    n = int(input("Digite um número: "))
    if c == 1 or n > lista[-1]:
        lista.append(n)
        print("Valor adicionado ao final da lista.")
    else:
        pos = 0
        while pos <= len(lista):
            if n < lista[pos]:
                lista.insert(pos, n)
                print(f"Valor adicionado na posição {pos} da lista.")
                break
            pos += 1

print(f"A lista é {lista}")