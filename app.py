from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        medicamento = request.form['medicamento']
        # Aquí deberías poner tu lógica de búsqueda real (con Selenium o BeautifulSoup)
        resultado = {
            'farmacia': 'Farmacia G',
            'precio': '$25.950',
            'link': 'https://www.ejemplo.com/medicamento'
        }
    return render_template('índice.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
