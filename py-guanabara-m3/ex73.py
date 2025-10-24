#crie uma tabela com os primeiros 20 colocados da tabela do brasileirão, na ordem de colocação, depois mostre: 
#a) os 5 primeiros b) os 4 últimos c) times em ordem alfabética d) em que posição está o time do Bragantino

times = ("Flamengo", "Cruzeiro", "Palmeiras", "Mirassol", "Botafogo", "Bahia", "São Paulo", "Bragantino", "Corinthians", 
         "Fluminense", "Ceará SC", "Internacional", "Atlético-MG", "Grêmio", "Vasco da gama", 
         "Santos", "EC Vitória", "Juventude", "Fortaleza", "Sport Recife")

print("=-" * 85)
print(f"Lista de times do brasileirão: {times}")
print("=-" * 85)
print(f"Os 5 primeiros são: {times[0:5]}")
print("=-" * 85)
print(f"Os 4 últimos são: {times[-4:]}")
print("=-" * 85)
print(f"(Lista em ordem alfabética: {sorted(times)}")
print("=-" * 85)
print(f"O Bragantino está na {times.index("Bragantino")+1}º posição")
print("=-" * 85)