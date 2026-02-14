from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        tipo = request.form.get("tipo")
        quartos = int(request.form.get("quartos"))
        parcelas = int(request.form.get("parcelas"))

        # Lógica conforme o desafio [cite: 17, 18, 19, 24, 25]
        valor_base = {"Apartamento": 700, "Casa": 900, "Estúdio": 1200}
        aluguel = valor_base[tipo]
        
        if tipo == "Apartamento" and quartos == 2: aluguel += 200
        elif tipo == "Casa" and quartos == 2: aluguel += 250
        
        valor_parcela = 2000 / parcelas
        
        resultado = {
            "aluguel": f"{aluguel:.2f}",
            "parcelas": parcelas,
            "valor_parcela": f"{valor_parcela:.2f}",
            "total": f"{(aluguel + valor_parcela):.2f}"
        }
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)