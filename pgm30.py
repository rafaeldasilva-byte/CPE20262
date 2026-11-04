#Solução para pgm29

def incluir(menu):
    id = input("Insira o ID para incluir: ")
    quantidade = int(input("Insira a quantidade: "))
    preço = float(input("Insira o preço (utilize \".\" para casas decimais): R$"))
    if not (id in menu):
        return (menu[id]=[quantidade,preço])
    else:
        print("Este ID já existe.")

def apagar(menu):
    id = input("Insira o ID para apagar: ")
    if id in menu:
        del menu[id]
    else: 
        print("ID não encontrado.")

def listar(menu):
    print (menu)
