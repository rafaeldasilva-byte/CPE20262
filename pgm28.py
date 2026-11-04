#Estudos de funções
#Rafael Henrique Carvalho da Silva
#04/11/2026

def hipotenusa(cateto_1: str, cateto_2: str)->str:
    soma = cateto_1 ** 2 + cateto_2 ** 2
    a = soma ** 0.5
    return (a)
#print (type(hipotenusa(3.7,4)))

def media_positivos(valores):
    soma = 0
    quantidade = 0

    for valor in valores:
        if valor > 0:
            soma += valor
            quantidade += 1

    if quantidade == 0:
        return 0
    return soma / quantidade

valores = []

while True:
    v = input("Digite um valor, ou qualquer letra para parar: ")
    if (v.isdigit()):
        valores.append(int(v))
    else:
        break

print (f"Cálculo da média aproximada: {round(media_positivos(valores),2)}")