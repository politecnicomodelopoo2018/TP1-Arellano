from datetime import *

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

    # Otros Metodos
    def descerializar(self, dict):
        self.nombre = dict["nombre"]
        self.apellido = dict["apellido"]
        self.dni = dict["dni"]
        self.fechaNac = datetime.strptime(dict["fechaNacimiento"], "%Y-%m-%d")

    def getEdad(self):
        return datetime.now().year - self.fechaNac.year

class Tripulante(Persona):  # Definicion de Tripulante
    def __init__(self):
        self.listaAviones = []

    # Sets y Adds
    def setListaAviones(self, listaAviones):
        self.listaAviones = listaAviones

    def addAvion(self, avion):
        self.listaAviones.append(avion)

    # Otros Metodos
    def descerializar(self, dict):
        super().descerializar(dict)
        for item in dict["avionesHabilitados"]:
            self.listaAviones.append(item)

class Piloto(Tripulante):   # Definicion de Piloto
    pass

class Servicio(Tripulante):   # Definicion de ServicioAbordo
    def __init__(self):
        super().__init__()
        self.listaIdiomas = []

    # Sets y Adds
    def setListaIdiomas(self, listaIdiomas):
        self.listaIdiomas = listaIdiomas

    def addIdioma(self, idioma):
        self.listaIdiomas.append(idioma)

    # Otros Metodos
    def descerializar(self, dict):
        super().descerializar(dict)
        for item in dict["idiomas"]:
            self.listaIdiomas.append(item)

class Pasajero(Persona):    # Definicion de Pasajero
    vip = None
    necesidadEspecial = None

    # Sets y Adds
    def setVip(self, vip):
        self.vip = vip

    def setNecesidadEspecial(self, necesidadEspecial):
        self.necesidadEspecial = necesidadEspecial

    # Otros Metodos
    def descerializar(self, dict):
        super().descerializar(dict)
        self.vip = dict["vip"]
        # self.necesidadEspecial = dict["solicitudesEspeciales"]