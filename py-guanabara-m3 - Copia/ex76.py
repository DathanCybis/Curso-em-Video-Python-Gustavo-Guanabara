#crie um programa que tenha uma tupla com nomes de produtos e preços na sequência, 
#no final mostre uma listagem de produtos e preços organizados de forma tabular

lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Tranferidor", 4.20, 
         "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("=" * 50)
print(f"{"LISTA DE PREÇOS":^50}")
print("=" * 50)

for c in range(0,len(lista),2):
    print(f"{lista[c]:.<38} R$ {lista[c+1]:7.2f}")

print("=" * 50)
