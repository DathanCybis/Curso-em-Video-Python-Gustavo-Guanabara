#crie um programa e reescreva a função leiaint() que fizemos no ex104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(txt):
    while True:
        try:
            msg = int(input(txt))
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return 0
        except:
            print("\033[31mErro! Por favor, digite um número inteiro válido!\033[m")
        else:
            return msg


def leiafloat(txt):
    while True:
        try:
            msg = float(input(txt))
            return msg
        except (KeyboardInterrupt):
            print("\033[31mEntrada de dados interrompida pelo usuário!\033[m")
            return 0
        except:
            print("\033[31mErro! Por favor, digite um número inteiro válido!\033[m")


num1 = leiaint("Digite um número inteiro: ")
num2 = leiafloat("Digite um número real: ")
print(f"\033[32mO número inteiro digitado foi {num1} e o real foi {num2}\033[m")
