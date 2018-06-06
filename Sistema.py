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

    def buscarPersonaEnLista(self, persona, listaPersonas):
        for item in listaPersonas:
            if persona == item.dni:
                return item

    def validarCanTripulacion(self, vuelo):
        for item in self.listaAviones:
            if vuelo.avion == item.modelo:
               if len(vuelo.listaTripulacion) < item.limTripulacion:
                   return False
        return True

    def validarTripulantes(self, vuelo):
        for item in vuelo.listaTripulacion:
            for meti in item.listaAviones:
                if meti == vuelo.avion:
                    return True
        return False

    def pasajerosPorVuelo(self, vuelo):
        pasajerosEnVuelo = []
        for meti in vuelo.listaPasajeros:
            pasajerosEnVuelo.append(meti)
        return pasajerosEnVuelo

    def pasajeroJoven(self, listaPasajeros):
        fechaMayor = listaPasajeros[0].fechaNac
        joven = listaPasajeros[0]
        for item in listaPasajeros:
            if item.fechaNac > fechaMayor:
                joven = item
        return joven

    def VoEporVuelo(self, vuelo):
        listaGente = []
        for item in vuelo.listaPasajeros:
            if item.vip == 1 or item.necesidadEspecial is not None:
                listaGente.append(item)
        return listaGente



