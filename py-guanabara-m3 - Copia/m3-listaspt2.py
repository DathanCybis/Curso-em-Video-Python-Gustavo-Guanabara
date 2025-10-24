teste = []
teste.append("Gustavo")
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 34
galera.append(teste[:])
print(galera)

rpz = [["João", 32], ["Joana", 22], ["Carmen", 63], ["Miguel", 51]]

#print(rpz)
#print(rpz[1][1])
for p in rpz:
    print(p[1])

pessoas = []
dados = []

for i in range(1, 4):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

maior = menor = 0
for p in pessoas:
    if p[1] >= 18:
        print(f"{p[0]} é maior de idade.")
        maior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        menor += 1

print(f"Temos {maior} maiores e {menor} menores de idade.")
