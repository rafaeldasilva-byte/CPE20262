# Programa em que o usuário digita 3 números inteiros e mostra os números em ordem crescente
# Rafael H - 26/08/26

n1 = int(input ("Digite o primeiro número: "))
n2 = int(input ("Digite o segundo número: "))
n3 = int(input ("Digite o terceiro número: "))

if n1>n2:
    if n1>n3:
        maior = n1
        if n2> n3:
            meio = n2
            menor = n3
        else:
            meio = n3
            menor = n2
else:
    if n1>n3:
        
    else:
        menor = n1
    
print(f"A ordem crescente dos números é: {maior}, {meio}, {menor}.")
