def tit(txt):
    print("=-" * 30)
    print(f"{txt:^60}")
    print("=-" * 30)


tit("Aula em Python")
tit("Aprendendo Muito!")
tit("Muito Bom!")
print()

def soma(a, b):
    s = a + b
    print(s)


soma(9, 5)
soma(43, 24)
soma(4, 7)
print()

def contador(* num):
    tam = len(num)
    print(f"Recebi os valores {num} e ao todo são {tam} números")


contador(2, 5, 7)
contador(7, 3, 8, 9, 0)
contador(1, 3)
print()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    
valores = [2, 6, 2, 3, 9, 7, 8]

print(valores)
dobra(valores)
print(valores)
print()


def somaa(* valores):
    s = 0
    for i in valores:
        s += i
    print(f"Somando {valores} temos {s}")


somaa(2, 5, 7)
somaa(3, 4)
somaa(9, 8, 2, 4, 3)