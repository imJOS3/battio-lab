import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import traceback
from api.productos_api import (
    obtener_productos, crear_producto, actualizar_producto, eliminar_producto
)

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
                valores = []
                for col in self.tree["columns"]:
                    val = p[col]
                    if isinstance(val, bool):
                        val = "Sí" if val else "No"
                    elif "Fecha" in col and val:
                        val = val.split("T")[0]  # Ajustar si vienen con tiempo
                    valores.append(val)
                self.tree.insert("", tk.END, values=tuple(valores), tags=(p["ID_Implemento"],))
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
        # Mapear los datos a columnas
        datos_dict = dict(zip(self.tree["columns"], datos))
        # Convertir "Sí"/"No" a bool para Estado
        if "Estado" in datos_dict:
            datos_dict["Estado"] = True if datos_dict["Estado"] == "Sí" else False
        self.abrir_formulario_producto(datos_dict)

    def eliminar_producto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un producto.")
            return
        codigo = self.tree.item(seleccionado[0], 'values')[0]
        if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):
            try:
                if eliminar_producto(int(codigo)):
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

            if campo == "Estado":
                var_estado = tk.BooleanVar(value=datos[campo] if datos else False)
                chk = tk.Checkbutton(form, variable=var_estado)
                chk.grid(row=i, column=1, padx=5, pady=5)
                entries[campo] = var_estado
            else:
                e = tk.Entry(form)
                e.grid(row=i, column=1, padx=5, pady=5)
                if datos:
                    e.insert(0, datos[campo])
                    if campo == "ID_Implemento":
                        e.configure(state="disabled")
                entries[campo] = e

        def guardar():
            try:
                data = {}
                for k, widget in entries.items():
                    if isinstance(widget, tk.BooleanVar):
                        data[k] = widget.get()
                    else:
                        val = widget.get()
                        if not val:
                            raise ValueError(f"El campo '{k}' no puede estar vacío.")
                        if k in ["Cantidad_Disponible", "StockMinimo"]:
                            data[k] = int(val)
                        elif k == "ID_Implemento":
                            # Si está deshabilitado (modificar), igual convertir a int
                            data[k] = int(val)
                        elif k == "Costo_Adquisicion":
                            data[k] = float(val)
                        elif k in ["Fecha_Adquisicion", "Fecha_Ultima_Inspeccion"]:
                            # Validar formato fecha yyyy-mm-dd
                            try:
                                datetime.strptime(val, "%Y-%m-%d")
                                data[k] = val
                            except ValueError:
                                raise ValueError(f"El campo '{k}' debe tener formato AAAA-MM-DD.")
                        else:
                            data[k] = val

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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión Productos")
    root.geometry("1300x500")
    app = GestionProductos(root)
    app.pack(expand=True, fill="both")
    root.mainloop()
