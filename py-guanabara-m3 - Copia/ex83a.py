#crie um programa que leia uma expressão qualquer que use párênteses. O programa deverá 
#analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expre = str(input("Digite a expressão: ")).strip()
pilha = []

for i in expre:
    if "(" in i:
        pilha.append(i)
    elif ")" in i:
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(i)
            break

if len(pilha) == 0:
    print("Expressão válida")
else:
    print("Expressão inválida")
