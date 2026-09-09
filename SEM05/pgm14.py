#Programa do teorema de RSA
#Rafael H - 09/09/2026

from math import sqrt

n = int(input("Digite um produto de um primo: "))
p = 0
q = 0

for m in range (2, int(sqrt(n))):
    if n % m == 0:
        p=m
        q=n//m
        break
print (p, q)