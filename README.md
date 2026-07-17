# 🚗 GCars - Sistema de Gestión de Vehículos

## 📌 Descripción del proyecto

GCars es una aplicación web desarrollada con **Django** para la gestión de vehículos.

El objetivo del sistema es brindar una herramienta sencilla para administrar información de automóviles mediante una plataforma web, permitiendo registrar, consultar y organizar datos desde un panel administrativo.

El proyecto está desarrollado utilizando:

* Python
* Django
* SQLite como base de datos inicial
* HTML / CSS / Bootstrap para la interfaz
* Django Admin para la administración del sistema

---

# 🎯 Objetivo del sistema

GCars busca facilitar la administración de un inventario de vehículos, centralizando la información y permitiendo una gestión ordenada desde un entorno web.

El sistema está pensado para poder crecer incorporando nuevos módulos como:

* Clientes
* Ventas
* Historial de vehículos
* Fotografías
* Reportes
* Estadísticas
* Gestión de usuarios y permisos

---

# 🚀 Funcionalidades actuales

## 👤 Gestión de usuarios

El sistema utiliza el sistema de autenticación incluido en Django.

Permite:

* Inicio de sesión.
* Control de acceso.
* Administración mediante usuarios registrados.
* Gestión desde el panel administrativo.

---

## 🚘 Gestión de vehículos

El sistema está preparado para administrar información relacionada con vehículos:

* Marca.
* Modelo.
* Año.
* Datos generales.
* Información del inventario.

Las funcionalidades pueden ampliarse agregando nuevos campos y módulos según las necesidades del negocio.

---

# 💻 Requisitos del sistema

Para ejecutar el proyecto se necesita:

## Python

Versión recomendada:

```
Python 3.14+
```

Verificar instalación:

```bash
python --version
```

---

## Django

Verificar instalación:

```bash
python -m django --version
```

---

# 📂 Ubicación del proyecto

Ejemplo:

```
C:\GCars\GCarsDjango
```

---

# ⚙️ Instalación y configuración

## 1) Abrir la carpeta del proyecto

Desde una terminal:

```powershell
cd C:\GCars\GCarsDjango
```

---

## 2) Crear entorno virtual (recomendado)

Crear entorno:

```bash
python -m venv venv
```

Activarlo en Windows:

```bash
venv\Scripts\activate
```

---

## 3) Instalar dependencias

Si existe el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

Si se necesita generarlo:

```bash
pip freeze > requirements.txt
```

---

# 🗄️ Configuración de base de datos

Antes de ejecutar el sistema aplicar migraciones:

```bash
python manage.py migrate
```

Las migraciones crean las tablas necesarias para Django.

---

# 👤 Usuario administrador de prueba

El sistema cuenta con un usuario administrador para pruebas.

## Datos de acceso:

```
Usuario:
admin_gcars

Contraseña:
GCars2026*
```

Acceso al panel:

```
http://127.0.0.1:8000/admin/
```

Este usuario tiene permisos de administrador:

* is_staff: True
* is_superuser: True

---

# ▶️ Ejecutar el proyecto

Desde la carpeta:

```
C:\GCars\GCarsDjango
```

Ejecutar:

```bash
python manage.py runserver
```

Cuando aparezca:

```
Starting development server at http://127.0.0.1:8000/
```

Abrir el navegador:

Página principal:

```
http://127.0.0.1:8000/
```

Panel administrativo:

```
http://127.0.0.1:8000/admin/
```

---

# 🛑 Detener el servidor

Para detener Django:

Presionar:

```
CTRL + C
```

en la terminal.

---

# 🔐 Administración de usuarios

Crear un nuevo usuario administrador:

```bash
python manage.py createsuperuser
```

Django solicitará:

```
Username:
Email:
Password:
```

---

# 🔄 Actualización de modelos

Cuando se realizan cambios en los modelos:

Crear nuevas migraciones:

```bash
python manage.py makemigrations
```

Aplicar cambios:

```bash
python manage.py migrate
```

---

# 🧪 Uso en desarrollo

Actualmente GCars está configurado para trabajar en entorno local.

Antes de utilizarlo en producción se recomienda:

* Configurar DEBUG=False.
* Utilizar variables de entorno.
* Configurar una base de datos profesional.
* Configurar archivos estáticos.
* Utilizar un servidor web adecuado.

---

# 🛠️ Tecnologías utilizadas

| Tecnología   | Uso                        |
| ------------ | -------------------------- |
| Python       | Lenguaje principal         |
| Django       | Framework web              |
| SQLite       | Base de datos inicial      |
| Django Admin | Administración del sistema |
| HTML         | Estructura web             |
| CSS          | Estilos                    |
| Bootstrap    | Diseño responsive          |

---

# 📌 Posibles mejoras futuras

El proyecto puede evolucionar incorporando:

## Gestión comercial

* Registro de clientes.
* Seguimiento de ventas.
* Estado de vehículos.
* Historial de operaciones.

## Inventario avanzado

* Fotografías.
* Características técnicas.
* Disponibilidad.
* Ubicación del vehículo.

## Reportes

* Estadísticas de ventas.
* Vehículos disponibles.
* Informes generales.

## Usuarios

* Diferentes niveles de acceso.
* Usuarios vendedores.
* Usuarios administrativos.

---

# 🧑‍💻 Desarrollo

Proyecto:

```
GCars
```

Framework:

```
Django
```

Lenguaje:

```
Python
```

Base de datos:

```
SQLite
```

Estado:

```
🟢 En desarrollo
```

---

# 📘 Notas importantes

* No modificar directamente la base de datos sin realizar migraciones.
* Mantener actualizado el archivo requirements.txt.
* Realizar copias de seguridad antes de cambios importantes.
* Cambiar las credenciales de prueba antes de una puesta en producción.

---

## Fin del documento
