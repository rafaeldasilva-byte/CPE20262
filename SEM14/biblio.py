def procuravogais(frase:str) -> str:
    vogais = set("aeiouAEIOU")
    return vogais.intersection(set(frase))

def procuraletras(frase:str, letras:str) -> str:
    return set(letras).intersection(set(frase))
