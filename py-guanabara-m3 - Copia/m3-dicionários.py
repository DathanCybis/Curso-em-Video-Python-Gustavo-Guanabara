pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(pessoas)
print(pessoas["nome"])
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos")
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas["idade"]
pessoas["nome"] = "Leandro"
pessoas["peso"] = 98.5
for k, v in pessoas.items():
    print(f"{k} = {v}")
brasil = []
estado1 = {'uf': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['sigla'])
etd = {}
br = []
for c in range(0, 3):
    etd['uf'] = str(input("Unidade federativa: "))
    etd['sigla'] = str(input("Sigla: "))
    br.append(etd.copy())
print(br)

for e in br:
    for k, v in e.items():
        print(k, v)