#crie um programa e reescreva a função leiaint() que fizemos no ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(txt):
    while True:
        msg = str(input(txt))
        try:
            txt = int(msg)
            return txt
        except:
            print("\033[31mErro! Por favor, digite um número inteiro válido!\033[m")


def leiafloat(txt):
    while True:
        msg = str(input(txt))
        try:
            txt = float(msg)
            return txt
        except:
            print("\033[31mErro! Por favor, digite um número inteiro válido!\033[m")


num1 = leiaint("Digite um número inteiro: ")
num2 = leiafloat("Digite um número real: ")
print(f"O número inteiro digitado foi {num1} e o real foi {num2}")
