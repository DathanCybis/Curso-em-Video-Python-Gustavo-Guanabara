#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(an=2018):
    idade = 2018 - an

    if idade >= 65 or idade == 16 or idade == 17:
        print(f"Com {idade} o voto é OPCIONAL")
    elif idade >= 18:
        print(f"Com {idade} o voto é OBRIGATÓRIO.")
    else:
        print(f"Com {idade} não vota. ")


voto()
