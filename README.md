# sistema-gestion-peliculas-favoritas
 Sistema en Python: Aplicación interactiva de consola para gestionar y persistir películas favoritas usando Programación Orientada a Objetos (POO) y Bases de Datos Relacionales (SQLite3).
 
Es un programa diseñado para que múltiples usuarios puedan gestionar y almacenar su propia colección de películas preferidas de forma permanente. A diferencia de un programa tradicional en memoria, este sistema implementa persistencia de datos real, lo que significa que puedes cerrar la aplicación y tus películas seguirán almacenadas de forma segura la próxima vez que inicies sesión. El proyecto está construido bajo una arquitectura modular profesional, separando los modelos, los servicios, y la base de datos.

¿Qué puedes hacer con él?
El sistema ofrece un menú interactivo con las siguientes funciones principales:

* Registro / Inicio de Sesión: Ingresa con tu propio nombre y un ID único. El sistema registrará tu perfil en la base de datos para crear tu propia "bóveda" de información aislada de otros usuarios.
* Añadir a favoritos: Guarda una película en tu lista personal. El sistema se encarga de crear el objeto, validar los datos y ejecutar sentencias seguras en SQL para vincular la película a tu perfil.
* Ver mi lista: Muestra de forma ordenada todas las películas que has guardado hasta el momento, leyendo los datos en tiempo real directo desde el archivo .db.
* Quitar de favoritos: Borra permanentemente una película de la base de datos mediante su número de identificación 
