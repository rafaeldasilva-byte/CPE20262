# Completando códigos

#Rafael Henrique Carvalho da Silva
import os
import sys

def incluir(menu):
    id = input("Insira o ID para incluir: ")
    quantidade = int(input("Insira a quantidade: "))
    preço = float(input("Insira o preço (utilize \".\" para casas decimais): R$"))
    if not (id in menu):
        menu[id]=[str(quantidade),str(preço)]
    else:
        print("Este ID já existe.")

def apagar(menu):
    id = input("Insira o ID para apagar: ")
    if id in menu:
        del menu[id]
    else: 
        print("ID não encontrado.")

menu={}

def main():
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
                    print("\n=== INCLUIR PRODUTO ===")
                    incluir(menu)
                    os.system('pause')
                case "2":
                    print("\n=== APAGAR PRODUTO ===")
                    print(menu)
                    apagar(menu)
                    os.system('pause')
                case "3":
                    print("\n=== LISTANDO ===")
                    print(menu)
                    os.system('pause')
                case "4":
                    print("Saindo do programa.")
                    sys.exit()
                case _:
                    print("Opção invalida. Tente novamente.")
                    os.system('pause')
if __name__ == "__main__":
    main()
