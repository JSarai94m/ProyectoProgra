class Libros: 
    """
    Clase que representa un libro con atributos como código, título, autor y categoría.
    """
    def __init__(self,codigo,titulo,autor,categoria):
        """ Constructor para inicializar los atributos de un libro"""
        
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
    
    # retornar la informacion del libro 
    def informacion_libro (self):
        """
        Retorna toda la información del libro como una tupla.
        """
        return self.__codigo,self.__titulo, self.__autor, self.__categoria
    
    

        
