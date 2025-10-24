#crie um programa que tenha uma função fatorial() que receba dois parâmentros: o primeiro que indique o número a calcular 
#e o outro chamado show, que será um valor lógico(opcional) indicando se será ou não mostrado na tela o processo de cálculo do fatorial.

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número n
    -> Feito por Dan.C
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            if c == 1:
                print(f'{c} =',end = " ")
            else:
                print(f'{c} x',end = " ")
    return f


print(fatorial(5, show=True))
print(fatorial(6))
print(fatorial(6, show=False))
print(fatorial(6, show=True))
#help(fatorial)
