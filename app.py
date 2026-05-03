from services.mis_peliculas_favoritas import MisPeliculasFavoritas
from models.usuario import Usuario
from models.pelicula import Pelicula
from db.database import get_connection
from db.database import  registrar_usuario_db

sistema = MisPeliculasFavoritas('mis peliculas favoritas')

nombre_completo = input('Ingresa tu usuario(nombre): ').lower().strip()
try:
    id_usuario= int(input('Ingresa tu ID: '))
except ValueError:
    print('Ingresa numeros en el ID')
usuario = Usuario(nombre_completo,id_usuario)
print(usuario)

registrar_usuario_db(usuario)

while True:
    print(f'---{sistema.nombre}---')
    print('1. Agregar Peliculas Favoritas')
    print('2. Listar Peliculas Favoritas')
    print('3. Eliminar Peliculas ')
    print('4. Salir')

    opcion = int(input('Elige una opcion: '))
    match opcion:
            case 1:
                print(sistema.agregar_pelicula(usuario))
            case 2: 
                sistema.listar_peliculas(usuario)
            case 3:
                sistema.eliminar(usuario)
            case 4: 
             print('Fin del Programa')
             break


 
     