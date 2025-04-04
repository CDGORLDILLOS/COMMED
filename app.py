from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        medicamento = request.form.get("medicamento")

        # Simulación de resultados (aquí iría tu lógica con Selenium)
        resultado = {
            "farmacia": "Farmacia A",
            "precio": "$25.950",
            "link": "https://www.farmaciaa.com/producto"
        }

        return render_template("índice.html", resultado=resultado)

    return render_template("índice.html", resultado=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
