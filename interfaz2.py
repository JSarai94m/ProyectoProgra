import tkinter as tk
from tkinter import ttk, messagebox

"""DEFINE UNA CLASE QUE HEREDA DE tk.Tk PARA ENCAPSULAR EL SISTEMA"""
class Ventana(tk.Tk):
    def _init_(self):  
        super()._init_()
        self.title("Sistema Bibliotecario")
        self.geometry("300x300")
        """EVITA QUE CAMBIE EL TAMAÑO DE LA VENTANA"""
        self.resizable(0, 0)
        
        """LLAMA AL METODO LOGIN PARA MOSTRAR LA VENTANA DE INICIO DE SESIÓN"""
        self.login()
        
    """PARA CREAR EL INICIO DE SESION CON ETIQUETAS, CAMPOS DE ENTRADA Y BOTON SE METIO TODO EN UN METODO"""
    def login(self):
        # Título del login
        lbltitulo = tk.Label(self, text='Inicio de Sesión', font=('Arial', 14, 'bold')) #EL FONT ES PARA EL TAMAÑO, TIPO DE LETRA Y QUE ESTE EN NEGRITA 
        lbltitulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10, sticky="n")

  # Etiqueta y campo de entrada para el usuario
        lbl_usuario = tk.Label(self, text="Usuario:")
        lbl_usuario.grid(row=1, column=0, padx=5, pady=10, sticky="e") # EL STICKY SIRVE PARA ALINEAR UN WIDGET, EN ESTE CASO SE ALIEA A LA DERECHA 

        self.txt_usuario = tk.Entry(self)
        self.txt_usuario.grid(row=1, column=1, padx=5, pady=10)

        lbl_contraseña = tk.Label(self, text="Contraseña:")
        lbl_contraseña.grid(row=2, column=0, padx=5, pady=10, sticky="e")

        self.txt_contraseña = tk.Entry(self, show="*")
        self.txt_contraseña.grid(row=2, column=1, padx=5, pady=10)

 # Botón de acceso, enlazado al método iniciar_sesion
        btn_acceso = tk.Button(self, text='Iniciar Sesión', command=self.iniciar_sesion)
        btn_acceso.grid(row=3, column=1, padx=5, pady=20)

    def iniciar_sesion(self):
        # Obtener los valores de usuario y contraseña
        usuario = self.txt_usuario.get().strip()
        contraseña = self.txt_contraseña.get().strip()

  # Validar si los campos no están vacíos
        if usuario and contraseña:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido al sistema, {usuario}.")
             
            """ OCULTA LA VENTANA DE INICIO DE SESION """
            self.withdraw()
            self.abrir_sistema()
        else:
            messagebox.showerror("Error", "Por favor ingrese un usuario y contraseña válidos.")

    def abrir_sistema(self):
        # Ventana principal del sistema bibliotecario
        ventana_principal = tk.Toplevel(self)
        ventana_principal.title("Sistema Bibliotecario - Ventana Principal")
        ventana_principal.geometry("800x800")
        ventana_principal.resizable(0, 0)

  # Labels y campos de entradas para gestionar libros
        tk.Label(ventana_principal, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(ventana_principal)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ventana_principal, text="Código:").grid(row=1, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(ventana_principal)
        self.codigo_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana_principal, text="Autor:").grid(row=2, column=0, padx=5, pady=5)
        self.autor_entry = tk.Entry(ventana_principal)
        self.autor_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(ventana_principal, text="Género:").grid(row=3, column=0, padx=5, pady=5)
        self.genero_entry = tk.Entry(ventana_principal)
        self.genero_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(ventana_principal, text="Estado:").grid(row=4, column=0, padx=5, pady=5)
        self.estado_entry = tk.Entry(ventana_principal)
        self.estado_entry.grid(row=4, column=1, padx=5, pady=5)
        
  # Botones                                   # EL WIDTH ES PARA ESPECIFICAR EL ANCHO DEL BOTON
        tk.Button(ventana_principal, text="Añadir", width=14, command=self.añadir).grid(row=5, column=0, padx=5, pady=15)
        tk.Button(ventana_principal, text="Modificar", width=14, command=self.modificar).grid(row=5, column=1, padx=5, pady=15)
        tk.Button(ventana_principal, text="Mostrar", width=14, command=self.mostrar).grid(row=5, column=2, padx=5, pady=15)
        tk.Button(ventana_principal, text="Eliminar", width=14, command=self.eliminar).grid(row=5, column=3, padx=5, pady=15)

        """MENU DESPLEGABLE EN EL BOTON BUSCAR"""
        self.criterio_busqueda = tk.StringVar(value="Código")
        opciones_busqueda = ttk.Combobox(ventana_principal, textvariable=self.criterio_busqueda, state="readonly", values=["Código", "Nombre", "Autor", "Género"])
        opciones_busqueda.grid(row=5, column=4, padx=5, pady=15)
        
        tk.Button(ventana_principal, text="Buscar", width=14, command=self.buscar).grid(row=5, column=5, padx=5, pady=15)

  #CONFIGURA LA TABLA PARA MOSTRAR LOS LIBROS
        self.tabla(ventana_principal)

