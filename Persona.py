
class Persona(object):  # Definición de Persona
    nombre = None
    apellido = None
    fechaNac = None
    dni = None

    # Sets y Adds
    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFechaNac(self, fechaNac):
        self.fechaNac = fechaNac

    def setDni(self, dni):
        self.dni = dni


class Tripulante(Persona):  # Definicion de Tripulante
    def __init__(self):
        self.listaAviones = []

    # Sets y Adds
    def setListaAviones(self, listaAviones):
        self.listaAviones = listaAviones

    def addAvion(self, avion):
        self.listaAviones.append(avion)


class Piloto(Tripulante):   # Definicion de Piloto
    pass


class ServicioAbordo(Tripulante):   # Definicion de ServicioAbordo
    def __init__(self):
        self.listaIdiomas = []

    # Sets y Adds
    def setListaIdiomas(self, listaIdiomas):
        self.listaIdiomas = listaIdiomas

    def addIdioma(self, idioma):
        self.listaIdiomas.append(idioma)

class Pasajero(Persona):    # Definicion de Pasajero
    vip = None

    # Sets y Adds
    def setVip(self, vip):
        self.vip = vip
