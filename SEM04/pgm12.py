# Programa que imprime todos os números ímpares de 1 até o limite digitado
# Rafael H - 04/09/2026
limite = (input("Digite um limite: "))

while not limite.isdigit():
    limite = input("Digite um número válido: ")
limite = int(limite)    

for num in range(1, limite+1):
    if not num % 2 == 0:
        print (num)