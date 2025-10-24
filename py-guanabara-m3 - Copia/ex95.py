#crie um programa que aprimore o ex93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador
fut = {}
gol = []
time = []
while True: 
    gol.clear()
    fut['nome'] = str(input("Nome do jogador: ").strip().title())
    qnt = int(input(f"Quantas partidas {fut['nome']} jogou?: "))
    for i in range(0, qnt):
        golpart = int(input(f"   Quantos gols na partida {i+1}?: "))
        gol.append(golpart)
    fut['gols'] = gol.copy()
    fut['total'] = sum(gol)
    time.append(fut.copy())
    fut.clear()
    while True:
        sn = str(input("Quer continuar? [S/N]: "))
        if sn in 'SsNn':
            break
        else:
            print("Valor inválido, digite apenas S ou N.")
    if sn in "Nn":
        break
print("=-" * 30)
print(f"{'cod':<5} {'nome':<10} {'gols':>7} {'total':>13}")
print("--"*20)
cod = 0
for i in range(0, len(time)):
    print(f"{cod:<5} {time[cod]['nome']}",end="")
    print(" " * 10, end="")
    print(f"{time[cod]['gols']}", end="")
    print(" " * 8, end="")
    print(f"{time[cod]['total']}")
    cod += 1

while True:
    dados = int(input("Mostrar dados de qual jogador? (999 pra parar): "))
    if dados == 999:
        break
    elif dados > len(time)-1 or dados < 0:
        print(f"Dados inválidos, não existe jogador com o código {dados}.")
    else:
        print(f" -> Aproveitamento do jogador {time[dados]['nome']}")
        for i in range(0, len(time[dados]['gols'])):
            print(f"    => Na partida {i+1}, fez {time[dados]['gols'][i]} gols.")
    print("--" * 20)

print("Programa finalizado!!")
