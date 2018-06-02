
class Avion(object):    # Definicion de Avion
    modelo = None
    limPasajeros = None
    limTripulacion = None

    # Sets y Adds
    def setModelo(self, modelo):
        self.modelo = modelo

    def setLimPasajeros(self, limPasajeros):
        self.limPasajeros = limPasajeros

    def setLimTripulacion(self, limTripulacion):
        self.limTripulacion = limTripulacion

    # Otros Metodos
    def descerializar(self, dict):
            self.modelo = dict["codigoUnico"]
            self.limPasajeros = dict["cantidadDePasajerosMaxima"]
            self.limTripulacion = dict["cantidadDeTripulacionNecesaria"]