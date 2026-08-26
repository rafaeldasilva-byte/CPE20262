# Programa que mostra a diferença de 2 números
# Rafael H - 26/08/26
n1 = float(input ("Digite o primeiro número a ser subtraído: "))
n2 = float(input ("Digite o segundo número a ser subtraído: "))

if n1 > n2:
    result = n1 - n2
else:
    result = n2 - n1
if type(n1 and n2) == float:
    print (f"A subtração de {n1} com {n2} é igual a {result}" )
else:
    print("Retorne apenas números")
