import tkinter as tk
from tkinter import ttk, messagebox

class SistemaBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Bibliotecario")

        # Ventana de inicio de sesión
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Inicio de Sesión")
        self.login_window.geometry("300x150")

        # Etiqueta y campo de entrada para el nombre de usuario
        tk.Label(self.login_window, text="Usuario:").grid(row=0, column=0, padx=10, pady=10)
        self.usuario_entry = tk.Entry(self.login_window)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10)

        # Etiqueta y campo de entrada para la contraseña
        tk.Label(self.login_window, text="Contraseña:").grid(row=1, column=0, padx=10, pady=10)
        self.contraseña_entry = tk.Entry(self.login_window, show="*")
        self.contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botón para realizar el inicio de sesión
        tk.Button(self.login_window, text="Iniciar sesión", command=self.iniciar_sesion).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def iniciar_sesion(self):
        # los valores de los campos de usuario y contraseña, y eliminar espacios adicionales
        usuario = self.usuario_entry.get().strip()
        contraseña = self.contraseña_entry.get().strip()

        # Validar si los campos no están vacíos
        if usuario and contraseña:
            messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido al sistema, {usuario}.")
            self.login_window.destroy()  # Cerrar la ventana de inicio de sesión
            self.abrir_sistema()  # Abrir la ventana principal del sistema
        else:
            messagebox.showerror("Error", "Por favor ingrese un usuario y contraseña válidos.")

    def abrir_sistema(self):
        # ventana principal del sistema bibliotecario
        ventana_principal = tk.Toplevel(self.root)
        ventana_principal.title("Sistema Bibliotecario - Ventana Principal")
        ventana_principal.geometry("600x400")

        # Labels y entradas para gestionar libros
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

        # Botones
        tk.Button(ventana_principal, text="Añadir", command=self.añadir).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(ventana_principal, text="Modificar", command=self.modificar).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(ventana_principal, text="Mostrar", command=self.mostrar).grid(row=5, column=2, padx=5, pady=5)
        tk.Button(ventana_principal, text="Eliminar", command=self.eliminar).grid(row=5, column=3, padx=5, pady=5)
        tk.Button(ventana_principal, text="Buscar", command=self.buscar).grid(row=5, column=4, padx=5, pady=5)

        # Tabla
        self.tabla = ttk.Treeview(ventana_principal, columns=("codigo", "nombre", "autor", "genero", "estado"), show="headings")
        self.tabla.grid(row=6, column=0, columnspan=5, padx=5, pady=5)

        # Encabezados de la tabla
        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("autor", text="Autor")
        self.tabla.heading("genero", text="Categoría")
        self.tabla.heading("estado", text="Estado")

        # Lista para almacenar libros
        self.libros = []

    # Funciones para cada botón
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
            self.mostrar()  # Mostrar la tabla después de añadir
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
                    self.mostrar()  # Actualizar la tabla
                    self.limpiar_campos()
                    return
                else:
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return
        messagebox.showerror("Error", "No se encontró el libro con ese código")

    def mostrar(self):
        # Limpiar la tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Insertar los libros en la tabla
        for libro in self.libros:
            self.tabla.insert("", "end", values=libro)

    def eliminar(self):
        # Obtener el código del libro a eliminar
        codigo = self.codigo_entry.get()
        for i, libro in enumerate(self.libros):
            if libro[0] == codigo:
                del self.libros[i]
                self.mostrar()  # Actualizar la tabla
                self.limpiar_campos()
                return
        messagebox.showerror("Error", "No se encontró el libro con ese código")

    def buscar(self):
        # Buscar libro por código
        codigo = self.codigo_entry.get()
        for libro in self.libros:
            if libro[0] == codigo:
                # Mostrar los datos del libro en las entradas
                self.nombre_entry.delete(0, tk.END)
                self.nombre_entry.insert(0, libro[1])
                self.autor_entry.delete(0, tk.END)
                self.autor_entry.insert(0, libro[2])
                self.genero_entry.delete(0, tk.END)
                self.genero_entry.insert(0, libro[3])
                self.estado_entry.delete(0, tk.END)
                self.estado_entry.insert(0, libro[4])
                return
        messagebox.showerror("Error", "No se encontró el libro con ese código")

    def limpiar_campos(self):
        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.genero_entry.delete(0, tk.END)
        self.estado_entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
sistema = SistemaBiblioteca(root)
root.mainloop()
