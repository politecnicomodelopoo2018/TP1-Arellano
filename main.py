from Persona import *
from Sistema import *
from Vuelo import *
from Avion import *
import json
from datetime import *
from Funciones import *

s = Sistema()
d = {}

d = traerArchivo("datos.json")

listaAviones = generarListaAviones(d)


for item in listaAviones:
    print(item.modelo)
    print(item.limPasajeros)
    print(item.limTripulacion)
