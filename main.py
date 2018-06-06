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
listaPersonas = generarListaPersonas(d)

for item in listaAviones:
    print(item.modelo)
    print(item.limPasajeros)
    print(item.limTripulacion)

print("SERVICIO")
for item in listaPersonas:
    if type(item) == Servicio:
        print(item.nombre, "|", item.apellido, "|", item.dni, "|", item.fechaNac)
        print("Aviones")
        for meti in item.listaAviones:
            print(meti)
        print("Idiomas")
        for meti in item.listaIdiomas:
            print(meti)

print("PILOTO")
for item in listaPersonas:
    if type(item) == Piloto:
        print(item.nombre, "|", item.apellido, "|", item.dni , "|", item.fechaNac)
        print("Aviones")
        for meti in item.listaAviones:
            print(meti)

print("PASAJERO")
for item in listaPersonas:
    if type(item) == Pasajero:
        print(item.nombre, "|", item.apellido, "|", item.dni, "|", item.fechaNac, "|", item.vip)
