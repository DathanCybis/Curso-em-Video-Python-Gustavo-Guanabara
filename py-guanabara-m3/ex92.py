#crie um programa que leia nome, ano de nascimente e carteira de trabalho e cadastre-os em um dicionário, se por acaso o CTPS for diferente de 0, 
#o dicionário receberá támbem o ano de contratação e o salário. Calcule e acrescente idade, e com quantos anos a pessoa vai se aposentar(35 de work)
from datetime import datetime
infos = {}
ano = datetime.now().year
infos['nome'] = str(input("Nome: ").title())
nasc = int(input("Ano de nascimento: "))
infos['idade'] = ano - nasc
infos['ctps'] = int(input("Carteira de trabalho (0 se não tem): "))

if infos['ctps'] == 0:
    print("-=" * 30)
    for k, v in infos.items():
        print(f"{k} tem o valor {v}")
else:
    infos['contratacao'] = int(input("Ano de contratação: "))
    infos['salario'] = float(input("Salário: R$"))
    infos['aposentadoria'] = 35 - (ano - infos["contratacao"]) + infos['idade']
    print("-=" * 30)
    for k, v in infos.items():
        print(f"{k} tem o valor {v}")
print("=-" * 30)
