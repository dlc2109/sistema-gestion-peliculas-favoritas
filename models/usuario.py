class Usuario :
    def __init__(self,nombre_completo):
        self.nombre_completo = nombre_completo
        self.mis_fav = []
    

    def __str__(self):
        return f' Bienvenido {self.nombre_completo}'

    