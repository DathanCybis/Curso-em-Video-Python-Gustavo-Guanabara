#crie um programa que leia o nome e o preço de vários itens. ele deverá perguntar se o usuário quer continuar. 
#No final mostre: a) qual o total gasto na compra b) quantos produtos custam mais de R$1000 c) qual é o nome do produto mais barato
total = qnt = cont = 0


while True:
    nome = str(input("Nome do produto: ")).strip()
    preco = float(input("Valor: R$"))
    cont += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome
    total += preco
    if preco > 1000:
        qnt += 1

    sn = " "
    while sn not in "SsNn":
        sn = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if sn in "Nn":
        break

print("\n===Fim do programa!===")
print(f"O total gasto na compra foi de R${total:.2f}")
print(f"No total {qnt} produtos custam mais de R$1000.00")
print(f"O nome do produto mais barato é {barato} e o valor é de R${menor:.2f}")
