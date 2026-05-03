class Usuario :
    def __init__(self,nombre_completo,id_usuario):
        self.nombre_completo = nombre_completo
        self.id_usuario = id_usuario
        self.mis_fav = []
    

    def __str__(self):
        return f' Bienvenido {self.nombre_completo.title()} Numero de ID: {self.id_usuario}'

    