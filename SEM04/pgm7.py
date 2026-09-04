# Programa que separa um número apenas com operações matemáticas
# Rafael H - 02/09/2026

import sys
num = int(input("Digite um número de 6 algarismo: "))

if (num < 99999 or num > 999999):
    print ("Número inválido! Digite um número de 6 algarismos.")
    sys.exit()

n1 = num // 100000
n2 = num % 100000
print (n1)
n1 = n2 // 10000
n2 = num % 10000
print (n1)
n1 = n2 // 1000
n2 = num % 1000
print (n1)
n1 = n2 // 100
n2 = num % 100
print (n1)
n1 = n2 // 10
n2 = num % 10
print (n1)
n1 = n2 // 1
n2 = num % 1
print (n1)
