from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Vehiculo
from django import forms

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'kilometraje', 'precio', 'patente']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'patente': forms.TextInput(attrs={'class': 'form-control'}),
        }

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'inventario/vehiculo_list.html'
    context_object_name = 'vehiculos'

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'inventario/vehiculo_detail.html'

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'inventario/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'inventario/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'inventario/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')
