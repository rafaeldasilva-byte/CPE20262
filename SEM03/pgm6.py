# Programa da cifra de César
# Rafael H - 28/08/2026
import random
import sys
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
<<<<<<< HEAD
palavra = input ("Digite uma palavra a de 5 letras a ser criptografada: ")
if not palavra.isalpha():
    print("A palavra deve conter apenas letras")
=======
palavra = input ("Digite uma palavra de 7 letras a ser criptografada: ")
if (not palavra.isalpha() or len(palavra) != 7):
    print("A palavra deve conter apenas 7 letras.")
>>>>>>> 65508b3c5247b3161cb83d901f1360f34e73ecf8
    sys.exit()
if len(palavra) != 5:
    print("Palavra inválida.")
    sys.exit()
palavra = palavra.upper()
cifra = ""
deslocamento = (input ("Digite um número: "))
aleatorio = random.randint(0,26)

if not deslocamento.isdigit():
    print ("Digite apenas números.")
    sys.exit()
<<<<<<< HEAD
deslocamento = int(deslocamento)
if (deslocamento > 10 or deslocamento < 1):
    print ("Número para chave incorreto!")
    sys.exit()
cifra = deslocamento + aleatorio
if cifra > 27:
    cifra = cifra % 27
print(palavra[0], " -> ", alfabeto[cifra])
=======

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



>>>>>>> 65508b3c5247b3161cb83d901f1360f34e73ecf8

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