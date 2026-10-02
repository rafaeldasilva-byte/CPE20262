#Programa para aprender lista
#Rafael Henrique - 02/10/2026
lista = []

for i in range(4):
    equipamento = input("Insira o equipamento: ").lower()
    lista.append(equipamento)
urgente = input("Equipamento urgente: ").lower()
lista.insert(0,urgente)

cancelar = input("\nCancelar: ")
if cancelar in lista:
    lista.remove(cancelar)
else:
    print("Equipamento não encontrado.")
    
urgente = lista.pop(0)
print(f"\nEquipamento em teste: {urgente}")
print(f"Restante da lista: {lista}")
