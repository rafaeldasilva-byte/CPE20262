#Menu de testes
#Rafael Henrique - 02/10/2026
import sys
import os


while True:
    os.system("cls")
    print("=== MENU ===")
    print("1 - Incluir")
    print("2 - Apagar")
    print("3 - Listar")
    print("4 - Para programa")

    opcao = int(input("Número de menu: "))
    match opcao:
        case 1:
            print("Incluir")
            os.system("pause")
        case 2:
            print("Apagar")
            os.system("pause")
        case 3:
            print("Listar")
            os.system("pause")
        case 4:
            exit()
        case _:
            print("Número inválido, digite um número de 1 a 4.")
