#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

"""cidade = str(input("Digite o nome de uma cidade: ")).strip()

if cidade == cidade.split()[0] == "Santo":

    print(cidade)
else: 
    print("False")
"""



"""cidade = str(input("Digite o nome de uma cidade: ")).strip()

c = cidade.upper()

if c.startswith("SANTO"):
    
    print("True")

else:

    print("False")
"""




cid = str(input("Digite uma cidade: ")).strip()

print(cid[:5].upper() == "SANTO")