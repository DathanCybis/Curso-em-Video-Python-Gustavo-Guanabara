#crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato
fut = {}
fut['nome'] = str(input("Nome do jogador: ").strip().title())
qnt = int(input(f"Quantas partidas {fut['nome']} jogou?: "))
gol = []
somagol = golpart = 0
for i in range(0, qnt):
    golpart = int(input(f"   Quantos gols na partida {i+1}?: "))
    gol.append(golpart)
    somagol += golpart
fut['gols'] = gol
fut['total'] = somagol # ou fut['total'] = sum(gol)
print("=-" * 30)
print(fut)
print("=-" * 30)
for k, v in fut.items():
    print(f"O campo {k}, tem o valor {v}")
print("=-" * 30)
print(f"O jogador {fut['nome']} jogou {qnt} partidas.")
for i, v in enumerate(gol):
    print(f"    => Na partida {i+1}, fez {v} gols.")
print(f"Total de {somagol} gols.")
