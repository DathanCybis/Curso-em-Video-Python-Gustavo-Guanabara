#crie um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, 
#peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite seu sexo [M/F]: ")).upper().strip()

while sexo != "M" and sexo != "F":

    sexo = str(input("Valor inválido, digite seu sexo [M/F]: ")).upper().strip()
    
print("Sexo {} cadastrado com êxito!".format(sexo))