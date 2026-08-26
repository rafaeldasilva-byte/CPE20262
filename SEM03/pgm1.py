# Programa que soletra uma palavra digitada pelo usuário
# Rafael H - 26/08/26
palavra = input ("Digite uma palvra a ser soletrada: ")
print 
for i in palavra:
    print (i)

# Programa que soletra palavras de 5 letras sem loops
palavra1 = input("Digite uma palavra de 5 letras: ")
if len(palavra1) == 5:
    print (palavra1[0])
    print (palavra1[1])
    print (palavra1[2])
    print (palavra1[3])
    print (palavra1[4])
else:
    print ("A palavra digitada não tem 5 letras.")
