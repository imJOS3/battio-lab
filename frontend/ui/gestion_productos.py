import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

class GestionProductos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Título
        titulo_label = tk.Label(self, text="Gestión de Productos", font=("Arial", 18, "bold"))
        titulo_label.pack(pady=10)

        # Conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="batio_lab"
        )
        self.cursor = self.conexion.cursor(dictionary=True)

        # Definir columnas de la tabla
        columnas = ("Código", "Nombre", "Descripción", "Stock", "Precio", "Estado")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10)

        # Botones de acción
        frame_botones = tk.Frame(self)
        frame_botones.pack()

        btn_crear = tk.Button(frame_botones, text="Crear Producto", command=self.crear_producto)
        btn_crear.grid(row=0, column=0, padx=5)

        btn_modificar = tk.Button(frame_botones, text="Modificar Producto", command=self.modificar_producto)
        btn_modificar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Producto", command=self.eliminar_producto)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # Listar productos
        self.listar_productos()

    def listar_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        consulta = "SELECT * FROM productos"
        self.cursor.execute(consulta)
        for row in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=(
                row["ID_Implemento"],
                row["Nombre"],
                row["Descripcion"],
                row["Cantidad_Disponible"],
                row["Costo_Adquisicion"],
                row["Estado"]
            ), tags=(row["ID_Implemento"],))

    def crear_producto(self):
        self.abrir_formulario_producto()

    def modificar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para modificar.")
            return

        item = self.tree.item(seleccionado[0])
        codigo_producto = item["tags"][0]

        self.cursor.execute("SELECT * FROM productos WHERE ID_Implemento = %s", (codigo_producto,))
        datos_producto = self.cursor.fetchone()

        if datos_producto:
            self.abrir_formulario_producto(datos_producto)

    def eliminar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este producto?")
        if respuesta:
            codigo_producto = self.tree.item(seleccionado[0], 'values')[0]

            try:
                self.cursor.execute("DELETE FROM productos WHERE ID_Implemento = %s", (codigo_producto,))
                self.conexion.commit()

                self.listar_productos()
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al eliminar el producto: {e}")

    def abrir_formulario_producto(self, datos_producto=None):
        formulario_prod = tk.Toplevel(self)
        formulario_prod.title("Formulario Producto")

        # Campos del formulario
        tk.Label(formulario_prod, text="Código:").grid(row=0, column=0, padx=5, pady=5)
        entry_codigo = tk.Entry(formulario_prod)
        entry_codigo.grid(row=0, column=1, padx=5, pady=5)
        if datos_producto:
            entry_codigo.insert(0, datos_producto["ID_Implemento"])

        tk.Label(formulario_prod, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_prod)
        entry_nombre.grid(row=1, column=1, padx=5, pady=5)
        if datos_producto:
            entry_nombre.insert(0, datos_producto["Nombre"])

        tk.Label(formulario_prod, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        entry_descripcion = tk.Entry(formulario_prod)
        entry_descripcion.grid(row=2, column=1, padx=5, pady=5)
        if datos_producto:
            entry_descripcion.insert(0, datos_producto["Descripcion"])

        tk.Label(formulario_prod, text="Stock:").grid(row=3, column=0, padx=5, pady=5)
        entry_stock = tk.Entry(formulario_prod)
        entry_stock.grid(row=3, column=1, padx=5, pady=5)
        if datos_producto:
            entry_stock.insert(0, datos_producto["Cantidad_Disponible"])

        tk.Label(formulario_prod, text="Precio:").grid(row=4, column=0, padx=5, pady=5)
        entry_precio = tk.Entry(formulario_prod)
        entry_precio.grid(row=4, column=1, padx=5, pady=5)
        if datos_producto:
            entry_precio.insert(0, datos_producto["Costo_Adquisicion"])

        tk.Label(formulario_prod, text="Estado:").grid(row=5, column=0, padx=5, pady=5)
        entry_estado = tk.Entry(formulario_prod)
        entry_estado.grid(row=5, column=1, padx=5, pady=5)
        if datos_producto:
            entry_estado.insert(0, datos_producto["Estado"])

        # Botón de Guardar
        def guardar_producto():
            codigo = entry_codigo.get()
            nombre = entry_nombre.get()
            descripcion = entry_descripcion.get()
            stock = entry_stock.get()
            precio = entry_precio.get()
            estado = entry_estado.get()

            if not (codigo and nombre and descripcion and stock and precio and estado):
                messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
                return

            try:
                if datos_producto:  # Modificar producto
                    self.cursor.execute("""
                        UPDATE productos
                        SET Nombre = %s, Descripcion = %s, Cantidad_Disponible = %s, Costo_Adquisicion = %s, Estado = %s
                        WHERE ID_Implemento = %s
                    """, (nombre, descripcion, stock, precio, estado, codigo))
                else:  # Crear nuevo producto
                    self.cursor.execute("""
                        INSERT INTO productos (ID_Implemento, Nombre, Descripcion, Cantidad_Disponible, Costo_Adquisicion, Estado)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (codigo, nombre, descripcion, stock, precio, estado))

                self.conexion.commit()
                messagebox.showinfo("Éxito", "Producto guardado correctamente.")
                self.listar_productos()
                formulario_prod.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al guardar el producto: {e}")

        btn_guardar = tk.Button(formulario_prod, text="Guardar Producto", command=guardar_producto)
        btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)
