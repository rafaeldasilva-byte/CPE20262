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

print(f"=== ENVIO ===\n{n0} - {n1} - {n2} - {n3} - {n4} - {n5} - {n6} - {n7} - {n8} - {n9}")

if ruido == 0:
    crc1 = crc1
elif ruido == 1:
    n1 = 1
elif ruido == 2:
    n2 = 2
elif ruido == 3:
    n3 = 3
elif ruido == 4:
    n4 = 4
elif ruido == 5:
    n5 = 5
elif ruido == 6:
    n6 = 6
elif ruido == 7:
    n7 = 7
elif ruido == 8:
    n8 = 8
elif ruido == 9:
    n9 = 9

crc1 = (crc1 * 3 - n1) % 97
crc1 = (crc1 * 3 - n2) % 97
crc1 = (crc1 * 3 - n3) % 97
crc1 = (crc1 * 3 - n4) % 97
crc1 = (crc1 * 3 - n5) % 97
crc1 = (crc1 * 3 - n6) % 97
crc1 = (crc1 * 3 - n7) % 97
crc1 = (crc1 * 3 - n8) % 97
crc1 = (crc1 * 3 - n9) % 97
crc1 = (crc1 * 3 - n1) % 97

print(f"CRC = {crc1}")

print(f"=== RECEBIDO ===\n{n0} - {n1} - {n2} - {n3} - {n4} - {n5} - {n6} - {n7} - {n8} - {n9}")

crc2 = 0
crc2 = (crc2 * 3 - n1) % 97
crc2 = (crc2 * 3 - n2) % 97
crc2 = (crc2 * 3 - n3) % 97
crc2 = (crc2 * 3 - n4) % 97
crc2 = (crc2 * 3 - n5) % 97
crc2 = (crc2 * 3 - n6) % 97
crc2 = (crc2 * 3 - n7) % 97
crc2 = (crc2 * 3 - n8) % 97
crc2 = (crc2 * 3 - n9) % 97
crc2 = (crc2 * 3 - n1) % 97

