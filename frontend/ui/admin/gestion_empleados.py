import tkinter as tk
from tkinter import ttk, messagebox
from api import empleados_api

class GestionEmpleados(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="Gestión de Empleados", font=("Arial", 18, "bold")).pack(pady=10)

        columnas = ("ID", "Nombre", "Apellido", "Correo", "Teléfono", "Dirección", "Ingreso", "Salida", "Estado")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10, fill="both", expand=True)

        # Botones
        frame_btn = tk.Frame(self)
        frame_btn.pack(pady=10)
        tk.Button(frame_btn, text="Crear", command=self.crear_empleado).grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="Modificar", command=self.modificar_empleado).grid(row=0, column=1, padx=5)
        tk.Button(frame_btn, text="Eliminar", command=self.eliminar_empleado).grid(row=0, column=2, padx=5)

        self.cargar_empleados()

    def cargar_empleados(self):
        try:
            self.tree.delete(*self.tree.get_children())
            empleados = empleados_api.obtener_empleados()
            for e in empleados:
                self.tree.insert("", tk.END, values=(
                    e["idEmpleados"], e["nombre"], e["apellido"], e["correo"], e["numeroTel"],
                    e["direccion"], e["fechaIngreso"], e["fechaSalida"], e["estado"]
                ))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def crear_empleado(self):
        self.formulario_empleado()

    def modificar_empleado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un empleado")
            return

        datos = self.tree.item(seleccion[0], "values")
        self.formulario_empleado(datos)

    def eliminar_empleado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un empleado")
            return

        datos = self.tree.item(seleccion[0], "values")
        id_empleado = datos[0]

        if messagebox.askyesno("Confirmación", "¿Eliminar este empleado?"):
            try:
                if empleados_api.eliminar_empleado(id_empleado):
                    messagebox.showinfo("Éxito", "Empleado eliminado")
                    self.cargar_empleados()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def formulario_empleado(self, datos=None):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Empleado")

        campos = [
            "Nombre", "Apellido", "Correo", "Teléfono",
            "Dirección", "Ingreso", "Salida", "Estado"
        ]
        entradas = {}
        for idx, campo in enumerate(campos):
            tk.Label(ventana, text=campo + ":").grid(row=idx, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(ventana)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            entradas[campo] = entry

        if datos:
            for i, campo in enumerate(campos):
                entradas[campo].insert(0, datos[i + 1])  # +1 porque el primer dato es el ID

        def guardar():
            data = {
                "nombre": entradas["Nombre"].get(),
                "apellido": entradas["Apellido"].get(),
                "correo": entradas["Correo"].get(),
                "numeroTel": entradas["Teléfono"].get(),
                "direccion": entradas["Dirección"].get(),
                "fechaIngreso": entradas["Ingreso"].get(),
                "fechaSalida": entradas["Salida"].get(),
                "estado": entradas["Estado"].get(),
            }

            try:
                if datos:
                    id_empleado = datos[0]
                    empleados_api.actualizar_empleado(id_empleado, data)
                    messagebox.showinfo("Éxito", "Empleado modificado")
                else:
                    empleados_api.crear_empleado(data)
                    messagebox.showinfo("Éxito", "Empleado creado")

                ventana.destroy()
                self.cargar_empleados()

            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=len(campos), columnspan=2, pady=10)
