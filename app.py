#Se importa la biblioteca de Flask
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

#Ruta de página principal index
@app.route('/')
def index():
    return render_template('index.html')

#Ruta de página 1
@app.route('/pag1')
def entretenimiento():
    return render_template('/pag1.html')

#Ruta de página 2
@app.route('/pag2')
def salud():
    return render_template('/pag2.html')

#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)