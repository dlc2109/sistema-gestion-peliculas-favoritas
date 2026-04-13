class Pelicula :
    def __init__(self,titulo,genero,anio,id_peli):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.id_peli = id_peli

    def __str__ (self):
            return f' Titulo: {self.titulo} | Genero: {self.genero} | Anio: {self.anio} | ID: {self.id_peli} '

   
        