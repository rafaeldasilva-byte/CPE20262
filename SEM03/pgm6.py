# Programa da cifra de César
# Rafael H - 28/08/2026
import random
import sys
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
palavra = input ("Digite uma palavra de 7 letras a ser criptografada: ")
if (not palavra.isalpha() or len(palavra) != 7):
    print("A palavra deve conter apenas 7 letras.")
    sys.exit()
palavra = palavra.upper()
cifra = ""
deslocamento = (input ("Digite um número: "))
aleatorio = random.randint(0,26)

if not deslocamento.isdigit():
    print ("Digite apenas números.")
    sys.exit()

deslocamento = int(deslocamento)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]
aleatorio = random.randint(0,26)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]

aleatorio = random.randint(0,26)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]
aleatorio = random.randint(0,26)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]
aleatorio = random.randint(0,26)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]
aleatorio = random.randint(0,26)

if (aleatorio + deslocamento) > 27:
    (aleatorio + deslocamento) == (aleatorio + deslocamento) % 27
cifra += alfabeto[aleatorio + deslocamento]

print (cifra)




