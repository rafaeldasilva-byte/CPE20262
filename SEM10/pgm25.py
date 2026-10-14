# Programa de cidades ideais para kaitsurf
# Rafael Henrique - 14/10/2026

import urllib.request
import os

capitais = [
    "São Paulo", "Rio de Janeiro", "Salvador", 
    "Fortaleza", "Recife", "Florianópolis", "Porto Alegre"
]

#Cria matriz de coordenadas (latitude, longitude) para cada capital
coordenadas = [
    [-23.96, -46.33], # Santos/SP
    [-22.91, -43.17], # Rio de Janeiro/RJ
    [-12.97, -38.51], # Salvador/BA
    [-3.71, -38.54], # Fortaleza/CE
    [-8.05, -34.88],  # Recife/PE
    [ -27.59, -48.54], # Florianópolis/SC
    [-30.03, -51.23],  # Porto Alegre/RS
]

windspeed = []
winddirection = []
pontos = ["Leste", "Nordeste","Norte","Noroeste","Oeste","Sudoeste","Sul","Sudeste"]

for i in range(len(capitais)):
    lat = coordenadas[i][0] 
    lon = coordenadas[i][1] 
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true"
    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")

    # Barra de carregamento
    print("[",end="")
    for j in range(i+1):
        print ("=",end="")
    print(">",end="")
    for k in range(len(capitais)-(i+1)):
        print("-",end="")
    print("] ",end="")
    print( (i+1)*(100//len(capitais)), "%",sep="")

    

    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")
    parte1 = texto.split('"windspeed":"km/h"')[1]
    parte2 = texto.split('"winddirection":"°"')[1]
    parte1 = parte1.split('"windspeed":')[1]
    parte2 = parte2.split('"winddirection":')[1]
    valor_winddirection = float(parte2.split(',')[0])
    valor_windspeed = float(parte1.split(',')[0])

    #Verificação da posição dentro da lista de pontos
    if (valor_winddirection/45) - (valor_winddirection//45)  >= 0.5:
        valor_winddirection = (valor_winddirection//45) + 1
    else:
        valor_winddirection = valor_winddirection//45

    windspeed.append(valor_windspeed)
    winddirection.append(int(valor_winddirection))
    #print(valor_windspeed)
    #print(valor_winddirection)
    os.system('cls' if os.name == 'nt' else 'clear')

print ("--- VELOCIDADE DOS VENTOS E SUAS DIREÇÕES ---\n")
for i in range(len(capitais)):
    print(capitais[i], ":", windspeed[i], "km/h", "-", pontos[winddirection[i]])

speed_max = max(windspeed)
posicao_max = windspeed.index(speed_max)

print("\n--- ANÁLISE DOS DADOS ---")
print("Mais vento:", capitais[posicao_max], "com", speed_max, "km/h")
