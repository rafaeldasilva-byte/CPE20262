# Programa que calcula o fatorial de um número
# Rafael Henrique - 11/09/2026

n = int(input("Digite um número:\n"))
f = n

for s in range(1,n):
    n = n * s 
print(f"{f}! = {n}")
