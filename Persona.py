class Persona(object):
    nombre = None
    apellido = None
    fechaNac = None
    dni = None

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFechaNac(self, fechaNac):
        self.fechaNac = fechaNac

    def setDni(self, dni):
        self.dni = dni

class Tripulacion(Persona):
    def __init__(self):
        self.listaAviones = []

class Piloto(Tripulacion):
    pass

class ServicioAbordo(Tripulacion):
    def __init__(self):
        self.listaIdiomas = []

class Pasajero(Persona):
    vip = None

    def setVip(self, vip):
        self.vip = vip
