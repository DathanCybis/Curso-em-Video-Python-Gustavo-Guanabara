#crie um programa que melhore o anterior, perguntando ao usuário se ele quer mostrar mais alguns termos. 
#o programa encerra quando ele dizer 0 termos.

primeiro = int(input("Digite o valor do primeiro termo: "))
razão = int(input("Digite o valor da razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end = "")
        cont += 1
        termo += razão
    print("PAUSA")
    mais = int(input("Quantos termos a mais você quer ver?: "))

print("Programa finalizado com {} termos exibidos!".format(total))