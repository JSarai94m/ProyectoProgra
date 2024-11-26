
import tkinter as tk
from tkinter import ttk, messagebox
from gestion_biblioteca import Gestionar
from mensajes import Mensaje

class Ventana(tk.Tk):
    """
    Clase principal de la interfaz gráfica para el sistema bibliotecario.
    Contiene funcionalidades para iniciar sesión, gestionar libros (añadir, modificar, eliminar, buscar) 
    y navegar entre las interfaces de inicio de sesión y el sistema.
    """
   
    def __init__(self):
        """
        Constructor de la clase Ventana.
        Configura las propiedades iniciales de la ventana y carga la interfaz de inicio de sesión.
        """
        super().__init__()
        self.title("Sistema Bibliotecario")
        self.geometry("400x400")
        self.resizable(0, 0)
        # Conexión inicial con la base de datos.
        Gestionar.conexionBD()  
        self.interfaz_login()
        self.config(bg="honeydew3")
        self.iconbitmap("sesion.ico")
    
    def interfaz_login(self):
            """
            Crea la interfaz de inicio de sesión, permitiendo al usuario ingresar sus datos.
            """
            
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=2)
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(4, weight=1)
            
            # Título de la ventana
            lbltitulo = tk.Label(self, text='Inicio de sesión', bg="honeydew3", font=('Arial', 14, 'bold'))
            lbltitulo.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        
            # # Etiqueta y campo de entrada para el usuario
            lbl_usuario = tk.Label(self, text="Usuario:", bg="honeydew3", font=("Helvetica", 12, "bold"))
            lbl_usuario.grid(row=1, column=0, padx=10, pady=10, sticky="e")
            self.txt_usuario = tk.Entry(self, width=25)
            self.txt_usuario.grid(row=1, column=1, padx=5, pady=10, sticky="w")
        
            # Etiqueta y campo de entrada para la contraseña
            lbl_contraseña = tk.Label(self, text="Contraseña:", bg="honeydew3", font=("Helvetica", 12, "bold"))
            lbl_contraseña.grid(row=2, column=0, padx=10, pady=5, sticky="e")
            self.txt_contraseña = tk.Entry(self, show="*", width=25)
            self.txt_contraseña.grid(row=2, column=1, padx=5, pady=10, sticky="w")
        
            # Botón de iniciar_sesion
            btn_acceso = tk.Button(self, text='Iniciar Sesión', command=self.iniciar_sesion, bg="sky blue", font=("Arial", 11, "bold"))
            btn_acceso.grid(row=3, column=0, columnspan=2, padx=5, pady=50)


    def interfaz_sistema(self):
        """
       Crea la interfaz principal del sistema bibliotecario después de iniciar sesión.
       Permite gestionar libros: añadir, modificar, eliminar, mostrar y buscar.
       """
        
        ventana_principal = tk.Toplevel(self)
        ventana_principal.title("Sistema Bibliotecario - Ventana Principal")
        ventana_principal.resizable(0, 0)
        ventana_principal.geometry("1000x700")
        ventana_principal.config(bg="gray64")
        ventana_principal.iconbitmap("sesion.ico")

        # etiquetas y campos de entrada para la gestion de los libros
        tk.Label(ventana_principal, text="Codigo:", bg="gray64", font=("Helvetica", 10, "bold")).grid(row=0, column=0, padx=5, pady=10)
        self.codigo_entry = tk.Entry(ventana_principal)
        self.codigo_entry.grid(row=0, column=1, padx=5, pady=10, columnspan=2, sticky="ew")

        tk.Label(ventana_principal, text="Titulo:", bg="gray64", font=("Helvetica", 10, "bold")).grid(row=1, column=0, padx=5, pady=10)
        self.titulo_entry = tk.Entry(ventana_principal)
        self.titulo_entry.grid(row=1, column=1, padx=5, pady=10, columnspan=2, sticky="ew")

        tk.Label(ventana_principal, text="Autor:", bg="gray64", font=("Helvetica", 10, "bold")).grid(row=2, column=0, padx=5, pady=10)
        self.autor_entry = tk.Entry(ventana_principal)
        self.autor_entry.grid(row=2, column=1, padx=5, pady=10, columnspan=2, sticky="ew")

        tk.Label(ventana_principal, text="Categoria:", bg="gray64", font=("Helvetica", 10, "bold")).grid(row=3, column=0, padx=5, pady=10)
        self.categoria_entry = tk.Entry(ventana_principal)
        self.categoria_entry.grid(row=3, column=1, padx=5, pady=10, columnspan=2, sticky="ew")

        # Botones de gestión
        tk.Button(ventana_principal, text="Añadir", width=14, command=self.añadir).grid(row=5, column=0, padx=5, pady=15)
        tk.Button(ventana_principal, text="Modificar", width=14, command=self.modificar).grid(row=5, column=1, padx=5, pady=15)
        tk.Button(ventana_principal, text="Mostrar", width=14, command=self.mostrar).grid(row=5, column=2, padx=5, pady=15)
        tk.Button(ventana_principal, text="Eliminar", width=14, command=self.eliminar).grid(row=5, column=3, padx=5, pady=15)
        tk.Button(ventana_principal, text="Salir", width=14, command=self.salir).grid(row=5, column=4, padx=5, pady=15)
        tk.Button(ventana_principal, text="Buscar", width=14, command=self.buscar).grid(row=5, column=5, padx=5, pady=15)

        # ComboBox de criterios de búsqueda
        self.opciones_busqueda = ttk.Combobox(ventana_principal, state="readonly", values=["Codigo", "Titulo", "Autor", "Categoria"])
        self.opciones_busqueda.grid(row=5, column=6, padx=5, pady=15)
        self.opciones_busqueda.bind("<<ComboboxSelected>>", self.campos_busqueda)
        self.opciones_busqueda.set("Buscar por...")
        

        # Tabla de resultados
        self.tabla = ttk.Treeview(ventana_principal, columns=("Codigo", "Titulo", "Autor", "Categoria"), show="headings")
        self.tabla.grid(row=6, column=0, columnspan=6, padx=10, pady=20, sticky="nsew")

        # Encabezados de columnas
        self.tabla.heading("Codigo", text="Codigo")
        self.tabla.heading("Titulo", text="Titulo")
        self.tabla.heading("Autor", text="Autor")
        self.tabla.heading("Categoria", text="Categoria")

        # Configuracion de las columnas
        self.tabla.column("Codigo", width=100)
        self.tabla.column("Titulo", width=300)
        self.tabla.column("Autor", width=200)
        self.tabla.column("Categoria", width=200)

        # Vincula la selección de la tabla
        self.tabla.bind('<ButtonRelease-1>', self.seleccionar_registro)

        # Ajuste de filas
        ventana_principal.rowconfigure(6, weight=1)
        
    
    def ocultar_campos(self, criterio):
        """
        Oculta todos los campos y muestra solo aquellos relacionados con el criterio de busqueda seleccionado.
        """
        # Diccionario de campos y etiquetas
        campos = {
            "Codigo": (self.lbl_codigo, self.codigo_entry),
            "Titulo": (self.lbl_titulo, self.titulo_entry),
            "Autor": (self.lbl_autor, self.autor_entry),
            "Categoria": (self.lbl_categoria, self.categoria_entry),}
    
        # Ocultar todos los campos
        for label, entry in campos.values():
            label.grid_remove()
            entry.grid_remove()
    
        # Mostrar únicamente el campo relacionado con el criterio seleccionado
        if criterio in campos:
            label, entry = campos[criterio]
            label.grid()
            entry.grid()
            return entry  
        return None
    

    def campos_busqueda(self, event):
        """
        Llama a la gestión de campos al seleccionar un criterio en el Combobox.
        """
        criterio = self.opciones_busqueda.get()
        self.ocultar_campos(criterio)
        
    def mostrar_todos_los_campos(self):
        """
        Muestra todos los campos de entrada y etiquetas, independientemente del criterio seleccionado.
        """
        campos = {
            "Codigo": (self.lbl_codigo, self.codigo_entry),
            "Titulo": (self.lbl_titulo, self.titulo_entry),
            "Autor": (self.lbl_autor, self.autor_entry),
            "Categoria": (self.lbl_categoria, self.categoria_entry),}
        
        for label, entry in campos.values():
            label.grid()
            entry.grid()
            
    
    def limpiar_campos(self):
        """
        Limpia los campos de entrada del formulario para gestionar libros.
        """
        self.codigo_entry.delete(0, tk.END)
        self.titulo_entry.delete(0, tk.END)
        self.autor_entry.delete(0, tk.END)
        self.categoria_entry.delete(0, tk.END)

    def salir(self):
        """
        Confirma con el usuario si desea salir de la aplicación.
        """
        
        if messagebox.askyesno("Salir", Mensaje.salir):
            self.quit()
            self.destroy()
            
    def seleccionar_registro(self, event):
        """Carga los datos del libro seleccionado en la tabla a los campos de entrada."""
        item = self.tabla.selection()
        if item:  
            valores = self.tabla.item(item, 'values')
            self.codigo_entry.delete(0, tk.END)
            self.codigo_entry.insert(0, valores[0])
            self.titulo_entry.delete(0, tk.END)
            self.titulo_entry.insert(0, valores[1])
            self.autor_entry.delete(0, tk.END)
            self.autor_entry.insert(0, valores[2])  
            self.categoria_entry.delete(0, tk.END)
            self.categoria_entry.insert(0, valores[3])

    # Funciones asociadas a las acciones del sistema
    
    def iniciar_sesion(self):
        """
        Valida las credenciales del usuario e inicia sesión si son correctas.
        """
        usuario = self.txt_usuario.get()
        contraseña = self.txt_contraseña.get()
        
        if Gestionar.iniciar_sesion(usuario, contraseña):
            # Oculta la ventana de inicio de sesion
            self.withdraw() 
            # Abre la ventana del sistema
            self.interfaz_sistema()  
        else:
            messagebox.showerror("Error", Mensaje.error_login)  


    def añadir(self):
        """Añade un libro nuevo a la base de datos si todos los datos son correctos."""
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        categoria = self.categoria_entry.get()
    
        
        Gestionar.añadir(codigo, titulo, autor, categoria)
        self.limpiar_campos()
        self.mostrar()


    def modificar(self):
        """Modifica un libro existente en la base de datos."""
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        categoria = self.categoria_entry.get()
    
        
        Gestionar.modificar(codigo, titulo, autor, categoria)
        self.limpiar_campos()
        self.mostrar()

        

    def eliminar(self):
        """Elimina un libro de la base de datos según el código."""
        codigo = self.codigo_entry.get()
        
        Gestionar.eliminar(codigo)
        self.limpiar_campos()
        self.mostrar()

    def buscar(self):
        """Busca libros según el criterio seleccionado."""
        criterio = self.opciones_busqueda.get()
        valor = ""
    
        if criterio == "Codigo":
            valor = self.codigo_entry.get()
        elif criterio == "Titulo":
            valor = self.titulo_entry.get()
        elif criterio == "Autor":
            valor = self.autor_entry.get()
        elif criterio == "Categoria":
            valor = self.categoria_entry.get()
    
       
        if valor.strip():
            Gestionar.buscar(self.tabla, criterio, valor)
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", Mensaje.buscar.format(criterio=criterio))


    def mostrar(self):
        """Muestra todos los libros almacenados en la base de datos."""
        Gestionar.mostrar(self.tabla)

    
def main():
    """
    Función principal para iniciar el programa
    """
    app = Ventana()
    app.mainloop()

if __name__ == '__main__':
    main()