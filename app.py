from flask import Flask, render_template
import os
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG_TB_ENABLED'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

toolbar = DebugToolbarExtension(app)


# Define una ruta para la página principal ('/')
@app.route('/')
def index():
    return render_template('index.html')

# Define una ruta para la página de contacto ('/contacto')
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

# Define una ruta para la página de contacto ('/contacto')
@app.route('/sobremi')
def sobremi():
    return render_template('sobremi.html')

# Define una ruta para la página de contacto ('/contacto')
@app.route('/descarga')
def descarga():
    return render_template('descarga.html')


# Verifica si este script se está ejecutando directamente como programa principal
if __name__ == '__main__':
    # Inicia el servidor de desarrollo de Flask
    app.run(debug=True)
