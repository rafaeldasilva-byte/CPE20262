#Programa que simula transmissão por meio do CRC
#Rafael H - 09/09/2026

#int(input("Digite um número"))
from random import randint

crc1 = 0
ruido = randint(0,10)

n0 = int(input("Primeiro número de leitura: "))
n1 = int(input("Seguno número de leitura: "))
n2 = int(input("Terceiro número de leitura: "))
n3 = int(input("Quarto número de leitura: "))
n4 = int(input("Quinto número de leitura: "))
n5 = int(input("Sexto número de leitura: "))
n6 = int(input("Sétimo número de leitura: "))
n7 = int(input("Oitavo número de leitura: "))
n8 = int(input("Nono número de leitura: "))
n9 = int(input("Décimo número de leitura: "))

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
elif ruido == 2:
    n1 = 2
elif ruido == 3:
    n2 = 3
elif ruido == 4:
    n3 = 4
elif ruido == 5:
    n4 = 5
elif ruido == 6:
    n5 = 6
elif ruido == 7:
    n6 = 7
elif ruido == 8:
    n7 = 8
elif ruido == 9:
    n8 = 9
elif ruido == 10:
    n9 = 10

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
    print(f"\n⚠️  ERRO DE TRANSMISSÃO DETECTADO!\nOcorreu interferência no canal! O dado na posição {ruido} foi corrompido.")
else:
    print(f"\n✅  TRANSMISSÃO BEM SUCEDIDA!\nO dado foi transmitido com sucesso, sem interferência no canal.")

