#aprimore o desafio anterior, ex86, mostrando no final: 
#a) a soma de todos os pares digitados b) a soma dos valores da terceira coluna c) o maior valor da segunda linha

from time import sleep
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = soma = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o valor para [{l}][{c}]: "))
print("GERANDO MATRIZ 3X3...")
sleep(1)
print("=-"*11)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if maior == 0:
                maior = matriz[l][c]
            elif matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print("=-"*11)
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da terceira coluna é {soma}")
print(f"O maior valor da segunda linha é {maior}")
