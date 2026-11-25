# Claudia Jacy Barenco Abbas
# Modificado com Funções, Dicionário e Suporte a Excel

import os
import openpyxl

itens = {}
NOME_ARQUIVO = "dados_itens.xlsx"

def carregar_excel():
    if os.path.exists(NOME_ARQUIVO):
        try:
            planilha = openpyxl.load_workbook(NOME_ARQUIVO, data_only=True)
            folha  = planilha.active           
            for linha in folha.iter_rows(min_row=2, values_only=True):
                if linha and linha[0] is not None:
                    chave = str(linha[0]).strip()
                    descricao = str(linha[1]).strip() 
                    quantidade = str(linha[2]).strip() 
                    itens[chave] = (descricao, quantidade)
            print(f"Dados carregados com sucesso do arquivo '{NOME_ARQUIVO}'!")
            os.system('pause')
        except Exception as e:
            print(f"Erro ao carregar o arquivo Excel: {e}")

def gravar_excel():
    print("--- GRAVAR EM EXCEL ---")
    try:
        planilha = openpyxl.Workbook()
        folha = planilha.active
        folha.title = "Itens"       
        folha.append(["ID", "Descrição", "Quantidade"])       
        for chave, (descricao, quantidade) in itens.items():
            folha.append([chave, descricao, quantidade])
            
        planilha.save(NOME_ARQUIVO)
        print(f"Dados salvos com sucesso no arquivo '{NOME_ARQUIVO}'!")
    except Exception as e:
        print(f"Erro ao salvar no Excel: {e}")
    print("Pressione Enter para continuar...")
    os.system('pause')

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
    os.system('pause')

def modificar():
    print("--- MODIFICAR ITEM ---")
    chave = input("Digite o ID do item a ser modificado: ").strip()
    if chave not in itens:
        print("Erro: Chave não encontrada no sistema.")
    else:
        desc_atual, qtd_atual = itens[chave]
        print(f"Dados atuais -> Descrição: {desc_atual} | Quantidade: {qtd_atual}")
        print("Deixe em branco para manter o valor atual.")
        
        nova_desc = input("Digite a nova descrição: ").strip()
        nova_qtd = input("Digite a nova quantidade: ").strip()
        
        if nova_desc != "":
            desc_final = nova_desc
        else: 
            desc_final = desc_atual
        
        if nova_qtd != "":
           qtd_final = nova_qtd
        else:
            qtd_final = qtd_atual
        
        itens[chave] = (desc_final, qtd_final)
        print(f"Item '{chave}' modificado com sucesso!")
    print("Pressione Enter para continuar...")
    os.system('pause')

def apagar():
    print("--- APAGAR ITEM ---")
    chave = input("Digite o ID do item a ser apagado: ").strip()
    if chave in itens:
        removido = itens.pop(chave)
        print(f"Item '{chave}' foi removido com sucesso!")
    else:
        print("Erro: Chave não encontrada no sistema.")
    print("Pressione Enter para continuar...")
    os.system('pause')

def listar():
    print("--- LISTAR ITENS ---")
    if not itens:
        print("Nenhum item cadastrado.")
    else:
        print(f"{'Item':<15} | {'Quantidade':<10} | {'Valor':<10}")
        print("-" * 35)
        for chave, valor in itens.items():
            print(f"{chave:<15} | {valor[1]:<10} | {valor[0]:<1}")
    print("Pressione Enter para continuar...")
    os.system('pause')

def sair():
    print("Saindo do programa... Até logo!")

def opcao_invalida():
    print("Opção inválida. Tente novamente.")
    print("Pressione Enter para continuar...")
    os.system('pause')

menu_opcoes = (
    incluir,
    modificar,
    apagar,
    listar,
    gravar_excel,
    sair
)

def main():
    carregar_excel()
    while True:
        os.system('cls')
        print("====================")
        print("        MENU        ")
        print("====================")
        print("1. Incluir")
        print("2. Modificar")
        print("3. Apagar")
        print("4. Listar")
        print("5. Gravar em Excel")
        print("6. Sair")
        print("====================")
        
        opcao = input("Digite a opcao desejada: ").strip()
        acao = menu_opcoes[int(opcao)-1]
        if opcao == "6":
            break
        acao()
        

if __name__ == "__main__":
    main()