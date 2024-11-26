class Mensaje:
    """
    Clase que contiene todos los mensajes de texto que se muestran en la interfaz gráfica.
    """
    
    # Mensaje de inicialización de la base de datos
    inicializar_bd = 'Error al inicializar la base de datos'
        
   
        
    # Mensajes generales
    llenar_campos = 'Todos los campos son obligatorios' 
    busqueda = 'No se encontró ningún libro con ese código'
        
    # Mensajes para inicio de sesión
    login_exitoso = 'Bienvenido al sistema'    
    error_usuario = 'El usuario no esta permitido para acceder al sistema'
    error_login  = 'Error al iniciar sesión'
    campos_faltantes = 'Por favor ingrese un usuario y contraseña ' 
        
     # Mensaje para salir del programa   
    salir = '¿Está seguro de que desea salir del programa?'
        
     # Mensajes relacionados con mostrar libros  
    error_mostrar = 'No se pudieron cargar los registros'
        
     # Mensajes relacionados con añadir un libro   
    exito_añadir = 'Libro añadido correctamente'
    error_existencia = 'El código ya existe. Por favor, use un código único' 
    error_añadir = 'No se pudo añadir el libro'
        
    # Mensajes relacionados con eliminar un libro
    selec_eliminar = 'Por favor, seleccione un libro o introduzca su código'
    decision_eliminar = '¿Está seguro de que desea eliminar el libro seleccionado?'
    cancelar_eliminacion = 'La eliminación fue cancelada.'
    eliminar_libro = 'Libro eliminado correctamente'
    error_eliminar = 'No se pudo eliminar el libro'
        
    # Mensaje relacionados con modificar un libro 
    decision_modificar = '¿Está seguro de que desea modificar el libro seleccionado?'
    exito_modificar = 'Libro modificado correctamente'
    error_modificar = 'No se pudo modificar el libro'
    cancelar_modificacion = 'La modificación fue cancelada'    
       
    # Mensajes relacionados con la búsqueda de libros    
    buscar = 'Por favor ingrese un valor para buscar en {criterio}'
    informacion = 'No se encontraron libros que coincidan con la búsqueda'
    error_busqueda = 'Error al realizar la búsqueda'