# Completando códigos

from pgm30 import incluir, apagar, listar

#Claudia Jacy Barenco Abbas
#02.10.2026
import os
import sys

menu={}

while True:
      os.system('cls') 
      print("MENU")
      print("1. Incluir")
      print("2. Apagar")
      print("3. Listar")
      print("4. Sair")
      opcao = input("Digite a opcao desejada: ")
      match opcao:
            case "1":
                print("Incluir")
                incluir(menu)
                os.system('pause')
            case "2":
                print("Apagar")
                apagar(menu)
                os.system('pause')
            case "3":
                print("Listar")
                print(menu)
                os.system('pause')
            case "4":
                print("Saindo do programa.")
                sys.exit()
            case _:
                print("Opcao invalida. Tente novamente.")
