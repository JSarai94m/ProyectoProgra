
import sqlite3
from consultas import Consultas
from libros_usuarios import Libros,Usuarios

class Funciones :  
    
    """Hace la conexion con la base de datos, crea el cursor ,cada funcion a usar se conecta con la base de datos 
     y ejecuta las consultas correspondientes"""
    @staticmethod
    def conexion():
        
        conexion = sqlite3.connect('database.db')  
        cursor = conexion.cursor()
        return conexion,cursor
    @staticmethod
    def conexionBD():
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.tabla_usuario)
        cursor.execute(Consultas.tabla_libros)
    @staticmethod    
    def iniciar_sesion(nombre,contraseña):
        conexion,cursor = Funciones.conexion()  
        cursor.execute(Consultas.Usuario,(nombre,contraseña))
        return cursor.fetchall()
        
    @staticmethod   
    def mostrar():
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.Ordenar)
        return cursor.fetchall() 
    @staticmethod 
    def añadir(codigo,titulo,autor,categoria):
        conexion,cursor = Funciones.conexion()
        libro = Libros(codigo,titulo,autor,categoria)
        cursor.execute(Consultas.Insert,(libro.informacion_libro()))
        conexion.commit()
        
    @staticmethod    
    def modificar(codigo,titulo,autor,categoria):
        conexion,cursor = Funciones.conexion()
        libro = Libros(codigo,titulo,autor,categoria)
        cursor.execute(Consultas.Update,(titulo, autor, categoria, codigo))
        conexion.commit()
    @staticmethod    
    def eliminar(codigo):
        conexion,cursor = Funciones.conexion()
        cursor.execute(Consultas.Delete,(codigo,))
        conexion.commit ()   
    @staticmethod           
    def buscar(criterio, valor):
        conexion,cursor = Funciones.conexion()
        query = Consultas.Buscar.format(criterio)  
        cursor.execute(query, (f"%{valor}%",)) 
        return cursor.fetchall()
    
    
    
    