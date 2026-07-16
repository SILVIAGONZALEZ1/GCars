class Vehiculo:

    def __init__(self, marca, modelo, kilometraje, precio, patente):
        self.marca = marca
        self.modelo = modelo
        self.kilometraje = kilometraje
        self.precio = precio
        self.patente = patente

    def to_dict(self):
        return {
            "marca": self.marca,
            "modelo": self.modelo,
            "kilometraje": self.kilometraje,
            "precio": self.precio,
            "patente": self.patente
        }