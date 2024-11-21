import sqlite3
conexion = sqlite3.connect('Basado_Usuario.db')
conexion_cursor = conexion.cursor()

def lista_libros(Basado_Usuario):
 
  try:
      #Consulta que listara el titulo de cada libro
      consulta= "SELECT Titulo FROM Libros"
      conexion_cursor.execute(consulta)
      Titulos = [Titulo[0] for Titulo in conexion_cursor.fetchall()]
      conexion.commit
      conexion.close
      return Titulos
  except sqlite3.Error as e:
        print("Error en su búsqueda")
Libros_titulos= lista_libros('Basado_Usuario.db')
if Libros_titulos:
    print("Titulos de Libros")
    for Titulo in Libros_titulos:
        print("---------------------------------------------------------------------------")
        print(Titulo)
else: print("No se encontraron más Titulos de Libros")
print("****************")


#Eliminar un libro de la base de datos
def Borrar_libro(Codigo, Basado_Usuario):
    conexion_cursor = conexion.cursor()
    consulta= "DELETE FROM Libros WHERE codigo= "+ Codigo
    conexion_cursor.execute(consulta)
    conexion.commit()
    
Borrar_libro("NOV202")
Eliminar_libro(Borrar_libro)
conexion.close()












  

  
   
