#crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, 
#só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
        else:
            print("Erro! Tente novamente!")
    
    
n = leiaint('Digite um número: ')
print(f"Você digitou o número {n}!")
