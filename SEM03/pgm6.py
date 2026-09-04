# Programa da cifra de César
# Rafael H - 28/08/2026
import random
import sys
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
palavra = input ("Digite uma palavra a de 5 letras a ser criptografada: ")
if not palavra.isalpha():
    print("A palavra deve conter apenas letras")
    sys.exit()
if len(palavra) != 5:
    print("Palavra inválida.")
    sys.exit()
palavra = palavra.upper()
cifra = ""
deslocamento = input ("Digite um número de 1 a 10 para a chave de criptografia: ")
aleatorio = random.randint(0,26)

if not deslocamento.isdigit():
    print ("Digite apenas um número.")
    sys.exit()
deslocamento = int(deslocamento)
if (deslocamento > 10 or deslocamento < 1):
    print ("Número para chave incorreto!")
    sys.exit()
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[0], " -> ", alfabeto[cifra])

aleatorio = random.randint(0,26)
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[1], " -> ", alfabeto[cifra])

aleatorio = random.randint(0,26)
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[2], " -> ", alfabeto[cifra])

aleatorio = random.randint(0,26)
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[3], " -> ", alfabeto[cifra])

aleatorio = random.randint(0,26)
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[4], " -> ", alfabeto[cifra])