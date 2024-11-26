
import sqlite3
from consultas import Consultas
from libros_usuarios import Libros
from libros_usuarios import Usuarios

class Funciones :
    
    """
    Clase que contiene métodos estáticos para gestionar operaciones con la base de datos,incluyendo conexión, 
    creación de tablas, inicio de sesión, y operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los libros.
    """
    
    @staticmethod
    def conexion():
        """
        Establece la conexión con la base de datos y crea un cursor.
        """
        conexion = sqlite3.connect('database.db')  
        cursor = conexion.cursor()
        return conexion,cursor
    
    @staticmethod
    def conexionBD():
        """
        Crea las tablas de usuarios y libros si no existen en la base de datos.
        Utiliza las sentencias predefinidas en la clase Consultas.
        """
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.tabla_usuario)
        cursor.execute(Consultas.tabla_libros)
        
    @staticmethod    
    def iniciar_sesion(nombre,contraseña):
        """
        Verifica si un usuario existe en la base de datos y devuelve una lista de registros 
        que coinciden con los datos proporcionados.
        """
        conexion,cursor = Funciones.conexion()  
        cursor.execute(Consultas.Usuario,(nombre,contraseña))
        return cursor.fetchall()
        
    @staticmethod   
    def mostrar():
        """
        Muestra todos los libros de la base de datos ordenados por categoría.
        """
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.Ordenar)
        return cursor.fetchall() 
    
    @staticmethod 
    def añadir(codigo,titulo,autor,categoria):
        """
        Agrega un nuevo libro a la base de datos.
        """
        conexion,cursor = Funciones.conexion()
        # Instancia de la clase Libros.
        libro = Libros(codigo,titulo,autor,categoria)
        # Se pasa la información del libro.
        cursor.execute(Consultas.Insert,(libro.informacion_libro()))
        conexion.commit()
        
    @staticmethod    
    def modificar(codigo,titulo,autor,categoria):
        """
        Modifica un libro existente en la base de datos.
        """
        conexion,cursor = Funciones.conexion()
        # Instancia de la clase Libros.
        libro = Libros(codigo,titulo,autor,categoria)
        # Actualiza con los nuevos datos.
        cursor.execute(Consultas.Update,(titulo, autor, categoria, codigo))
        conexion.commit()
        
    @staticmethod    
    def eliminar(codigo):
        """
        Elimina un libro de la base de datos.
        """
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.Delete,(codigo,))
        conexion.commit ()   
        
    @staticmethod           
    def buscar(criterio, valor):
        """
        Busca libros en la base de datos según un criterio y un valor.
        Devuelve una lista de libros que coinciden con la búsqueda.
        """
        conexion,cursor = Funciones.conexion()
        # Inserta dinámicamente el criterio en la consulta.
        query = Consultas.Buscar.format(criterio)  
        # Utiliza LIKE para búsquedas parciales.
        cursor.execute(query, (f"%{valor}%",)) 
        return cursor.fetchall()
    
    
    
    