#Programa que simula transmissão por meio do CRC
#Rafael H - 09/09/2026

#int(input("Digite um número"))
from random import randint

crc1 = 0
ruido = randint(0,10)

n0 = 80
n1 = 56
n2 = 67
n3 = 40
n4 = 25
n5 = 68
n6 = 31
n7 = 94
n8 = 18
n9 = 73

print(f"=== ENVIADO ===\n{n0} - {n1} - {n2} - {n3} - {n4} - {n5} - {n6} - {n7} - {n8} - {n9}")

crc1 = (crc1 * 3 - n0) % 97
crc1 = (crc1 * 3 - n1) % 97
crc1 = (crc1 * 3 - n2) % 97
crc1 = (crc1 * 3 - n3) % 97
crc1 = (crc1 * 3 - n4) % 97
crc1 = (crc1 * 3 - n5) % 97
crc1 = (crc1 * 3 - n6) % 97
crc1 = (crc1 * 3 - n7) % 97
crc1 = (crc1 * 3 - n8) % 97
crc1 = (crc1 * 3 - n9) % 97

if ruido == 1:
    n0 = 1
    erro = n0
elif ruido == 2:
    n1 = 2
    erro = n1
elif ruido == 3:
    n2 = 3
    erro = n2
elif ruido == 4:
    n3 = 4
    erro = n3
elif ruido == 5:
    n4 = 5
    erro = n4
elif ruido == 6:
    n5 = 6
    erro = n5
elif ruido == 7:
    n6 = 7
    erro = n6
elif ruido == 8:
    n7 = 8
    erro = n7
elif ruido == 9:
    n8 = 9
    erro = n8
elif ruido == 10:
    n9 = 10
    erro = n9

print(f"CRC enviado = {crc1}\n")

print(f"=== RECEBIDO ===\n{n0} - {n1} - {n2} - {n3} - {n4} - {n5} - {n6} - {n7} - {n8} - {n9}")

crc2 = 0
crc2 = (crc2 * 3 - n0) % 97
crc2 = (crc2 * 3 - n1) % 97
crc2 = (crc2 * 3 - n2) % 97
crc2 = (crc2 * 3 - n3) % 97
crc2 = (crc2 * 3 - n4) % 97
crc2 = (crc2 * 3 - n5) % 97
crc2 = (crc2 * 3 - n6) % 97
crc2 = (crc2 * 3 - n7) % 97
crc2 = (crc2 * 3 - n8) % 97
crc2 = (crc2 * 3 - n9) % 97

print(f"CRC recebido = {crc2}")
if not crc1 == crc2:
    print(f"\n⚠️  ERRO DE TRANSMISSÃO DETECTADO!\nOcorreu interferência no canal! O dado na posição {erro} foi corrompido.")