# Rafael Henrique Carvalho da Silva, João Lucas Barros Barroso, Nicoly Mariano Muniz de Souza, João Gabriel Correia
# 28/10/2026

#Análise de espécies de fauna ameaçada 2026

import pandas as pd 

df = pd.read_excel("Fauna Ameaçada 2026.xlsx")
colunas_notas = ['nomeci', 'nomeco', 'grupo', 'categoria','data','endemico','biomas','estados']
dicionario = df.set_index('nomeci').to_dict(orient='index')

print("\n=== ANÁLISE DE ESPÉCIES AMEAÇADAS ===")
print("")

vu = 0
re = 0
ew = 0
ex = 0
en = 0
crpe = 0
cr = 0
for nomeci, info in dicionario.items():
    #print(f"Nome científico: {nomeci}")
    #print(f"Categoria: {info['categoria']}")
    #print("")
    if info['categoria'] == 'Vulnerável (VU)':
        vu = vu+1
    if info['categoria'] == 'Regionalmente Extinta (RE)':
        re = re+1
    if info['categoria'] == 'Extinta na Natureza (EW)':
        ew = ew +1
    if info['categoria'] == 'Extinta (EX)':
        ex = ex+1
    if info['categoria'] == 'Em Perigo (EN)':
        en=en+1
    if info['categoria'] == 'Criticamente em Perigo (CR) (PE)':
        crpe=crpe+1
    if info['categoria'] == 'Criticamente em Perigo (CR)':
        cr=cr+1

todo = vu+re+ew+ex+en+crpe+cr

print(f"Espécies Vulneráveis: {vu}/{todo} - {round(vu/todo*100,2)}%")
print(f"Espécies Regionalmente Extinta:{re}/{todo} - {round(re/todo*100,2)}%")
print(f"Espécies Extinta na Natureza: {ew}/{todo} - {round(ew/todo*100,2)}%")
print(f"Espécies Extinta: {ex}/{todo} -  {round(ex/todo*100,2)}%")
print(f"Espécies Em Perigo:{en}/{todo} - {round(en/todo*100,2)}%")
print(f"Espécies Criticamente em Perigo (CR) (PE):{crpe}/{todo} - {round(crpe/todo*100,2)}%")
print(f"Espécies Criticamente em Perigo (CR):{cr}/{todo} - {round(cr/todo*100,2)}%")

ac = 0
al = 0
ap = 0
am = 0
ba = 0
ce = 0
df = 0
es = 0
go = 0
ma = 0
mt = 0
ms = 0
mg = 0
pa = 0
pb = 0
pr = 0
pe = 0
pi = 0
rj = 0
rn = 0
rs = 0
ro = 0
rr = 0
sc = 0
sp = 0
se = 0
to = 0

for nomeci, info in dicionario.items():
    if "Acre" in info['estados']:
        ac = ac + 1

    if "Alagoas" in info['estados']:
        al = al + 1

    if "Amapá" in info['estados']:
        ap = ap + 1

    if "Amazonas" in info['estados']:
        am = am + 1

    if "Bahia" in info['estados']:
        ba = ba + 1

    if "Ceará" in info['estados']:
        ce = ce + 1

    if "Distrito Federal" in info['estados']:
        df = df + 1

    if "Espírito Santo" in info['estados']:
        es = es + 1

    if "Goiás" in info['estados']:
        go = go + 1

    if "Maranhão" in info['estados']:
        ma = ma + 1

    if "Mato Grosso" in info['estados']:
        mt = mt + 1

    if "Mato Grosso do Sul" in info['estados']:
        ms = ms + 1

    if "Minas Gerais" in info['estados']:
        mg = mg + 1

    if "Pará" in info['estados']:
        pa = pa + 1

    if "Paraíba" in info['estados']:
        pb = pb + 1

    if "Paraná" in info['estados']:
        pr = pr + 1

    if "Pernambuco" in info['estados']:
        pe = pe + 1

    if "Piauí" in info['estados']:
        pi = pi + 1

    if "Rio de Janeiro" in info['estados']:
        rj = rj + 1

    if "Rio Grande do Norte" in info['estados']:
        rn = rn + 1

    if "Rio Grande do Sul" in info['estados']:
        rs = rs + 1

    if "Rondônia" in info['estados']:
        ro = ro + 1

    if "Roraima" in info['estados']:
        rr = rr + 1

    if "Santa Catarina" in info['estados']:
        sc = sc + 1

    if "São Paulo" in info['estados']:
        sp = sp + 1

    if "Sergipe" in info['estados']:
        se = se + 1

    if "Tocantins" in info['estados']:
        to = to + 1

# 1. Agrupa todas as suas variáveis em um dicionário
contagens = {
    'Acre': ac, 'Alagoas': al, 'Amapá': ap, 'Amazonas': am, 'Bahia': ba, 
    'Ceará': ce, 'Distrito Federal': df, 'Espírito Santo': es, 'Goiás': go, 
    'Maranhão': ma, 'Mato Grosso': mt, 'Mato Grosso do Sul': ms, 'Minas Gerais': mg, 
    'Pará': pa, 'Paraíba': pb, 'Paraná': pr, 'Pernambuco': pe, 'Piauí': pi, 
    'Rio de Janeiro': rj, 'Rio Grande do Norte': rn, 'Rio Grande do Sul': rs, 
    'Rondônia': ro, 'Roraima': rr, 'Santa Catarina': sc, 'São Paulo': sp, 
    'Sergipe': se, 'Tocantins': to
}

# 2. Descobre qual é a chave (estado) que tem o maior valor
maior_estado = max(contagens, key=contagens.get)
maior_valor = contagens[maior_estado]

print(f"\nO estado com mais ocorrências é: {maior_estado} (com {maior_valor} espécies).")

print(f"\n=== ESPÉCIES POSSIVELMENTE EXTINTAS E SUAS REGIÕES (total = {crpe}) ===\n")

print("=> Nomes comuns conhecidos:\n")
n = 1
for nomeci, info in dicionario.items():
    if info['categoria'] == "Criticamente em Perigo (CR) (PE)":
        # Verifica se 'nomeco' não é nulo/vazio antes de printar
        if pd.notna(info['nomeco']):
            print(f"{n} - {info['nomeco']} --> {info['biomas']}")
            n = n+1
