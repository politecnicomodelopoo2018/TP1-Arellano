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
listaPersonas = generarListaPersonas(d, listaAviones)
listaVuelos = generarListaVuelos(d, listaPersonas, listaAviones)
s.cargar(listaPersonas, listaVuelos, listaAviones)

print("\n", "AVIONES")
for item in listaAviones:
    printDatosAvion(item)

print("\n", "PERSONAS")
print("SERVICIO")
for item in listaPersonas:
    printDatosPersona(item)

print("\n", "VUELOS")
for item in listaVuelos:
    printDatosVuelo(item)

print("\n", "Pasajeros Jovenes")
for item in listaVuelos:
    esto = s.pasajerosPorVuelo(item)
    pasajeroJoven = esto[0]
    for meti in esto:
        if meti == pasajeroJoven:
            print(meti.nombre, "|", meti.apellido, "|*")
        else:
            print(meti.nombre, "|", meti.apellido)

print("\n", "Pasajeros V/Ne")
for item in s.listaVuelos:
    print("Vuelo", item.avion.modelo)
    for meti in item.listaVoNe():
        print(meti.dni)

print("\n", "VALIDANDO")
print("VALIDOS por Cant")
for item in listaVuelos:
    if item.validarCanTripulacion():
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)

print("INVALIDOS por Cant")
for item in listaVuelos:
    if not item.validarCanTripulacion():
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)

print("VALIDOS por Aviones Permitidos")
for item in listaVuelos:
    if s.validarAvionTripulantes(item):
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)
print("INVALIDOS por Aviones Permitidos")
for item in listaVuelos:
    if not s.validarAvionTripulantes(item):
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)




