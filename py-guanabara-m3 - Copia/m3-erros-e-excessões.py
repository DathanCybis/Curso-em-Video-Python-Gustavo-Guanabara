try:
    a = 10
    b = 2
    r = a/b

except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")

except (ValueError, TypeError):
    print("Tivemos problemas com o tipo de dados que você forneceu!")

except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados")

except Exception as erro:
    print("Infelizmente tivemos um problema :/")
    print(f"Problema encontrado no {erro.__class__, erro.__cause__}")

else:
    print(f"O resultado é {r:.1f}")
    
finally:
    print("Obrigado por usar nosso programa. Volte sempre!")
