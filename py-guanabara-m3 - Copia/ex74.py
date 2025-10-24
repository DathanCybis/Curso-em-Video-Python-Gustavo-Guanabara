#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, 
#mostre a listagem de números gerados e támbem indique o menor e o maior valor que estão na tupla

from random import randint
#nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
nums = tuple(randint(1, 10) for i in range(5))
print(f"Os números gerados foram: {nums}")
print(f"O maior valor foi: {sorted(nums)[4]}")
print(f"O menor valor foi: {sorted(nums)[0]}")
#print(f"{max(nums)}")
#print(f"{min(nums)}")
