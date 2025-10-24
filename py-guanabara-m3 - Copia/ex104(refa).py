#crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, 
#só que fazendo a validação para aceitar apenas um valor numérico.

def leiaint(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            txt = int(num)
            return txt
        else:
            print("Erro! Digite um valor válido!")


num = leiaint("Digite um número: ")
print(f"O número que você digitou é: {num}")
