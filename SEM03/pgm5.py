# Tente adivinhar o número que será gerado pelo programa
# Rafael H - 28/08/2026

import random
import sys
aleatorio=random.randint(1,5)
numero=input("Digite um número de 1 a 5: ")
if not numero.isdigit():
    print("Número inválido.")
    sys.exit
numero = int(numero)
if (numero < 1 or numero > 5):
    print("Número inválido.")
    sys.exit()
if numero == aleatorio:
    print("Parabéns, você acertou :) .")
else:
    print (f"Que pena, você errou :( . O número correto era: {aleatorio}")