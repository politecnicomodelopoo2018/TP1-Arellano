
# Definicion de Sistema
class Sistema(object):
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

    def buscarEnLista(self, algo, lista):
        for item in lista:
            if algo == item:
                return item

    def cargar(self, listaPersonas, listaVuelos, listaAviones):
        self.listaVuelos = listaVuelos
        self.listaAviones = listaAviones
        self.listaPersonas = listaPersonas

    def pasajerosPorVuelo(self, vuelo):
        pasajerosEnVuelo = []
        for item in self.listaVuelos:
            if item == vuelo:
                for meti in item.listaPasajeros:
                    pasajerosEnVuelo.append(meti)
        return pasajerosEnVuelo

    def pasajeroJoven(self, listaPasajeros):
        edad = listaPasajeros[0].getEdad
        joven = listaPasajeros[0]
        for item in listaPasajeros:
            if item.getEdad < edad:
                joven = item
        return joven

    def validarCanTripulacion(self, vuelo):
        for item in self.listaAviones:
            if vuelo.avion == item.modelo:
               if len(vuelo.listaTripulacion) < item.limTripulacion:
                   return 1
        return 0

    def validarTripulantes(self, vuelo):
        for item in vuelo.listaTripulacion:
            for meti in self.buscarEnLista(item, self.listaPersonas):
                for temi in meti.listaAviones:
                    if temi == vuelo.avion:
                        return 1
        return 0

        for item in vuelo.listaTripulacion:
            tripulante = self.buscarEnLista(item, self.listaTripulacion)






