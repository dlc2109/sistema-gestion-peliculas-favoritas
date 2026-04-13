from services.mis_peliculas_favoritas import MisPeliculasFavoritas
from models.usuario import Usuario
from models.pelicula import Pelicula

sistema = MisPeliculasFavoritas('mis peliculas favoritas')

nombre_completo = input('Ingresa tu usuario(nombre): ').lower().strip()
usuario = Usuario(nombre_completo)
print(usuario)

while True:
    print('---Sistema de Peliculas Favoritas---')
    print('1. Agregar Peliculas Favoritas')
    print('2. Listar Peliculas Favoritas')
    print('3. Eliminar Peliculas ')
    print('4. Salir')

    opcion = int(input('Elige una opcion: '))
    match opcion:
            case 1:
              titulo_peli = input('Ingresa Titulo: ').lower().strip()
              genero_peli = input('Ingresa Genero: ').lower().strip()

              try:
               anio_peli= int(input('Ingrese anio: '))
               id_peli = int(input('Ingresa ID: '))
              except ValueError:
                print('Ingresa numeros')
                continue

              nueva_peli = Pelicula(titulo_peli,genero_peli,anio_peli,id_peli)
              print( sistema.agregar_pelicula(usuario,nueva_peli))
            case 2: 
                sistema.listar_peliculas(usuario)
            case 3:
                sistema.eliminar(usuario)
            case 4: 
             print('Fin del Programa')
             break


 
     