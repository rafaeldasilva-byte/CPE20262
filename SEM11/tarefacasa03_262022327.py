#Rafael Henrique Carvalho da Silva (262022327)
#20/10/2026
#Classificação de mensagens com o algoritmo

#Declaração das listas
itens = ["links","pontos de exclamaçẽos","palavras suspeitas"]
entrada = []
distancias = []
menores = []
menoresnum = []
links = [0, 0, 1, 3, 2, 0, 4, 1, 3, 0]
exclamacoes = [0, 1, 0, 4, 3, 0, 5, 1, 4, 0]
suspeitas = [0, 0, 1, 4, 3, 0, 5, 1, 4, 0]

classes = [
"NORMAL", "NORMAL", "NORMAL", "SPAM", "SPAM",
"NORMAL", "SPAM", "NORMAL", "SPAM", "NORMAL"]

#Entrada de dados
print("CLASSIFICADOR DE MENSAGENS COM 1-NN")
for i in range(3):
    e = int(input(f"Quantidade de {itens[i]}: "))
    entrada.append(e)

#Distância de Manhattan
for i in range(10):
    d = abs(entrada[0] - links[i]) + abs(entrada[1] - exclamacoes[i]) + abs(entrada[2] - suspeitas[i])
    distancias.append(d)

#Encontrando os mínimos
menor = 1000
for i in distancias:
    if i < menor:
        menor = i 

for i in range(10):
    if distancias[i] == menor:
        menoresnum.append(i)
        menores.append(classes[i])

#Desempatando (Dùvida, é possível adicionar itens em uma soma? (classes[menores[0]]==classes[menores[1]]==classes[menores[2]]+))
n=0
s=0
for i in menores:
    if i == "NORMAL":
        n=n+1
    if i == "SPAM":
        s=s+1
if (n!=0 and s!=0):
    classe1="INDEFINIDO"
else:
    classe1=menores[0]

#Resposta
if len(menores)>1:
    print("\nForam encontrados exemplos empatados.")
print(f"\nClassificação: {classe1}\nMenor distância: {menor}\nExemplo(s) mais próximo(s): {" e ".join(map(str, menoresnum))}")
print(f"\nCaracterísticas do(s) exemplo(s):")
for i in menoresnum:
    print(f"{classes[i]}:\n   - Links:{links[i]}\n   - Exclamações:{exclamacoes[i]}\n   - Palavras suspeitas:{suspeitas[i]}")