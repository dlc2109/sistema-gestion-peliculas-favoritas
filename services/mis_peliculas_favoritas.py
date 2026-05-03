from models.pelicula import Pelicula
from models.usuario import Usuario
from db.database import get_connection



class MisPeliculasFavoritas:
    def __init__(self,nombre):
        self.nombre = nombre

    def agregar_pelicula(self, usuario):
        titulo_peli = input('Ingresa Titulo: ').lower().strip()
        genero_peli = input('Ingresa Genero: ').lower().strip()

        try:
            anio_peli = int(input('Ingrese anio: '))
            id_peli = int(input('Ingresa ID: '))
        except ValueError:
            return 'Error: Ingresa números válidos para el anio e ID.'

        nueva_peli = Pelicula(titulo_peli, genero_peli, anio_peli, id_peli)
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Pelicula (TITULO, GENERO, ANIO, USUARIO_ID) VALUES (?,?,?,?)" , (nueva_peli.titulo ,nueva_peli.genero,nueva_peli.anio,usuario.id_usuario))
        connection.commit()
        connection.close()
        return f'La película {nueva_peli.titulo} fue agregada con éxito'
    
    def listar_peliculas(self,usuario):
        connection= get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM PELICULA WHERE USUARIO_ID = ? ",(usuario.id_usuario,))
        listado = cursor.fetchall()
        connection.close()

        if not listado:
            print('No hay peliculas guardadas')
            return
        print(f' Lista de Favoritos de {usuario.nombre_completo}')
        for p in  listado:
            print(p)

    def eliminar(self,usuario):
        self.listar_peliculas(usuario)
        try:
            peli_eliminar = int(input('Ingrese ID de la pelicula a eliminar: '))
        except ValueError:
            print(' Error: Ingresa un número válido para el ID.')  
            return 

        connection= get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM PELICULA WHERE ID = ? AND USUARIO_ID = ?", (peli_eliminar, usuario.id_usuario))
        pelicula_eliminar = cursor.fetchone()
  
        if not pelicula_eliminar:
            print('No exite pelicula con ese ID')
            connection.close()
            return

        seguridad= input('Esta seguro de elimnar esta pelucula? S \ N').lower().strip()
        if seguridad == 'n':
            connection.close()
            return
        elif seguridad == 's': 
         cursor.execute("DELETE FROM PELICULA WHERE ID = ?", (peli_eliminar,))
         print(f'Pelicula  ID: {peli_eliminar} {pelicula_eliminar[1].title()} fue Eliminada de la Base de Datos')
         connection.commit()
         connection.close()

            

