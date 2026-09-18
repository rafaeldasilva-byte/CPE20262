# Programa que imprime um triangulo baseado na altura 
# Rafael H - 18/09/2026

altura = int(input("Digite a altura da sua arvore: "))
for i in range (1,altura+1):
    print (" "*(altura-i)+"🌲"*(i))
