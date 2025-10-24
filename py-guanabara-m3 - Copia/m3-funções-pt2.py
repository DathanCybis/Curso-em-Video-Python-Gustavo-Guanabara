#return
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#n = int(input("Digite um número: "))
f1 = fatorial(6)
f2 = fatorial(5)
f3 = fatorial()
print(f"Os fatoriais dos números escolhidos foram {fatorial(5)}, {f1}, {f2}, {f3}") #n
print()


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(par(7))
print(par(6))
print()

