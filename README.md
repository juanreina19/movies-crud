---

# Alquiler de Películas - GLOB GUSTERS

## Descripción

Este proyecto es una plataforma de alquiler de películas donde los socios pueden registrarse, alquilar películas y agregar co-deudores. La aplicación permite gestionar una base de datos de películas y actores, ofreciendo una interfaz amigable para los usuarios.

## Tabla de Contenidos

- [Enlace a la Aplicación](#enlace-a-la-aplicación)
- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)

## Enlace a la Aplicación

Puedes visitar la aplicación en el siguiente enlace: [GLOB GUSTERS WEB](https://movies-crud-iivw.onrender.com/)
- `Note: Si la pagina no carga, espera al menos 40 segundos y dale f5.`

## Características

- Registro de usuarios
- Alquiler de películas
- Gestión de co-deudores
- Visualización de películas disponibles
- Información detallada sobre cada película (título, sinopsis, actores, etc.)

## Tecnologías Utilizadas

- **Backend**: Django
- **Base de Datos**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Implementación**: Render
- **Control de versiones**: Git y GitHub

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url_del_repositorio>
   cd <nombre_del_directorio>
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos**:
   ```bash
   python manage.py migrate
   ```

5. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

## Uso

- Regístrate como nuevo usuario.
- Inicia sesión con tus credenciales.
- Explora la biblioteca de películas.
- Alquila películas y añade co-deudores según sea necesario.

## Funcionalidades

- **Registro**: Los nuevos usuarios pueden registrarse ingresando su información.
- **Alquiler**: Los socios pueden alquilar películas disponibles en la plataforma.
- **Co-deudores**: Los usuarios pueden agregar co-deudores para gestionar los alquileres de manera conjunta.




