from models.pelicula import Pelicula
from models.usuario import Usuario


class MisPeliculasFavoritas:
    def __init__(self,nombre):
        self.nombre = nombre

    def agregar_pelicula(self,usuario,pelicula):
        usuario.mis_fav.append(pelicula)
        return f'La película {pelicula.titulo} fue agregada con éxito'
    
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
        
        
       

        

         

    
