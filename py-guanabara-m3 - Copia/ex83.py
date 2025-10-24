#crie um programa que leia uma expressão qualquer que use párênteses. O programa deverá 
#analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#expre = []
qnt1 = qnt2 = 0

expre = str(input("Digite sua expressão: ")).strip()

for i, v in enumerate(expre):
    
    if v == "(":
        qnt1 += 1
    elif v == ")":
        qnt2 += 1

if qnt1 == qnt2:
    print("Expressão válida")
else:
    print("Expressão inválida")
