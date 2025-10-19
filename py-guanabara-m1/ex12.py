#crie um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input("Digite o preço do produto: "))

desconto = (preco * 5) / 100

print("O novo preço do seu produto com desconto é: {:.2f}".format(preco - desconto))