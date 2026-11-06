# Rafael Henrique Carvalho da Silva
#06/11/2026

import os
import openpyxl

arquivo = "Estoque.xlsx"
itens = {}

def incluir():
    print("--- INCLUIR ITEM ---")
    chave = input("Digite o ID do item: ").strip()
    if chave in itens:
        print("Erro: Já existe um item registrado com esta chave.")
    else:
        valor = input("Digite a descrição do item: ").strip()
        quantidade = input("Digite a quantidade do item: ").strip()
        itens[chave] = (valor, quantidade)
        print(f"Item '{chave}' incluído com sucesso!")
    print("Pressione Enter para continuar...")

def apagar():
    print("--- APAGAR ITEM ---")
    chave = input("Digite o ID do item a ser apagado: ").strip()
    if chave in itens:
        removido = itens.pop(chave)
        print(f"Item '{chave}' foi removido com sucesso!")
    else:
        print("Erro: Chave não encontrada no sistema.")
    print("Pressione Enter para continuar...")

def listar():
    print("--- LISTAR ITENS ---")
    if not itens:
        print("Nenhum item cadastrado.")
    else:
        print(f"{'Item':^15} | {'Quantidade':^10} | {'Valor':^10}")
        print("-" * 40)
        for chave, valor in itens.items():
            print(f"{chave:^15} | {valor[1]:^10} | {valor[0]:^10}")
    print("Pressione Enter para continuar...")

def alterar():
    print("--- ALTERAR ITENS ---")
    listar()
    chave = input("Digite o ID para alterar, \"\" para não alterar nada: ").strip()
    if chave in itens:
        valor = input("Digite a nova descrição: ").strip()
        quantidade = input("Digite a nova quantidade: ").strip()
        itens[chave] = (valor,quantidade)
    elif chave == "":
        return
    else:
        print("Erro: Chave não encontrada no sistema.")
def carregar_excel():
    if os.path.exists(arquivo):
        planilha = openpyxl.load_workbook(arquivo,data_only=True)
        aba = planilha.active
        for linha in aba.iter_rows(min_row=2, values_only = True):
            if linha and linha[0] is not None:
                chave = str(linha[0]).strip()
                valor =
                quantidade =
            itens[chave] = (valor,quantidade)

def gravar_no_excel():
    planilha = openpyxl.Workbook(arquivo)
    



def sair():
    print("Saindo do programa... Até logo!")

def opcao_invalida():
    print("Opção inválida. Tente novamente.")
    os.system('pause' if os.name == 'nt' else 'read -p "Pressione Enter para continuar..."')

menu_opcoes = {
    "1": incluir,
    "2": apagar,
    "3": listar,
    "4": alterar,
    "5": gravar_no_excel,
    "6": sair,
}

def main():
    while True:
        os.system('cls')
        print("====================")
        print("        MENU        ")
        print("====================")
        print("1. Incluir")
        print("2. Apagar")
        print("3. Listar")
        print("4. Alterar")
        print("5. Gravar no excel")
        print("6. Sair")
        print("====================")
        
        opcao = input("Digite a opcao desejada: ").strip()
        acao = menu_opcoes.get(opcao, opcao_invalida)
        
        # Executa a função correspondente
        acao()
        os.system('pause')
        
        if opcao == "6":
            break

if __name__ == "__main__":
    main()
