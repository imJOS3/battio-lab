import tkinter as tk
from tkinter import messagebox, ttk
from api.productos_api import (
    obtener_productos, crear_producto, actualizar_producto, eliminar_producto
)
import traceback

class GestionProductos(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="Gestión de Productos", font=("Arial", 18, "bold")).pack(pady=10)

        columnas = (
            "ID_Implemento", "Nombre", "Descripcion", "Categoria", "Marca",
            "Cantidad_Disponible", "Estado", "Fecha_Adquisicion", 
            "Costo_Adquisicion", "Fecha_Ultima_Inspeccion", "StockMinimo"
        )
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10, fill="x")

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=5)
        tk.Button(frame_botones, text="Crear", command=self.crear_producto).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar", command=self.modificar_producto).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_producto).grid(row=0, column=2, padx=5)

        self.listar_productos()

    def listar_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        try:
            productos = obtener_productos()
            for p in productos:
                self.tree.insert("", tk.END, values=tuple(p[col] for col in self.tree["columns"]), tags=(p["ID_Implemento"],))
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Error", f"No se pudo cargar la lista de productos.\n{str(e)}")

    def crear_producto(self):
        self.abrir_formulario_producto()

    def modificar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto.")
            return
        datos = self.tree.item(seleccionado[0])["values"]
        self.abrir_formulario_producto(dict(zip(self.tree["columns"], datos)))

    def eliminar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto.")
            return
        codigo = self.tree.item(seleccionado[0], 'values')[0]
        if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
            try:
                if eliminar_producto(codigo):
                    messagebox.showinfo("Éxito", "Producto eliminado.")
                    self.listar_productos()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto.")
            except Exception as e:
                traceback.print_exc()
                messagebox.showerror("Error", f"Ocurrió un error al eliminar el producto:\n{str(e)}")

    def abrir_formulario_producto(self, datos=None):
        form = tk.Toplevel(self)
        form.title("Formulario Producto")

        entries = {}
        for i, campo in enumerate(self.tree["columns"]):
            tk.Label(form, text=campo + ":").grid(row=i, column=0, padx=5, pady=5)
            e = tk.Entry(form)
            e.grid(row=i, column=1, padx=5, pady=5)
            if datos:
                e.insert(0, datos[campo])
            entries[campo] = e

        def guardar():
            data = {k: v.get() for k, v in entries.items()}
            if any(not v for v in data.values()):
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return
            try:
                if datos:
                    actualizar_producto(data["ID_Implemento"], data)
                else:
                    crear_producto(data)
                self.listar_productos()
                messagebox.showinfo("Éxito", "Producto guardado.")
                form.destroy()
            except Exception as e:
                traceback.print_exc()
                messagebox.showerror("Error", f"Ocurrió un error al guardar el producto:\n{str(e)}")

        tk.Button(form, text="Guardar", command=guardar).grid(row=len(entries), columnspan=2, pady=10)
