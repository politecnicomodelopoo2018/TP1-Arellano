from datetime import *
from Persona import *

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
    def descerializar(self, dict, listaPersonas, listaAviones):
        for item in listaAviones:
            if dict["avion"] == item.modelo:
                self.avion = item
        self.setFecha(datetime.strptime(dict["fecha"], "%Y-%m-%d"))
        self.setHora(dict["hora"])
        self.setDestino(dict["destino"])
        self.setOrigen(dict["origen"])
        for item in dict["pasajeros"]:
            for meti in listaPersonas:
                if type(meti) is Pasajero and item == meti.dni:
                    self.addPasajero(meti)
        for item in dict["tripulacion"]:
            for meti in listaPersonas:
                if ((type(meti) is Piloto) or (type(meti) is Servicio)) and item == meti.dni:
                    self.addTripulante(meti)

    def verificarTripulante(self, tripulante):
        for item in tripulante.listaAviones:
            if item.modelo == self.avion.modelo:
                return True
        return False

    def validarTripulacion(self):
        for item in self.listaTripulacion:
            if not self.verificarTripulante(item):
                return False
        return True

    def validarCanTripulacion(self):
        if len(self.listaTripulacion) < self.avion.limTripulacion:
            return False
        return True

    def listaVoNe(self):
        listaGente = []
        for item in self.listaPasajeros:
            if item.vip == 1 or item.necesidadEspecial is not None:
                listaGente.append(item)
        return listaGente

    def pasajeroJoven(self):
        joven = self.listaPasajeros[0]
        for item in self.listaPasajeros:
            if item.fechaNac > joven.fechaNac:
                joven = item
        return joven

    def idiomas(self):
        lista = []
        for item in self.listaTripulacion:
            if type(item) is Servicio:
                for item in item.listaIdiomas:
                    if item not in lista:
                        lista.append(item)
        return lista




