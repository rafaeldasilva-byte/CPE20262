# Análise de Similaridade Vetorial de Palavras via Distância de Cosseno em 3D
# Rafael Henrique Carvalho da Silva (262022327) - 23/09/2026

#Inicialização do programa
from math import sqrt
print("=== FASE 1: PROCESSAMENTO DE SIMILARIDADE VETORIAL 3D ===")

#x1 (Quantidade de vogais)
vogais = "aeiou"
#x2 (Quantidade de consoantes)
consoantes = "bcdfghjklmnpqrstvwxyz"
#x3 (Distribuição Alfabética - Quantidade de letras pertencentes à primeira metade do alfabeto (caracteres de 'a' até 'm')
alfameio = "abcdefghijklm"

# Parâmetros e variáveis da palavra de referência
palavraA = input("Insira uma palavra de referência: ")
a1 = 0
a2 = 0 
a3 = 0

# Quantidade de vogais na palavra de referência
for letra in palavraA:
    for v in vogais:
        if letra == v:
            a1 += 1

# Quantidade de consoantes na palavra de referência
for letra in palavraA:
    for c in consoantes:
        if letra == c:
            a2 += 1

# Distribuição alfabética da palavra de referência
for letra in palavraA:
    for am in alfameio:
        if letra == am:
            a3 += 1

#Norma Vetorial da referência
normaA = sqrt((a1**2) + (a2**2) + (a3**2))

# Vetores da referência
print(f"[Vetor Referencia '{palavraA}']: Vogais: {a1} | Consoantes: {a2} | Letras A-M: {a3} | Norma 3D: {round(normaA,4)}\n")

#Variável para cálculo da média das distâncias
cossenoTotal = 0

# Palavras a serem analizadas

for i in range (10):
    print(f"Palavra {i+1}/10")
    palavraB = input("Digite a palavra: ")

    # Parâmetros e variáveis da palavra de referência
    b1 = 0
    b2 = 0
    b3 = 0

    # Vetorização da palavraB
    #B1
    for letra in palavraB:
        for v in vogais:
            if letra == v:
                b1 += 1
    #B2
    for letra in palavraB:
        for c in consoantes:
            if letra == c:
                b2 += 1
    #B3
    for letra in palavraB:
        for am in alfameio:
            if letra == am:
                b3 += 1

    
    #Norma Vetorial da palavra
    normaB = sqrt((b1**2) + (b2**2) + (b3**2))

    #Calculo dos parâmetros2. Produto Escalar (Dot Product 3D):
    produto_escalar = (a1 * b1) + (a2 * b2) + (a3 * b3)

    if (normaA * normaB) > 0:
        similaridade = produto_escalar / (normaA * normaB)
    else:
        similaridade = 0.0

    distancia = 1.0 - similaridade

    #Similaridade das palavras
    if similaridade >= 0.95:
        classificacao = "Alta Similaridade"
    elif similaridade >= 0.80:
        classificacao = "Média Similaridade"
    else: 
        classificacao = "Baixa Similaridade"

    #Exibição das características da palavraB

    print(f"Vetor 3D: ({b1}, {b2}, {b3}) | Similaridade: {round(similaridade,4)} ({round((similaridade*100),2)}%) | Distancia: {round(distancia,4)}\nClassificação: {classificacao}\n")

    #Soma das distãncias
    cossenoTotal += similaridade

#FASE 2 
print(f"=== FASE 2: RELATÓRIO DO PROCESSAMENTO ===\nProcessamento Concluido com Sucesso!\nReferência '{palavraA}' -> Vetor 3D: ({a1}, {a2}, {a3})")
print(f"Média de similaridade global: {round((cossenoTotal/10),4)} ({round((cossenoTotal*10),2)}%)\n")

#FASE 3
print("=== FASE 3: DIAGNÓSTICO DE NOVA PALAVRA (INFERÊNCIA 3D) ===")



#Loop nas novas palavras
while True:
    palavraC = input("Digite a nova palavra para teste (PARAR para sair): ")

    if palavraC=="PARAR":
        break

    #Variáveis da nova palavra
    #C1
    c1 = 0
    for letra in palavraC:
        for v in vogais:
            if letra == v:
                c1 += 1
    #C2
    c2 = 0
    for letra in palavraC:
        for c in consoantes:
            if letra == c:
                c2 += 1
    #C3
    c3 = 0
    for letra in palavraC:
        for am in alfameio:
            if letra == am:
                c3 += 1
    print(f"Vetor Novo 3D: [{c1}, {c2}, {c3}]")

    #Norma Vetorial da palavra
    normaC = sqrt((c1**2) + (c2**2) + (c3**2))

    #Distância e similaridade com a palavra de referência

    produto_escalar = (a1 * c1) + (a2 * c2) + (a3 * c3)

    if (normaA * normaC) > 0:
        similaridade = produto_escalar / (normaA * normaC)
    else:
        similaridade = 0.0

    distancia = 1.0 - similaridade

    print(f"Similaridade Estimada: {round(similaridade,4)} ({round((similaridade*100),2)}%) | Distancia: {round(distancia,4)}")

    #Similaridade das palavras
    if similaridade >= 0.95:
        classificacao = "Alta Similaridade"
    elif similaridade >= 0.80:
        classificacao = "Média Similaridade"
    else: 
        classificacao = "Baixa Similaridade"

    print(f"[DIAGNÓSTICO]: {classificacao}\n")