import sqlite3 
conexion = sqlite3.connect('Basado_Usuario.db')   
conexion_cursor = conexion.cursor()

#Crear la tabla de libros
conexion_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Libros (
      Codigo TEXT PRIMARY KEY  ,
      Titulo TEXT  ,
      Autor TEXT ,
      Categoria TEXT
    )
  """)
#Comprobar si el codigo ya existe
conexion_cursor.execute("SELECT * FROM Libros WHERE Codigo = 'POE005'" )
if conexion_cursor.fetchone() is None:
        #Solo inserta Datos si no existe 
    conexion_cursor.execute("INSERT INTO Libros (Codigo, Titulo, Autor, Categoria) VALUES (?,?,?,?)",('POE005','Antalogía Poética ','Federico García Lorca','Poesía'))
    print ("Libro agregado con exito")
else:
     print("El codigo 'POE005' ya existe en la tabla")
#Guardar datos y cerrar conexion 
conexion.commit()
conexion.close()









    
