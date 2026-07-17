"""
URL configuration for gcars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventario.views import (
    VehiculoListView, VehiculoDetailView, VehiculoCreateView,
    VehiculoUpdateView, VehiculoDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VehiculoListView.as_view(), name='vehiculo_list'),
    path('vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detail'),
    path('vehiculo/nuevo/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculo/<int:pk>/editar/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculo/<int:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),
]
