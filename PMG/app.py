#Rafael Henrique Carvalho da Silva
#25/11/2026
#Password Manager and Generator

#IIMPORTAÇÃO DE BIBLIOTECAS
import os
import json
#Transformar textos em hashs
from argon2 import PasswordHasher
#Verficar hashs
from argon2.exceptions import VerifyMismatchError



#RECEPÇÃO DE USUÁRIOS
print(
    '''====== Password Manager and Generator ======='''
)

#VERIFICAÇÃO DE PRIMEIRO ACESSO
#Variáveis a utilizar
ph = PasswordHasher()

#Transformar texto em hash
def texto_hash(texto:str) -> str:
    texto_hash = ph.hash(texto)
    return texto_hash

#Comparar hashs (pois os hashs são diferentes, ele comparará o M (quantidade de memória), T (quantas vezes passará) e P (divisão de threads) e seus Salts dos hashs)
def comparar_hash(hash_correto:str,texto_novo:str) ->bool:
    try:
        ph.verify(hash_correto,texto_novo)
        return True
    except VerifyMismatchError:
        return False



def verificacao_sm():
    nome_arquivo = "auth.json"
    if not os.path.exists(nome_arquivo):
        dados_iniciais = {

        }
        with open(nome_arquivo,"w", encoding="utf-8") as json:
            json.dump(dados_iniciais, json, indent=4, ensure_ascii=False)


