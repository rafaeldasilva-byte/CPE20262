#Programa que imprime o decimal em binário
#Rafael Henrique - 11/09/2026

n = int(input("digite um número natural:\n"))
r = ""
while not n == 0:
    a = n % 2
    r += str(a)
    n = n // 2
print(f"{r[::-1]}")
