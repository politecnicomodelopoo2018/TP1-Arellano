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

def printDatosAvion(avion):
    print(avion.modelo, "|", avion.limPasajeros, "|", avion.limTripulacion)

def printDatosPersona(persona, Pas = False, Pil = False, Ser = False):
    if type(persona) is Pasajero and Pas:
        print(persona.nombre, "|", persona.apellido, "|", persona.fechaNac, "|", persona.dni, "|", persona.vip, "|",
              persona.necesidadEspecial)
    elif type(persona) is Servicio and Ser:
        print(persona.nombre, "|", persona.apellido, "|", persona.fechaNac, "|", persona.dni)
        for item in persona.listaAviones:
            print("Avion: ", item.modelo)
        for item in persona.listaIdiomas:
            print("Idiomas:", item)
    elif type(persona) is Piloto and Pil:
        print(persona.nombre, "|", persona.apellido, "|", persona.fechaNac, "|", persona.dni)
        for item in persona.listaAviones:
            print("Avion: ", item.modelo)

def printDatosVuelo(vuelo):
    print(vuelo.avion.modelo, "|", vuelo.origen, "|", vuelo.destino, "|", vuelo.fecha, "|", vuelo.hora)
    for item in vuelo.listaPasajeros:
        print("Pasajeros: ", item.dni)
    for item in vuelo.listaTripulacion:
        print("Tripulacion: ", item.dni)

