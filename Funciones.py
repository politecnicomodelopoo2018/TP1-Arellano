import json
from Avion import *
from Persona import *
from Vuelo import *

def traerArchivo(archivo):
    with open(archivo, "r") as f:
        dict = json.loads(f.read())
    return dict

def generarListaAviones(dict):
    listaAviones = []

    listaDiccionarios = dict["Aviones"]
    for item in listaDiccionarios:
        avion = Avion()
        avion.descerializar(item)
        listaAviones.append(avion)
    return listaAviones

def generarListaPersonas(dict, listaAviones):
    listaPersonas = []

    listaDiccionarios = dict["Personas"]
    for item in listaDiccionarios:
        persona = eval(item["tipo"])()
        persona.descerializar(item, listaAviones)
        listaPersonas.append(persona)
    return listaPersonas

def generarListaVuelos(dict, listaPersonas, listaAviones):
    listaVuelos = []

    listaDiccionarios = dict["Vuelos"]
    for item in listaDiccionarios:
        vuelo = Vuelo()
        vuelo.descerializar(item, listaPersonas, listaAviones)
        listaVuelos.append(vuelo)
    return listaVuelos