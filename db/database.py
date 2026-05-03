import sqlite3
DB_NAME = "db/favorite_movies.db" 

def get_connection ():
    try:
        connection = sqlite3.connect(DB_NAME)
        return connection
    except sqlite3.Error as e :
        print({e})
        return None

def create_tables ():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS Usuario( ID INTEGER PRIMARY KEY , NOMBRE_COMPLETO  TEXT NOT NULL)")
    

    cursor.execute("CREATE TABLE IF NOT EXISTS Pelicula ( ID INTEGER PRIMARY KEY, TITULO TEXT, GENERO TEXT, ANIO INTEGER , USUARIO_ID INTEGER, FOREIGN KEY (USUARIO_ID) REFERENCES Usuario (ID) )")
    connection.commit()
    connection.close()

def registrar_usuario_db(usuario):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO Usuario (ID, NOMBRE_COMPLETO) VALUES (?, ?)", 
        (usuario.id_usuario, usuario.nombre_completo.title())
    ) 
    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("--Creacion exitosa--")
