#Rafael Henrique Carvalho da Silva
#11/11/2026
#Estudos de flasks

from flask import Flask
import biblio

app = Flask(__name__)

# Criação de rotas 
@app.route('/')
def hello() -> str:
    return 'Hello, World from Flask!'

@app.route('/procuravogais')
def procurar_vogais() -> str:
    frase =input("Digite uma frase: ")
    print("Frase:",frase)
    vogais_encontradas = biblio.procuravogais(frase)
    #Exibe as vogais no html no formato ", "
    return ', '.join(vogais_encontradas)

app.run(debug=True)