# LA CREACION DE LA TABLA SE METIO DENTRO DE UN METODO
    def tabla(self, ventana_principal):
        # Crear el Treeview directamente en ventana_principal
        self.tree_lista_libros = ttk.Treeview(ventana_principal, columns=("codigo", "nombre", "autor", "genero", "estado"), show="headings")
        self.tree_lista_libros.grid(row=6, column=0, columnspan=6, padx=5, pady=5)

 # Encabezados de columnas
        self.tree_lista_libros.heading("codigo", text="Código")
        self.tree_lista_libros.heading("nombre", text="Nombre")
        self.tree_lista_libros.heading("autor", text="Autor")
        self.tree_lista_libros.heading("genero", text="Género")
        self.tree_lista_libros.heading("estado", text="Estado")
        
        """ AJUSTA EL TAMAÑO DE LAS COLUMNAS """
        self.tree_lista_libros.column("codigo", width=100)
        self.tree_lista_libros.column("nombre", width=200)
        self.tree_lista_libros.column("autor", width=150)
        self.tree_lista_libros.column("genero", width=150)
        self.tree_lista_libros.column("estado", width=100)

 # Lista para almacenar libros
        self.libros = []

# Métodos de los botones
    def añadir(self):
        # Obtener los datos de las entradas
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        autor = self.autor_entry.get()
        genero = self.genero_entry.get()
        estado = self.estado_entry.get()

        if codigo and nombre and autor and genero and estado:
            libro = (codigo, nombre, autor, genero, estado)
            self.libros.append(libro)
            self.mostrar()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    def modificar(self):
        # sirve para obtener el código del libro a modificar
        codigo = self.codigo_entry.get()
        for i, libro in enumerate(self.libros):
            if libro[0] == codigo:
                nuevo_nombre = self.nombre_entry.get()
                nuevo_autor = self.autor_entry.get()
                nuevo_genero = self.genero_entry.get()
                nuevo_estado = self.estado_entry.get()

                if nuevo_nombre and nuevo_autor and nuevo_genero and nuevo_estado:
                    # Modificar el libro
                    self.libros[i] = (codigo, nuevo_nombre, nuevo_autor, nuevo_genero, nuevo_estado)
                    self.mostrar()
                    self.limpiar_campos()
                    return
                else:
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return
        messagebox.showerror("Error", "No se encontró el libro con ese código")

    def mostrar(self):
        # Limpiar la tabla
        for row in self.tree_lista_libros.get_children():
            self.tree_lista_libros.delete(row)
            
# Insertar los libros en la tabla
        for libro in self.libros:
            self.tree_lista_libros.insert("", "end", values=libro)

    def eliminar(self):
        # Obtener el código del libro a eliminar
        codigo = self.codigo_entry.get()
        for i, libro in enumerate(self.libros):
            if libro[0] == codigo:
                del self.libros[i]
                self.mostrar()
                self.limpiar_campos()
                return
        messagebox.showerror("Error", "No se encontró el libro con ese código")

    def buscar(self):
        # Buscar libro por código  # Obtener el criterio de búsqueda seleccionado
        criterio = self.criterio_busqueda.get().lower()
        # Obtener el valor ingresado en el campo de entrada del boton buscar
        valor = self.codigo_entry.get()


        if not valor:
            messagebox.showerror("Error", "Debe ingresar un valor para buscar.")
            return
        
# Buscar el libro en la lista de libros según el criterio seleccionado
        for libro in self.libros:
            # Si el criterio es "código" y el valor coincide con el código del libro, mostrar el resultado
            if criterio == "código" and libro[0] == valor:
                self.mostrar_resultado(libro)   # Mostrar los detalles del libro encontrado
                return
            
         # Si el criterio es "nombre" y el valor coincide con el nombre del libro, mostrar el resultado
            elif criterio == "nombre" and libro[1] == valor:
                self.mostrar_resultado(libro)
                return
        # Si el criterio es "autor" y el valor coincide con el autor del libro, mostrar el resultado
            elif criterio == "autor" and libro[2] == valor:
                self.mostrar_resultado(libro)
                return
      # Si el criterio es "género" y el valor coincide con el género del libro, mostrar el resultado
            elif criterio == "género" and libro[3] == valor:
                self.mostrar_resultado(libro)
                return
# Si no se encuentra ningún libro que coincida con el criterio y el valor ingresado se muestra el siguiente mensaje
        messagebox.showerror("Error", "No se encontró el libro con ese criterio.")

    def mostrar_resultado(self, libro):
        # Mostrar los datos del libro en las entradas
        self.nombre_entry.delete(0, tk.END)
        self.nombre_entry.insert(0, libro[1])
        self.autor_entry.delete(0, tk.END)
        self.autor_entry.insert(0, libro[2])
        self.genero_entry.delete(0, tk.END)
        self.genero_entry.insert(0, libro[3])
        self.estado_entry.delete(0, tk.END)
        self.estado_entry.insert(0, libro[4])

    def limpiar_campos(self):
        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.estado_entry.delete(0, tk.END)

# SIRVE PARA QUE EL CÓDIGO SE EJECUTE CORRECTAMENTE
def main():
    app = Ventana()
    app.mainloop()

if __name__ == "_main_":  # Corregido el nombre de la condición principal
    main()