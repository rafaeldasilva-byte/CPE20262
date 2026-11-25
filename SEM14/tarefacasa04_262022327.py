#Rafael Henrique Carvalho da Silva
#10/11/2026
#Classificação de motores usando dados de sensores

import os
import openpyxl
arquivo = "dados_sensores.xlsx"

def carregar_dados(nome_aba:str) -> dict:
    dados = {}
    if (os.path.exists(arquivo)) and (nome_aba):
        try:
            #Carregando abas e planilha
            planilha = openpyxl.load_workbook(arquivo, data_only=True)
            aba  = planilha[nome_aba]         
            #Carregando dados das linhas
            for linha in aba.iter_rows(min_row=2,values_only=True):
                if linha and linha[0] is not None:
                    id = str(linha[0]).strip()
                    coluna_B = str(linha[1]).strip() 
                    coluna_C = str(linha[2]).strip() 
                    coluna_D = str(linha[3]).strip()
                    dados[id] = [coluna_B, coluna_C, coluna_D]
            #Retornando dados
            return dados
        except Exception as e:
            print(f"Erro ao carregar o arquivo Excel: {e}")
    else:
        print("Parâmetros Inválidos!!")

#Função da distância euclidiana
def distancia2(temp_ref:float,  vib_ref:float, temp_leitura:float, vib_leitura:float) -> float:
        dt = (temp_leitura - temp_ref)/20 
        dv = (vib_leitura - vib_ref)/2
        distancia2 = dt**2 + dv**2
        return distancia2

#Função para adicionar 

def vizinhos(dados_referencia:dict, dados_leitura:dict) -> dict:
    vizinhos_proximo = {}
    for id_leitura, [temp_leitura,vib_leitura,classe_motor] in dados_leitura.items():
        #Diferencas é zerada para evitar processamento
        diferencas = {}
        for id_ref, [temp_ref,vib_ref,classe_ref] in dados_referencia.items():
            diferencas[id_ref] = [distancia2(float(temp_ref), float(vib_ref), float(temp_leitura), float(vib_leitura)),classe_ref]
        #Buscando a menor diferença
        menor = ["id",100000]
        for id_diferencas, [valor,classe_ref] in diferencas.items():
            if valor < menor[1]:
                menor = [id_diferencas,valor,classe_ref]
        #Dicionário com as menores diferenças de cada id_leitura, sendo neste formato: {"id_leitura":["id_referencia_mais_proximo","diferença","classe_referencia"]}
        vizinhos_proximo[id_leitura] = menor
    return vizinhos_proximo

#Função que transforma dados de uma lista, com 3 itens, dentro de dicionário em uma única lista
def dados_em_listas(posicao_dado:int, dicionario:dict) -> list:
    lista =[]
    for id, dados in dicionario.items():
        lista.append(dados[posicao_dado])
    return lista

#Função que verifica se há dados faltantes no dicionario e retorna uma lista de chaves com None
def verificacao(dicionario:dict) -> dict:
    chaves_erradas = []
    for i in dicionario:
        if (dicionario[i][0] == "None") or (dicionario[i][1] == "None") or (dicionario[i][2] == "None"):
            chaves_erradas.append(i)
    return chaves_erradas

#def salvar_dados():
    
def main():
    #Criação dos dicionários
    treino_dados = carregar_dados("treino")
    teste_dados = carregar_dados("teste")
    novos_dados = carregar_dados("novas_leituras")

    #Mudança da ordem dos dados para que as temperaturas fiquem na posição 0 de cada chave
    for id,[b,c,d] in novos_dados.items():
        novos_dados[id] = [c,d,b]

    #Calculando a acurácia do programa utilizando os dados de treino como base em relação aos dados de teste
    vizinhos_treino_teste = vizinhos(treino_dados,teste_dados)

    #Transformando as classes em listas
    classes_treino_vizinhos = dados_em_listas(2,vizinhos_treino_teste)
    classes_teste = dados_em_listas(2,teste_dados)

    #Calculando a precisão
    igual = 0
    n_igual = 0
    for i in range (len(classes_treino_vizinhos)):
        if classes_treino_vizinhos[i] == classes_teste[i]:
            igual=igual+1
        else:
            n_igual=n_igual+1
    precisao = round((igual/(igual+n_igual)*100),2)
    print(f"Precisão: {precisao}%")

    #Verificando se não há falta de dados antes de classificar
    for i in range (len(verificacao(novos_dados))):
        del novos_dados[(verificacao(novos_dados))[i]]


    #Calculando e classificando novas leituras
    classes_previstas = {}
    ordem_classes=0
    for id_leitura, [temperatura_c,vibracao_mm_s,id_motor] in novos_dados.items():
        classes_previstas[id_leitura] = dados_em_listas(2,vizinhos(treino_dados,novos_dados))[ordem_classes]
        ordem_classes=ordem_classes+1
    print (classes_previstas)

if __name__ == "__main__":
    main()
