Proyecto de E-commerce con Django
Descripción
Este es un proyecto de un pequeño e-commerce desarrollado en Python utilizando el framework Django. El proyecto cuenta con las siguientes funcionalidades:

Página de inicio (Home).

Sistema de autenticación de usuarios (Login).

Visualización de categorías.

Visualización de productos con detalles como imagen, talle, color y descripción breve.

Acceso de administrador para realizar CRUD en la base de datos.

Búsqueda de categorías y productos a través de buscadores propios.

Actualmente, el proyecto no tiene implementada la parte de shop (carrito de compras y pagos).

Requisitos
Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

Python 3.x

Django 3.x o superior

SQLite (por defecto en Django, puedes cambiar la base de datos según tus necesidades)


Uso
Acceso de Usuario
Los usuarios pueden registrarse e iniciar sesión en el sistema.

Pueden navegar por las categorías y buscar productos específicos.

En la página de productos, pueden ver los detalles del producto incluyendo imagen, talle, color y una breve descripción.

Acceso de Administrador
Los administradores pueden acceder al panel de administración de Django en http://127.0.0.1:8000/admin/.

Desde el panel de administración, pueden realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos para gestionar categorías y productos.
(para agregar talle y color solo se puede hacer del panel de admin de django)

Tecnologías Utilizadas
Backend: Django

Base de Datos: SQLite (puede ser reemplazada por cualquier otra base de datos compatible con Django)

Frontend: HTML, CSS,
Autenticación: Sistema de autenticación de Django

Contribuir
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una nueva rama (git checkout -b nombre-de-la-rama).

Realiza los cambios y haz commit (git commit -m 'Descripción del cambio').

Sube los cambios a tu rama (git push origin nombre-de-la-rama).

Crea un pull request.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más información.


Instalación
Clona el repositorio:

bash
git clone https://github.com/Lean189/Proyecto_final
cd Proyecto_final
Crea y activa un entorno virtual (opcional pero recomendado):

bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias:

bash
pip install -r requirements.txt
Realiza las migraciones de la base de datos:

bash
python manage.py makemigrations
python manage.py migrate
Crea un superusuario para acceder al panel de administración:

bash
python manage.py createsuperuser
Ejecuta el servidor de desarrollo:

bash
python manage.py runserver
Abre tu navegador y navega a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.




link Youtube:
[text](https://youtu.be/9GfZEfvgCDs)

