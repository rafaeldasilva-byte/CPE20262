# Programa classificação médica multivariada com sigmóide
# Rafael H. C. da Silva (262022327)- 07/09/2026

#importação de bibliotecas
import math 
import sys

#Declaração de variáveis
w1 = 0.01 #glicose
w2 = 0.01 #idade
b = -0.5 #viés
n = 0.01 #taxa de aprendizado
amostra = 1

#Apresentação da Fase 1
print("=== FASE 1: TREINAMENTO (GLICOSE + IDADE) ===\n")

#Solicitação de dados para calibragem do programa
for _ in range (0,10):

    print(f"\n--- AMOSTRA {amostra}/10 ---")

    # variável x1 (Glicose) entre 70 e 180
    x1 = input("Insira um valor para a glicose: ") #Glicose
    while not x1.isdigit():
        x1 = input("Insira apenas números: ")
    x1 = float(x1)
    while (x1<70) or (x1>180):
        x1 = input("Insira um valor entre 70 e 180: ")
        while not x1.isdigit():
            x1 = input("Insira apenas números: ")
        x1 = float(x1)

    # variável x2 (Idade) 
    x2 = input("Insira um valor para a idade: ") #Idade
    while not x2.isdigit():
        x2 = input("Insira apenas números: ")
    x2 = float(x2)

    # variável y (Diagnóstico real) para 0 ou 1
    y = input("Insira o diagnóstico real (1.0 ou 0.0): ") #Diagnóstico real
    while not y.isdigit():
        y = input("Insira apenas números: ")
    y=float(y)
    while (y!=1) and (y!=0):
        y = input("Insira 0 ou 1: ")
        while not y.isdigit():
            y = input("Insira apenas números: ")
        y = float(y)

    #Cálculo da soma ponderada (z)
    z = (w1*x1)+(w2*x2)+b

    #Cálculo da probabilidade (y1)
    y1 = 1/(1+math.exp(-z))

    #Determinando a classe prevista (classe)
    if y1 >= 0.5:
        classe = 1.0
    else:
        classe = 0.0

    #Cálculo do erro (erro)
    erro = y-y1

    #Atualizando parâmetros
    w1 = w1+(n * erro * x1)
    w2 = w2+(n * erro * x2)
    b = b+(n * erro)

    #Verificação de status
    if classe == y:
        status = "ACERTO"
    else:
        status = "ERRO"

    #Contagem da amostra

    amostra += 1 

    #Exibição dos resultados
    print (f"\nProbabilidade = {y1} ({y1*100}%) | Classe Prevista = {classe} | Diagnóstico Real = {y} | Status = {status}\nErro = {erro} | W1 = {w1} | W2 = {w2}| B = {b}")

# Final da fase 1
print(f"\n=======================================\nTreinamento Concluído! \U0001F60A\nPesos Calibrados -> W1 (Glicose): {w1} | W2 (Idade): {w2} | B: {b}\n=======================================")

# Fase 3 Diagnóstico do novo paciente (Inferência)
print("\n=== FASE 3: DIAGNÓSTICO DE NOVO PACIENTE (INFERÊNCIA) ===")

#Declarando variáveis do novo paciente

 #Glicose do novo paciente (x1_novo)
x1_novo = input("Insira o valor da glicose do novo paciente: ")
while not x1_novo.isdigit():
    x1_novo = input("Insira apenas números: ")
x1_novo = float(x1_novo)

 #Glicose do novo paciente (x2_novo)
x2_novo = input("Insira o valor da idade do novo paciente: ") 
while not x2_novo.isdigit():
    x2_novo = input("Insira apenas números: ")
x2_novo = float(x2_novo)

#Cálculo da nova combinação linear (z_novo)
z_novo = (w1 * x1_novo) + (w2 * x2_novo) + b

#Cálculo da nova probabilidade (y1_novo)
y1_novo = 1 / (1 +math.exp(-z_novo))

#Status do diagnóstico
if y1_novo >= 0.5:
    diagnostico = "Alto Risco (Encaminhar para exames detalhados)"
else:
    diagnostico = "Baixo Risco (Sem preocupaçõees alarmantes)"

print(f"\nProbabilidade Estimada: {y1_novo} ({y1_novo*100}%)\n[DIAGNÓSTICO]: {diagnostico}")