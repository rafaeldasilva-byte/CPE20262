# Programa que mostra o tamanho da matrix quadrada
# Rafael H - 16/09/2026

matrix = int(input("Digite um número para matrix quadrada:\n"))
if matrix%2 ==0:
    impar = False
else:
    impar = True

for i in range (1, matrix+1):
    for j in range (1, matrix+1):
        if impar and (i == matrix-(matrix//2)) and (j == matrix-(matrix//2)):
            print("!",end="")
        elif i == j:
            print("#",end="")
        elif (j+i == matrix+1):
            print("&",end ="")
        else:
            print ("*",end="")
    print("")


