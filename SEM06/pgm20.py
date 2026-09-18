#Programa de jogo da forca
# Rafael H - 18/09/2026

import os
import sys

palavra = input("Digite a palavra inicial: ")
palavra = palavra.lower()

os.system("cls")
tentativa = "_"*len(palavra)
print(tentativa)

while True:
    letra = input("\nDigite uma letra: ")
    print("")
    letra = letra.lower()
    for i in range (len(palavra)):
        if letra == palavra[i]:
            tentativa = tentativa[0:i]+letra+tentativa[i+1::]
            print(tentativa)
    if tentativa == palavra:
         print("Parabéns você acertou!🥳")
         sys.exit()
    



