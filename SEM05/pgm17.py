#Programa que imprime o decimal em binário
#Rafael Henrique - 11/09/2026

n = int(input("digite um número natural:\n"))
f = n
r = ""
for _ in range (4):
    a = n % 2
    r += str(a)
    n = n // 2
    if n>2:
        break
print(f"{f} = {r[::-1]}")
