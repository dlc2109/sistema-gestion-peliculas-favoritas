from models.pelicula import Pelicula
from models.usuario import Usuario


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
        usuario.mis_fav.append(nueva_peli)
        return f'La película {nueva_peli.titulo} fue agregada con éxito'
    
    def listar_peliculas(self,Usuario):
        if not Usuario.mis_fav:
            print('No hay peliculas guardadas')
            return
        print(f' Lista de Favoritos de {Usuario.nombre_completo}')
        for p in Usuario.mis_fav:
            print(p)

    def eliminar(self,Usuario):
      self.listar_peliculas(Usuario)
      if not  Usuario.mis_fav:
        return
      try:
        peli_eliminar = int(input('Ingrese ID de la pelicula a eliminar: '))
        encontrado = False
        for p in Usuario.mis_fav:
         if peli_eliminar == p.id_peli:
            encontrado= True
            seguridad = input(' Esta seguro  de eliminar esta pelicula?: S \ N ').lower().strip()
            if seguridad == 's': 
                Usuario.mis_fav.remove(p)
                print(f"Película '{p.titulo}' eliminada con éxito.")
            else:
              print('Operacion cancelada')
              break
        if not encontrado:
            print('No se encontro la pelicula')   
      except ValueError:
       print(' Error: Ingresa un número válido para el ID.')    
        
        
       

        

         

    
