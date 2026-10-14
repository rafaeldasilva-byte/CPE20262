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

for i in range(len(capitais)):
    lat = coordenadas[i][0] 
    lon = coordenadas[i][1] 
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true"
    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")

    #print(texto)
    #os.system("pause")
    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")
    parte1 = texto.split('"windspeed":"km/h"')[1]
    parte2 = texto.split('"winddirection":"°"')[1]
    parte1 = parte1.split('"windspeed":')[1]
    parte2 = parte2.split('"winddirection":')[1]
    valor_winddirection = parte2.split(',')[0]
    valor_windspeed = parte1.split(',')[0]
    windspeed.append(float(valor_windspeed))
    winddirection.append(float(valor_winddirection))
    #print(valor_windspeed)
    #print(valor_winddirection)

if winddirection/45:
    #Analisar o 

    

print ("--- VELOCIDADE DOS VENTOS E SUAS DIREÇÕES ---\n")
for i in range(len(capitais)):
    print(capitais[i], ":", windspeed[i], "km/h", "-", winddirection[i])

speed_max = max(windspeed)
posicao_max = windspeed.index(speed_max)

print("\n--- ANÁLISE DOS DADOS ---")
print("Mais vento:", capitais[posicao_max], "com", speed_max, "km/h")
