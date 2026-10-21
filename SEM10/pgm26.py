# Rafael Henrique Carvalho da Silva
# Programa de jogo da velha
# 20/10/2026
from sys import exit

velha = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

vez = 0

while True:
    vitoria=""
    r=0
    vez = vez+1

    print("")
    for i in velha:
        print(i)

    if not vez%2==0:
        simbolo = "X"
        n = 1
    else:
        simbolo = "O"
        n = 2

    #Preenchimento o tabuleiro
    while True:
        player = int(input(f"\nJogador {n} - Selecione uma posição: "))

        for i in range (3):
                for j in range (3):
                    if (1+(i*3)+j == player):
                            if (velha[i][j] == "X") or (velha[i][j] == "O"):
                                print("\nPOSIÇÃO JÁ PREENCHIDA.")
                                r=0
                            else:
                                velha[i][j] = simbolo
                                r=1
        if r==1:
            break

    #Validação de Vitórias
    for i in range(3):
        if velha[i][0]==velha[i][1]==velha[i][2]:
            vitoria = "linha"
        for j in range (i):
            if velha[0][j]==velha[1][j]==velha[2][j]:
                vitoria = "coluna"

    if velha[0][0]==velha[1][1]==velha[2][2]:
         vitoria = "diagonal"
    if velha[0][2]==velha[1][1]==velha[2][0]:
         vitoria = "diagonal"

    #Validação velha
    if vez == 9:
         print("")
         for i in velha:
                     print(i)
         print("\nJogo sem vencedor, velha.")
         exit()

    #Resultado
    if not vitoria=="":
        print("")
        for i in velha:
            print(i)
        print(f"\nVitória Jogador {n} por {vitoria} em {(vez+1)//2} rodadas completas.")
        exit()
        

