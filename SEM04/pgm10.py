# Testes com o while
# Rafael H - 04/09/2026
tentativa = 0
while True:
    senha = input("Insira a senha: ")
    if senha == "python":
        print("Parabéns, senha correta")
        break
    print ("Tente novamente")
    tentativa += 1
    if tentativa == 3:
        print("Número de tentativas excedida, ligando para a polícia.\U0001F60D")
        break
