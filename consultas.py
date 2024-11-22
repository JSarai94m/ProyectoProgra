
# sentencias SQL en formato string

""" Crea las tablas si no existen y declaran variables con las consultas a usar con la base de datos"""
class Consultas:
    
    tabla_usuario = '''
                    CREATE TABLE IF NOT EXISTS Usuarios (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre TEXT NOT NULL,
                        Contraseña TEXT NOT NULL
                    )
                '''
                
    tabla_libros = '''
                    CREATE TABLE IF NOT EXISTS Libros (
                        Codigo TEXT PRIMARY KEY,
                        Titulo TEXT NOT NULL,
                        Autor TEXT NOT NULL,
                        Categoria TEXT NOT NULL
                    )
                '''
                
    Usuario = "SELECT Nombre, Contraseña FROM Usuarios WHERE Nombre = ? AND Contraseña = ?"
    
    Insert = "INSERT INTO Libros (Codigo, Titulo, Autor, Categoria) VALUES (?, ?, ?, ?)"
    
    Select = "SELECT *FROM Libros"
    
    Update = "UPDATE Libros SET Titulo = ?, Autor = ?, Categoria = ? WHERE Codigo = ?"
    
    Delete = "DELETE FROM Libros WHERE Codigo = ?"
    
    Buscar = "SELECT * FROM Libros WHERE {} LIKE ?"
    
    Ordenar = "SELECT * FROM Libros ORDER BY Categoria ASC"
  
    
    
    
    
   
    
    
 
 