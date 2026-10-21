#Rafael Henrique Carvalho da Silva
#21/10/2026
#O círculo dos cavaleiros lendários
from sys import exit

print("--- SIMULADOR DO CÍRCULO DOS CAVALEIROS ---")
n= int(input("Digite o número de cavaleiros: "))

#Criação do círculo
cavaleiros=[]
for i in range(n):
    cavaleiros.append(i+1)

print("\n--- SIMULAÇÃO ---")

#Posição da espada
espada =0

#Simulação mata ou morre
while not len(cavaleiros) == 1:
    if espada == len(cavaleiros)-1:
        print(f"Cavaleiro {cavaleiros[espada]} matou o cavaleiro {cavaleiros[0]}",end=" ")
        cavaleiros.pop(0)
        espada=0
        print(f"e passou a espada para o cavaleiro {cavaleiros[espada]}.")
    elif espada == len(cavaleiros)-2:
        print(f"Cavaleiro {cavaleiros[espada]} matou o cavaleiro {cavaleiros[espada+1]}",end=" ")
        cavaleiros.pop(espada+1)
        espada=0
        print(f"e passou a espada para o cavaleiro {cavaleiros[espada]}.")
    else:
        print(f"Cavaleiro {cavaleiros[espada]} matou o cavaleiro {cavaleiros[espada+1]}",end=" ")
        cavaleiros.pop(espada+1)
        espada=espada+1
        print(f"e passou a espada para o cavaleiro {cavaleiros[espada]}.")
print(f"\nSobrevivente: Cavaleiro n° {"".join(map(str,cavaleiros))}")
        


