import datetime

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
    def descerializar(self, dict, listaAviones):
        self.setNombre(dict["nombre"])
        self.setApellido(dict["apellido"])
        self.setDni(dict["dni"])
        self.setFechaNac(datetime.datetime.strptime(dict["fechaNacimiento"], "%Y-%m-%d"))

class Tripulante(Persona):  # Definicion de Tripulante
    def __init__(self):
        self.listaAviones = []

    # Sets y Adds
    def setListaAviones(self, listaAviones):
        self.listaAviones = listaAviones

    def addAvion(self, avion):
        self.listaAviones.append(avion)

    # Otros Metodos
    def descerializar(self, dict, listaAviones):
        super().descerializar(dict, listaAviones)
        for item in dict["avionesHabilitados"]:
            for meti in listaAviones:
                if item == meti.modelo:
                    self.addAvion(meti)

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
    def descerializar(self, dict, listaAviones):
        super().descerializar(dict, listaAviones)
        for item in dict["idiomas"]:
            self.addIdioma(item)

class Pasajero(Persona):    # Definicion de Pasajero
    vip = None
    necesidadEspecial = None

    # Sets y Adds
    def setVip(self, vip):
        self.vip = vip

    def setNecesidadEspecial(self, necesidadEspecial):
        self.necesidadEspecial = necesidadEspecial

    # Otros Metodos
    def descerializar(self, dict, listaAviones):
        super().descerializar(dict, listaAviones)
        self.vip = dict["vip"]
        if "solicitudesEspeciales" in dict:
            self.setNecesidadEspecial(dict["solicitudesEspeciales"])