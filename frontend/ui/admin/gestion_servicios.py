import tkinter as tk
from tkinter import messagebox, ttk
import api.servicios_api as servicios_api

class GestionServicios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="Gestión de Servicios", font=("Arial", 18, "bold")).pack(pady=10)

        columnas = ("ID Servicio", "ID Cliente", "ID Empleado", "Tipo Servicio", "Fecha Ingreso", "Fecha Entrega", "Observaciones")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack()
        tk.Button(frame_botones, text="Crear", command=self.crear_servicio).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar", command=self.modificar_servicio).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_servicio).grid(row=0, column=2, padx=5)

        self.listar_servicios()

    def listar_servicios(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            servicios = servicios_api.obtener_servicios()
            for s in servicios:
                self.tree.insert("", tk.END, values=(
                    s["idServicio"], s["idCliente"], s["idEmpleado"], s["tipoServicio"],
                    s["fechaIngreso"], s["fechaEntrega"], s["observaciones"]
                ), tags=(s["idServicio"],))
        except Exception as e:
            print(f"Error al obtener servicios: {e}")
            messagebox.showwarning("Advertencia", "No se pudieron cargar los servicios.")

    def crear_servicio(self):
        self.abrir_formulario_servicio()

    def modificar_servicio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un servicio.")
            return

        id_servicio = self.tree.item(seleccionado[0])["tags"][0]
        try:
            servicio = servicios_api.obtener_servicio_por_id(id_servicio)
            if not servicio:
                raise ValueError("Servicio no encontrado.")
            self.abrir_formulario_servicio(servicio)
        except Exception as e:
            print(f"Error al obtener servicio: {e}")
            messagebox.showerror("Error", "No se pudo obtener la información del servicio.")

    def eliminar_servicio(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un servicio.")
            return

        id_servicio = self.tree.item(seleccionado[0])["tags"][0]
        if messagebox.askyesno("Confirmar", "¿Desea eliminar este servicio?"):
            try:
                servicios_api.eliminar_servicio(id_servicio)
                self.listar_servicios()
                messagebox.showinfo("Éxito", "Servicio eliminado correctamente.")
            except Exception as e:
                print(f"Error al eliminar servicio: {e}")
                messagebox.showerror("Error", "No se pudo eliminar el servicio.")

    def abrir_formulario_servicio(self, servicio=None):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Servicio")

        campos = ["idServicio", "idCliente", "idEmpleado", "tipoServicio", "fechaIngreso", "fechaEntrega", "observaciones"]
        entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(ventana, text=f"{campo}:").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(ventana)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            if servicio:
                entrada.insert(0, servicio.get(campo, ""))
                if campo == "idServicio":
                    entrada.config(state="disabled")
            entradas[campo] = entrada

        def guardar():
            datos = {campo: entrada.get() for campo, entrada in entradas.items()}
            if any(not valor.strip() for valor in datos.values()):
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return

            try:
                if servicio:
                    servicios_api.modificar_servicio(datos)
                    messagebox.showinfo("Éxito", "Servicio actualizado correctamente.")
                else:
                    servicios_api.crear_servicio(datos)
                    messagebox.showinfo("Éxito", "Servicio creado correctamente.")
                self.listar_servicios()
                ventana.destroy()
            except Exception as e:
                print(f"Error al guardar servicio: {e}")
                messagebox.showerror("Error", "No se pudo guardar el servicio.")

        tk.Button(ventana, text="Guardar", command=guardar).grid(row=len(campos), columnspan=2, pady=10)
