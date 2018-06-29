from flask import Flask
from flask import render_template
from flask import request
from Persona import *
from Sistema import *
from Vuelo import *
from Avion import *
import json
from datetime import *
from Funciones import *


s = Sistema()
d = {}

d = traerArchivo("datos.json")

listaAviones = generarListaAviones(d)
listaPersonas = generarListaPersonas(d, listaAviones)
listaVuelos = generarListaVuelos(d, listaPersonas, listaAviones)
s.cargar(listaPersonas, listaVuelos, listaAviones)



app = Flask(__name__, static_url_path='/static')


@app.route('/')
def Index():
    return 'Hola'

@app.route('/tablaVuelos')
def TablaVuelos():
    return render_template("/tablaVuelos.html", ListaVuelos=listaVuelos)

@app.route('/invalidosTripulacion')
def InvalidosTripulacion():
    return render_template("/invalidosTripulacion.html", ListaVuelos=listaVuelos)

@app.route('/noAutorizados')
def NoAutorizados():
    return render_template("/noAutorizados.html", ListaVuelos=listaVuelos)

@app.route('/unDiaUnVuelo')
def UnDiaUnVuelo():
    return render_template("/unDiaUnVuelo.html", Sistema=s)

@app.route('/idiomasPorVuelo')
def IdiomasPorVuelo():
    return render_template("/idiomaPorVuelo.html", ListaVuelos=listaVuelos)

if __name__ == '__main__':  # para actualizar automaticamente la pagina sin tener que cerrarla
    app.run(debug=True)     # para correr la pagina se puede hacer en este caso "python3 PruebaFlask.py" en la terminal