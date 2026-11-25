#Rafael Henrique Carvalho da Silva
#25/11/2026
#Testando GET com flask

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

notas = [
    {"matricula":"1001", "disciplina":"MAT101", "nota":8.0},
    {"matricula":"1001", "disciplina":"FIS101", "nota":7.5},
    {"matricula":"1002", "disciplina":"MAT101", "nota":9.0},
    {"matricula":"1002", "disciplina":"FIS101", "nota":6.5}
    ]

@app.route("/notas", methods=["GET"])
def procurar_nota():
    matricula = request.args.get("matricula","").strip().upper()
    disciplina = request.args.get("disciplina", "").strip().upper()

    mensagem = ""
    resultado = []

    if matricula or disciplina:
        for cadastro in notas:
            if (cadastro["matricula"] == matricula) and (cadastro["disciplina"] == disciplina):
                resultado.append(cadastro)
                break

    if len(resultado) == 0:
        mensagem = "Nota não encontrada"

    return render_template("notas.html", resultado=resultado, notas=notas, matricula=matricula, disciplina=disciplina, mensagem=mensagem)


app.run(debug=True,port=9002)
