from flask import Flask, render_template

app = Flask(__name__, template_folder='files/html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/unidades')
def unidades():
    return render_template('unidades.html')

if __name__ == '__main__':
    app.run(debug=True)
