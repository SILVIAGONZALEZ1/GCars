from django.db import models


class Vehiculo(models.Model):

    marca = models.CharField(max_length=30)

    modelo = models.CharField(max_length=30)

    kilometraje = models.PositiveIntegerField()

    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    patente = models.CharField(
        max_length=10,
        unique=True
    )

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.patente}"
