# Programa da cifra de César
# Rafael H - 28/08/2026
import random
import sys
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
palavra = input ("Digite uma palavra a ser criptografada: ")
if not palavra.isalpha():
    print("A palavra deve conter apenas letras")
    sys.exit()
palavra = palavra.upper()
cifra = ""
deslocamento = input ("Digite um número de 1 a 10 para a chave de criptografia: ")
aleatorio = random.randint(0,26)

if not deslocamento.isdigit():
    print ("Digite apenas um número.")
    sys.exit()
cifra = deslocamento + aleatorio
alfabeto[aleatorio] = alfabeto[cifra]

