import json
import os
from vehiculo import Vehiculo

ARCHIVO = "vehiculos.json"


def cargar_datos():
    """Carga los vehículos desde el archivo JSON."""

    if not os.path.exists(ARCHIVO):
        return []

    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        vehiculos = []

        for v in datos:
            vehiculo = Vehiculo(
                v["marca"],
                v["modelo"],
                v["kilometraje"],
                v["precio"],
                v["patente"]
            )
            vehiculos.append(vehiculo)

        return vehiculos

    except (json.JSONDecodeError, KeyError, FileNotFoundError):
        return []


def guardar_datos(vehiculos):
    """Guarda la lista de vehículos en el archivo JSON."""

    datos = []

    for vehiculo in vehiculos:
        datos.append(vehiculo.to_dict())

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def buscar_por_patente(patente):
    """Busca un vehículo por patente."""

    vehiculos = cargar_datos()

    for vehiculo in vehiculos:
        if vehiculo.patente.upper() == patente.upper():
            return vehiculo

    return None


def actualizar_vehiculo(patente, nuevo_vehiculo):
    """Actualiza un vehículo según su patente."""

    vehiculos = cargar_datos()

    for i in range(len(vehiculos)):
        if vehiculos[i].patente.upper() == patente.upper():
            vehiculos[i] = nuevo_vehiculo
            guardar_datos(vehiculos)
            return True

    return False


def agregar_vehiculo(vehiculo):
    """Agrega un vehículo nuevo."""

    vehiculos = cargar_datos()
    vehiculos.append(vehiculo)
    guardar_datos(vehiculos)


def listar_vehiculos():
    """Devuelve todos los vehículos."""

    return cargar_datos()