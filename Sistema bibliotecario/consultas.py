
class Consultas:
    """
    Clase que contiene consultas SQL predefinidas para interactuar con una base de datos.
    """
    
    # sentencia SQL para crear la tabla Usuarios si no existe (ID, Nombre, Contraseña).
    tabla_usuario = '''
                    CREATE TABLE IF NOT EXISTS Usuarios (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre TEXT NOT NULL,
                        Contraseña TEXT NOT NULL
                    )
                '''
      
    # Sentencia SQL para crear la tabla Libros si no existe (Codigo, Titulo, Autor, Categoria).
    tabla_libros = '''
                    CREATE TABLE IF NOT EXISTS Libros (
                        Codigo TEXT PRIMARY KEY,
                        Titulo TEXT NOT NULL,
                        Autor TEXT NOT NULL,
                        Categoria TEXT NOT NULL
                    )
                '''
              
    # Consulta para verificar la existencia de un usuario por Nombre y Contraseña.            
    Usuario = "SELECT Nombre, Contraseña FROM Usuarios WHERE Nombre = ? AND Contraseña = ?"
    
    # Insertar un nuevo libro en la tabla Libros.
    Insert = "INSERT INTO Libros (Codigo, Titulo, Autor, Categoria) VALUES (?, ?, ?, ?)"
    
    # Seleccionar todos los registros de la tabla Libros.
    Select = "SELECT *FROM Libros"
    
    # Actualizar un libro identificado por su Codigo.
    Update = "UPDATE Libros SET Titulo = ?, Autor = ?, Categoria = ? WHERE Codigo = ?"
    
    # Eliminar un libro identificado por su Codigo.
    Delete = "DELETE FROM Libros WHERE Codigo = ?"
    
    # Buscar libros en una columna específica usando un patrón.
    Buscar = "SELECT * FROM Libros WHERE {} LIKE ?"
    
    # Ordenar los libros por la columna Categoria en orden ascendente.
    Ordenar = "SELECT * FROM Libros ORDER BY Categoria ASC"
  
    
    
    
    
   
    
    
 
 