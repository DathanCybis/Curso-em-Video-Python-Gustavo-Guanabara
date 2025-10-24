#crie um programa que o usuário digite 5 valores e cadastre-os em uma lista, já na posição correta, 
#no final mostre a lista ordenada na tela. #proibido usar o .sort()
lista = []

for c in range (1, 6):
    num = int(input("Digite um número: "))
    if c == 1 or num > lista[-1]:
        lista.append(num)
        print("Adicionado na última posição da lista...")
    else:
        pos = 0
        while pos < len(lista):  
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f"adicionado na posição {pos} da lista...")
                break
            pos+=1

print(lista)