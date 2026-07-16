import json
import os

ARCHIVO = "vehiculos.json"


def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as archivo:
        try:
            return json.load(archivo)
        except:
            return []


def guardar_datos(vehiculos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(vehiculos, archivo, indent=4)