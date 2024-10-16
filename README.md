Alquiler de Películas
Descripción
Este proyecto es una plataforma de alquiler de películas donde los socios pueden registrarse, alquilar películas y agregar co-deudores. La aplicación permite gestionar una base de datos de películas y actores, ofreciendo una interfaz amigable para los usuarios.

Tabla de Contenidos
Características
Tecnologías Utilizadas
Instalación
Uso
Funcionalidades
Contribuciones
Enlace a la Aplicación
Licencia
Características
Registro de usuarios
Alquiler de películas
Gestión de co-deudores
Visualización de películas disponibles
Información detallada sobre cada película (título, sinopsis, actores, etc.)
Tecnologías Utilizadas
Backend: Django
Base de Datos: SQLite
Frontend: HTML, CSS, JavaScript
Implementación: Render
Control de versiones: Git y GitHub
Instalación
Clonar el repositorio:

bash
Copy code
git clone <url_del_repositorio>
cd <nombre_del_directorio>
Crear un entorno virtual:

bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instalar las dependencias:

bash
Copy code
pip install -r requirements.txt
Migrar la base de datos:

bash
Copy code
python manage.py migrate
Cargar datos iniciales (si corresponde):

bash
Copy code
python manage.py loaddata <nombre_de_archivo_json>
Ejecutar el servidor:

bash
Copy code
python manage.py runserver
Uso
Regístrate como nuevo usuario.
Inicia sesión con tus credenciales.
Explora la biblioteca de películas.
Alquila películas y añade co-deudores según sea necesario.
Funcionalidades
Registro: Los nuevos usuarios pueden registrarse ingresando su información.
Alquiler: Los socios pueden alquilar películas disponibles en la plataforma.
Co-deudores: Los usuarios pueden agregar co-deudores para gestionar los alquileres de manera conjunta.
Contribuciones
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama:
bash
Copy code
git checkout -b nombre_de_rama
Realiza tus cambios y haz commit:
bash
Copy code
git commit -m 'Descripción de los cambios'
Envía un pull request.
Enlace a la Aplicación
Puedes visitar la aplicación en el siguiente enlace: Alquiler de Películas

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
