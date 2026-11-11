#Rafael Henrique Carvalho da Silva
#11/11/2026
#Funções recursivas

n = input("Digite um valor: ")

def fatorial(n):
    if n < 0:
        raise ValueError("n negativo")
    if n <= 1:
        #Valor deterministico para parar a função
        return 1
    return n * fatorial (n-1)
#print(fatorial(int(n)))

#n=posição da sequência
def fibonacci(n):
    if n <= 1:
        return n
    print (f"Estou no fibonacci de {n}:{n-1},{n-2}")
    return fibonacci (n-1) + fibonacci(n-2)

print(fibonacci(int(n)))