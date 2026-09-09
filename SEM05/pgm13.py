#Programa que imprime todos os números primos até o o limite
#Rafael H - 09/09/2026

limite=input("Digite um número para o limite: ")

while limite.isalpha():
    limite=(input("Digite um número para o limite: "))

limite = int(limite)
print(limite)

for i in range(1,limite+1):
    primo=True
    if i>1:
        for j in range(2,i):
            if (i%j) == 0:
                primo = False
                break
    if primo == True:
        print(i)

#utilizando o teorema

from math import sqrt

limite=input("Digite um número para o limite: ")

while limite.isalpha():
    limite=(input("Digite um número para o limite: "))

limite = int(limite)
print(limite)

for i in range(1,limite+1):
    primo=True
    if i>1:
        for j in range(2,int((limite+1)**(1/2))):
            if (i%j) == 0:
                primo = False
                break
    if primo == True:
        print(i)

