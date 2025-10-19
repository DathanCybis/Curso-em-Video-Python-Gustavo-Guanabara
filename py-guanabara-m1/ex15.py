#crie um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int(input("Por quantos dias o carro foi alugado?: "))
km = float(input("Quantos km você percorreu com ele?: "))

preco = (dias * 60) + (km * 15 / 100)

print("O valor total a pagar é de: R${:.2f}".format(preco))