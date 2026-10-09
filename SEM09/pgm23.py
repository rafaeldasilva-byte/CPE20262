# Programa de organização de itens
# Rafael da Silva - 08/10/2026

from sys import exit
import os
import time

itens = []
while True:
    
    print ("\n=== MENU DO SISTEMA ===")
    print ("""
    1 - Adicionar manutenção normal
    2 - Adicionar manutenção urgente
    3 - Cancelar uma manutenção
    4 - Concluir a próxima manutenção
    5 - Retirar uma máquina por posição
    6 - Mostrar a fila
    0 - Encerrar""")

    menu = int(input("\nSelecione uma opção: "))
    if menu:
        os.system("cls" if os.name == 'nt' else "clear")
    match menu:
        case 1:
            maquina = input("\nManutenção normal: ").lower()
            igual = False
            for i in itens:
                if maquina == i:
                    igual = True
            if igual:
                print("Não é possível cadastrar duas vezes a mesma máquina.")
            else:
                itens.append(maquina)
        case 2:
            maquina = input("\nManutenção urgente: ").lower()
            igual = False
            for i in itens:
                if maquina == i:
                    igual = True
            if igual:
                print("Não é possível cadastrar duas vezes a mesma máquina.")
            else:
                itens.insert(0, maquina)
        case 3:
            maquina = input("\nMáquina a ser cancelada: ").lower()
            if not maquina in itens:
                print("Máquina não encontrada.")
            else:
                itens.remove(maquina)
        case 4:
            if len(itens) == 0:
                "Não existe máquinas na fila"
            else:
                print(f"Manutenção de {itens[0]} concluída.")
                itens.pop(0)
        case 5:
            if len(itens) == 0:
                "Não existe máquinas na fila"
            else:
                position = int(input("Posição a ser retirada: "))
                if (position < 0) or (position >= len(itens)):
                    print("Posição inválida.")
                else:
                    print(f"Máquina {itens[position]} retirada.")
                    itens.pop(position)
        case 6:
            print("Fila de manutenção: ")
            print (itens)
        case 0: 
            exit()
        case _:
            print("Digite uma opção válida.")
os.system("pause")
    


