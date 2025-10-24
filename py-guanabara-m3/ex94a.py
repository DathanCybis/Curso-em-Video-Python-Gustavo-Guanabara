#crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários 
#em uma lista. No final, mostra: a) quantas pessoas cadastradas b) a média de idade c) uma lista com mulheres d) uma lista com idade acima da média
pessoas = {}
lista = []
mulheres = []
soma = media = 0
while True:
    pessoas['nome'] = str(input("Nome: ").strip().title())
    while True:
        sx = str(input("Sexo [M/F]: ").strip().upper())
        if sx in "MF":
            pessoas['sexo'] = sx
            break
        else:
            print("Valor inválido, por favor, digite apenas M ou F.")
    pessoas['idade'] = int(input("Idade: "))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True: 
        sn = str(input("Quer continuar? [S/N]: "))
        if sn in "NnSs":
            break
        else:
            print("Digite um valor válido! S ou N.")
    if sn in "Nn":
            break
print("=-" * 30)
print(f"Existem {len(lista)} pessoas cadastradas na lista")
media = soma / len(lista)
print(f"A média de idade das pessoas é: {media:.1f}")
for i in lista:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
print(f"As mulheres cadastradas foram: {mulheres}")
print("Uma lista das pessoas que estão acima da média: ")
for i in range(0, len(lista)):
    if lista[i]['idade'] >= media:
        print(f"   {lista[i]}")
