# Programa que verifica se uma palavra é palindromo
# Rafael H - 28/08/2026

palavra = input("Digite a palavra a ser analisada: ").lower()

palavra = palavra.replace(" ","")
palindromo = palavra [::-1]
if palindromo == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
