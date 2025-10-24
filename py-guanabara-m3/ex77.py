#crie um programa que tenha uma tupla com várias palavras sem acentos. Depois mostre para cada palavra, suas vogais.

lista = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS", "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")


for c in lista:
    print(f"\nNa palavra  {c:^12} temos as vogais: ", end = "")
    for letras in c:
        if letras in "AEIOU":
            print(letras, end = " ")
