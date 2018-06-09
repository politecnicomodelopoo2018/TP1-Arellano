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

print("\n", "PASAJEROS")
for item in listaPersonas:
    printDatosPersona(item, True)

print("\n", "Pasajeros Jovenes")
for item in listaVuelos:
    print("Vuelo", item.avion.modelo)
    pasajeroJoven = item.pasajeroJoven()
    print("paasa: ", pasajeroJoven.dni)
    for meti in item.listaPasajeros:
        if meti == pasajeroJoven:
            print(meti.nombre, "|", meti.apellido, "|", meti.fechaNac, "|*")
        else:
            print(meti.nombre, "|", meti.apellido, "|", meti.fechaNac)



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
    if item.validarTripulacion():
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)
print("INVALIDOS por Aviones Permitidos")
for item in listaVuelos:
    if not item.validarTripulacion():
        print(item.avion.modelo, "|", item.origen, "|", item.destino, "|", item.fecha, "|", item.hora)

print("VALIDOS por Un Dia - Un Vuelo")
for item in listaPersonas:
    if type(item) is Piloto:
        if s.verificarDiasPiloto(item):
            print(item.nombre, "|", item.apellido, "|", item.dni)

print("INVALIDOS por Un Dia - Un Vuelo")
for item in listaPersonas:
    if type(item) is Piloto:
        if not s.verificarDiasPiloto(item):
            print(item.nombre, "|", item.apellido, "|", item.dni)

print("\n", "Pasajeros V/Ne")
for item in s.listaVuelos:
    print("Vuelo", item.avion.modelo)
    for meti in item.listaVoNe():
        print(meti.dni)

print("\n", "IDIOMAS POR VUELO")
for item in s.listaVuelos:
    print("Vuelo", item.avion.modelo)
    for meti in item.idiomas():
        print(meti)