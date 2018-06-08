from Persona import *

# Definicion de Sistema
class Sistema(object):

    __instance = None
    nombre = None

    def __new__(cls):
        if Sistema.__instance is None:
            Sistema.__instance = object.__new__(cls)
        return Sistema.__instance

    def __init__(self):
        self.listaPersonas = []
        self.listaVuelos = []
        self.listaAviones = []

    # Sets y Adds
    def setListaPersonas(self, listaPersonas):
        self.listaPersonas = listaPersonas

    def setListaVuelos(self, listaVuelos):
        self.listaVuelos = listaVuelos

    def setListaAviones(self, listaAviones):
        self.listaAviones = listaAviones

    def addPersona(self, persona):
        self.listaPersonas.append(persona)

    def addVuelo(self, vuelo):
        self.listaVuelos.append(vuelo)

    def addAvion(self, avion):
        self.listaAviones.append(avion)

    # Otros Metodos

    def cargar(self, listaPersonas, listaVuelos, listaAviones):
        self.listaVuelos = listaVuelos
        self.listaAviones = listaAviones
        self.listaPersonas = listaPersonas

    def vuelosHechosPorPiloto(self, piloto):
        listaVuelos = []
        for item in self.listaVuelos:
            for meti in item.listaTripulacion:
                if meti == piloto:
                    listaVuelos.append(item)
        return listaVuelos

    def verificarDiasPiloto(self, piloto):
        for item in self.vuelosHechosPorPiloto(piloto):
            for meti in self.vuelosHechosPorPiloto(piloto):
                if item.fecha.day == meti.fecha.day:
                    return False
        return True








