import tkinter as tk
from tkinter import messagebox, ttk
import api.precio_mano_obra_api as precio_mano_obra_api

class GestionPrecioManoDeObra(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Gestión de Precios Mano de Obra", font=("Arial", 18, "bold")).pack(pady=10)

        columnas = ("Tipo Servicio", "Precio Base")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)
        self.tree.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack()
        tk.Button(frame_botones, text="Crear", command=self.crear_precio).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar", command=self.modificar_precio).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_precio).grid(row=0, column=2, padx=5)

        self.listar_precios()

    def listar_precios(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        precios = precio_mano_obra_api.obtener_precios()
        for p in precios:
            self.tree.insert("", tk.END, values=(p["tipoServicio"], p["precioBase"]), tags=(p["tipoServicio"],))

    def crear_precio(self):
        self.abrir_formulario()

    def modificar_precio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un tipo de servicio.")
            return
        tipo = self.tree.item(seleccionado[0])["tags"][0]
        precio = precio_mano_obra_api.obtener_precio_por_tipo(tipo)
        self.abrir_formulario(precio)

    def eliminar_precio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un tipo de servicio.")
            return
        tipo = self.tree.item(seleccionado[0])["tags"][0]
        if messagebox.askyesno("Confirmar", f"¿Eliminar el precio de '{tipo}'?"):
            precio_mano_obra_api.eliminar_precio(tipo)
            self.listar_precios()
            messagebox.showinfo("Éxito", "Registro eliminado.")

    def abrir_formulario(self, precio=None):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Precio Mano de Obra")

        tk.Label(ventana, text="Tipo Servicio:").grid(row=0, column=0, padx=5, pady=5)
        entry_tipo = tk.Entry(ventana)
        entry_tipo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(ventana, text="Precio Base:").grid(row=1, column=0, padx=5, pady=5)
        entry_precio = tk.Entry(ventana)
        entry_precio.grid(row=1, column=1, padx=5, pady=5)

        if precio:
            entry_tipo.insert(0, precio["tipoServicio"])
            entry_tipo.config(state="disabled")
            entry_precio.insert(0, precio["precioBase"])

        def guardar():
            tipo = entry_tipo.get().strip()
            precio_base = entry_precio.get().strip()
            if not tipo or not precio_base:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return
            data = {"tipoServicio": tipo, "precioBase": precio_base}
            if precio:
                precio_mano_obra_api.modificar_precio(data)
            else:
                precio_mano_obra_api.crear_precio(data)
            self.listar_precios()
            ventana.destroy()
            messagebox.showinfo("Éxito", "Registro guardado correctamente.")

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=2, columnspan=2, pady=10)
