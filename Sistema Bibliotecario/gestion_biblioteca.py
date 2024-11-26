from tkinter import messagebox
from funciones import Funciones
from mensajes import Mensaje
from sqlite3 import IntegrityError

class Gestionar:
    """
    Clase que gestiona las operaciones con la base de datos, vinculadas a la interfaz gráfica.
    Maneja la lógica para la conexión, inicio de sesión y operaciones CRUD sobre los libros,
    mostrando mensajes de éxito o error mediante 
    """
    
    @staticmethod
    def conexionBD():
        """
        Inicializa la base de datos creando las tablas si no existen.
        Muestra un mensaje de error si ocurre algún problema.
        """
        try:
            Funciones.conexionBD()
        except Exception as e:
            messagebox.showerror("ERROR", f"{Mensaje.inicializar_bd}: {e}")

    @staticmethod
    def iniciar_sesion(usuario, contraseña):
        """
        Verifica si los datos de inicio de sesión son válidas.
        Devuelve True si el inicio de sesión es exitoso, False en caso contrario.
        """
        if usuario and contraseña:  
            try:
                resultado = Funciones.iniciar_sesion(usuario, contraseña)
                if resultado:
                    nombre_db, contrasena_db = resultado[0]
                    if nombre_db == usuario and contrasena_db == contraseña:
                        messagebox.showinfo("Inicio de sesión exitoso", Mensaje.login_exitoso)
                        return True
                    else:
                        messagebox.showerror("Error", Mensaje.error_usuario)
                        return False
                else:
                    messagebox.showerror("Error", Mensaje.error_usuario)
                    return False
            except Exception as e:
                messagebox.showerror("Error", f"{Mensaje.error_login}: {e}")
                return False
        else:
            messagebox.showerror("Error", Mensaje.campos_faltantes)
            return False
        

    @staticmethod
    def mostrar(tree):
        """
       Muestra todos los libros almacenados en la base de datos en un widget tipo TreeView.
       tree: Widget TreeView donde se mostrará la información.
       """
        try:
            for row in tree.get_children():
                tree.delete(row)
            libros = Funciones.mostrar()
            for libro in libros:
                tree.insert("", "end", values=libro)
        except Exception as e:
            messagebox.showerror("Error", f"{Mensaje.error_mostrar}: {e}")

    @staticmethod
    def añadir(codigo, titulo, autor, categoria):
        """
        Añade un nuevo libro a la base de datos.
        Devuelve True si la operación es exitosa, False en caso de error.
        """
        try:
            if codigo and titulo and autor and categoria:
                Funciones.añadir(codigo, titulo, autor, categoria)
                messagebox.showinfo("Éxito", Mensaje.exito_añadir)
                return True
            else:
                messagebox.showerror("Error", Mensaje.llenar_campos)
                return False
        except IntegrityError:
            messagebox.showerror("Error", Mensaje.error_existencia)
            return False
        except Exception as e:
            messagebox.showerror("Error", f"{Mensaje.error_añadir}: {e}")
            return False

    @staticmethod
    def modificar(codigo, titulo, autor, categoria):
        """
        Modifica los datos de un libro existente.
        Devuelve True si la operación es exitosa, False si es cancelada o falla.
        """
        try:
            if codigo and titulo and autor and categoria:
                confirmacion = messagebox.askyesno("Confirmación", Mensaje.decision_modificar)
                if confirmacion:
                    Funciones.modificar(codigo, titulo, autor, categoria)
                    messagebox.showinfo("Éxito", Mensaje.exito_modificar)
                    return True
                else:
                    messagebox.showinfo("Cancelado", Mensaje.cancelar_modificacion)
                    return False
            else:
                messagebox.showerror("Error", Mensaje.llenar_campos)
                return False
        except Exception as e:
            messagebox.showerror("Error", f"{Mensaje.error_modificar}: {e}")
            return False
        

    @staticmethod
    def eliminar(codigo):
        """
        Elimina un libro de la base de datos.
        Devuelve True si la operación es exitosa, False si es cancelada o falla.
        """
        try:
            if codigo:
                confirmacion = messagebox.askyesno("Confirmación", Mensaje.decision_eliminar)
                if confirmacion:
                    Funciones.eliminar(codigo)
                    messagebox.showinfo("Éxito", Mensaje.eliminar_libro)
                    return True
                else:
                    messagebox.showinfo("Cancelado", Mensaje.cancelar_eliminacion)
                    return False
            else:
                messagebox.showerror("Error", Mensaje.selec_eliminar)
                return False
        except Exception as e:
            messagebox.showerror("Error", f"{Mensaje.error_eliminar}: {e}")
            return False

    @staticmethod
    def buscar(tree, criterio, valor):
        """
        Busca libros en la base de datos según un criterio y valor, y los muestra en un TreeView.
        """
        try:
            
            for row in tree.get_children():
                tree.delete(row)
    
            
            resultados = Funciones.buscar(criterio, valor)
            if resultados:
                for libro in resultados:
                    tree.insert("", "end", values=libro)
            else:
                messagebox.showinfo("Búsqueda", Mensaje.informacion)
        except Exception as e:
            messagebox.showerror("Error", f"{Mensaje.error_busqueda}: {e}")
