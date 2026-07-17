from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'modelo', 'kilometraje', 'precio')
    list_filter = ('marca', 'modelo')
    search_fields = ('patente', 'marca', 'modelo')
    ordering = ('-id',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('patente', 'marca', 'modelo')
        }),
        ('Detalles del Vehículo', {
            'fields': ('kilometraje', 'precio')
        }),
    )