import sqlite3 

# Conectar a la base de datos  
conexion = sqlite3.connect('Basado_Usuario.db')   
conexion_cursor = conexion.cursor()

# Crear la tabla, si no existe  
conexion_cursor.execute("""  
CREATE TABLE IF NOT EXISTS Usuarios (  
    ID_usuario INTEGER PRIMARY KEY,  
    Nombre TEXT,  
    Contraseña TEXT  
)  
""")  
print("Tabla Creada con éxito")  


# Comprobar si el ID ya existe  
id_usuario = 1
conexion_cursor.execute("SELECT * FROM Usuarios WHERE ID_usuario = ?", (id_usuario,))  
if conexion_cursor.fetchone() is None:  
    # Solo inserta si no existe  
    conexion_cursor.execute("INSERT INTO Usuarios VALUES (?, 'Lucas', '237679')", (id_usuario,))  
    print("Usuario insertado con éxito.")  
else:  
    print("El ID ya existe. No se realizó la inserción.")
# Confirmar los cambios
conexion.commit()

conexion.close()

 




































      



