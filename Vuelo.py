from datetime import *

class Vuelo(object):    # Definicion de Vuelo
    avion = None
    origen = None
    destino = None
    fecha = None
    hora = None

    def __init__(self):
        self.listaPasajeros = []
        self.listaTripulacion = []

    # Sets y Adds
    def setAvion(self, avion):
        self.avion = avion

    def setOrigen(self, origen):
        self.origen = origen

    def setDestino(self, destino):
        self.destino = destino

    def setFecha(self, fecha):
        self.fecha = fecha

    def setHora(self, hora):
        self.hora = hora

    def setListaPasajeros(self, listaPasajeros):
        self.listaPasajeros = listaPasajeros

    def addPasajero(self, pasajero):
        self.listaPasajeros.append(pasajero)

    def setListaTripulacion(self, listaTripulacion):
        self.listaTripulacion = listaTripulacion

    def addTripulante(self, tripulante):
        self.listaTripulacion.append(tripulante)

    # Otros Metodos
    def descerializar(self, dict):
        self.avion = dict["avion"] # Ver si meter Avion()
        self.fecha = datetime.strptime(dict["fecha"], "%Y-%m-%d")
        self.hora = dict["hora"]
        self.destino = dict["destino"]
        self.origen = dict["origen"]
        for item in dict["pasajeros"]:
            self.listaPasajeros.append(item)
        for item in dict["tripulacion"]:
            self.listaTripulacion.append(item)


