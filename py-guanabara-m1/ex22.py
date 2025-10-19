#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas, com todas minúsculas, ao todo(sem considerar os espaços), e quantas tem a primeira parte do nome.

nome = str((input("Digite um nome e sobrenome: "))).strip()

print("Com todas maiúsculas: {}".format(nome.upper()))
print("Com todas minúsculas: {}".format(nome.lower()))
print("Ao todos sem espaços: {}".format(len(nome) - nome.count(" ")))
print("Primeira parte que é {} tem {} letras".format(nome.split()[0],nome.find(" ")))
