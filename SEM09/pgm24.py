# Programa da forca com lista
# Rafael Henrique - 09/10/2026

import os
import sys

palavra = str(input("Palavra a ser adivinhada: ").lower())
os.system("cls" if os.name == "nt" else "clear")
adivinha = []

for i in range(len(palavra)):
    adivinha.append("-")

while True:
    letra = str(input("Digite uma letra: ").lower())
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                adivinha[i] = letra
        print("Parabéns 👌")
        print(" ".join(adivinha))
    else:
        print("Errou 😛")
    for i in range(len(palavra)):
        if palavra[i] == adivinha[i]:
            igual = True
        else:
            igual = False
    if igual:
        print("ACERTOU 🥳")
        print(" ".join(adivinha))
        break
    os.system("pause")
    os.system("cls")
  
