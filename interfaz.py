import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from utils import listar_vehiculos, agregar_vehiculo, buscar_por_patente, actualizar_vehiculo
from vehiculo import Vehiculo

ventana = tk.Tk()
ventana.title("GCars")
ventana.geometry("600x500")

# Marco principal
marco_principal = ttk.Frame(ventana, padding="10")
marco_principal.pack(fill=tk.BOTH, expand=True)

# Título
titulo = ttk.Label(marco_principal, text="Sistema GCars", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Botones de opciones
marco_botones = ttk.Frame(marco_principal)
marco_botones.pack(pady=10)

# Área de texto para mostrar información
texto_area = tk.Text(marco_principal, height=20, width=70)
texto_area.pack(fill=tk.BOTH, expand=True, pady=10)

# Funciones de los botones
def mostrar_vehiculos():
    """Muestra la lista de todos los vehículos."""
    texto_area.delete(1.0, tk.END)
    vehiculos = listar_vehiculos()
    
    if not vehiculos:
        texto_area.insert(tk.END, "No hay vehículos registrados.")
        return
    
    texto_area.insert(tk.END, "=== LISTA DE VEHÍCULOS ===\n\n")
    for i, v in enumerate(vehiculos, 1):
        texto_area.insert(tk.END, 
            f"{i}. Patente: {v.patente}\n"
            f"   Marca: {v.marca}\n"
            f"   Modelo: {v.modelo}\n"
            f"   Kilometraje: {v.kilometraje} km\n"
            f"   Precio: ${v.precio}\n\n")

def agregar_nuevo_vehiculo():
    """Abre un diálogo para agregar un nuevo vehículo."""
    ventana_agregar = tk.Toplevel(ventana)
    ventana_agregar.title("Agregar Vehículo")
    ventana_agregar.geometry("300x420")
    ventana_agregar.resizable(False, False)
    
    # Campos de entrada
    ttk.Label(ventana_agregar, text="Patente:").pack(pady=5)
    entry_patente = ttk.Entry(ventana_agregar, width=30)
    entry_patente.pack(pady=5)
    
    ttk.Label(ventana_agregar, text="Marca:").pack(pady=5)
    entry_marca = ttk.Entry(ventana_agregar, width=30)
    entry_marca.pack(pady=5)
    
    ttk.Label(ventana_agregar, text="Modelo:").pack(pady=5)
    entry_modelo = ttk.Entry(ventana_agregar, width=30)
    entry_modelo.pack(pady=5)
    
    ttk.Label(ventana_agregar, text="Kilometraje:").pack(pady=5)
    entry_km = ttk.Entry(ventana_agregar, width=30)
    entry_km.pack(pady=5)
    
    ttk.Label(ventana_agregar, text="Precio:").pack(pady=5)
    entry_precio = ttk.Entry(ventana_agregar, width=30)
    entry_precio.pack(pady=5)
    
    def guardar():
        try:
            patente = entry_patente.get().strip()
            marca = entry_marca.get().strip()
            modelo = entry_modelo.get().strip()
            km = int(entry_km.get())
            precio = float(entry_precio.get())
            
            if not all([patente, marca, modelo]):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            
            vehiculo = Vehiculo(marca, modelo, km, precio, patente)
            agregar_vehiculo(vehiculo)
            messagebox.showinfo("Éxito", f"Vehículo {patente} agregado correctamente.")
            ventana_agregar.destroy()
            mostrar_vehiculos()
        except ValueError:
            messagebox.showerror("Error", "Kilometraje y precio deben ser números.")
    
    ttk.Button(ventana_agregar, text="Guardar", command=guardar).pack(pady=10)

def buscar_vehiculo():
    """Busca un vehículo por patente."""
    patente = simpledialog.askstring("Buscar Vehículo", "Ingrese la patente:")
    
    if patente is None:
        return
    
    vehiculo = buscar_por_patente(patente)
    texto_area.delete(1.0, tk.END)
    
    if vehiculo:
        texto_area.insert(tk.END, "=== VEHÍCULO ENCONTRADO ===\n\n"
            f"Patente: {vehiculo.patente}\n"
            f"Marca: {vehiculo.marca}\n"
            f"Modelo: {vehiculo.modelo}\n"
            f"Kilometraje: {vehiculo.kilometraje} km\n"
            f"Precio: ${vehiculo.precio}")
    else:
        texto_area.insert(tk.END, f"No se encontró vehículo con patente '{patente}'.")

# Crear botones con comandos
boton_listar = ttk.Button(marco_botones, text="Listar Vehículos", command=mostrar_vehiculos)
boton_listar.pack(side=tk.LEFT, padx=5)

boton_agregar = ttk.Button(marco_botones, text="Agregar Vehículo", command=agregar_nuevo_vehiculo)
boton_agregar.pack(side=tk.LEFT, padx=5)

boton_buscar = ttk.Button(marco_botones, text="Buscar Vehículo", command=buscar_vehiculo)
boton_buscar.pack(side=tk.LEFT, padx=5)
