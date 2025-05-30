import tkinter as tk
from tkinter import ttk, messagebox
from api.clientes_api import (
    obtener_clientes,
    obtener_cliente_por_id,
    crear_cliente,
    modificar_cliente,
    eliminar_cliente
)

class GestionClientes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="Gestión de Clientes", font=("Arial", 18, "bold")).pack(pady=10)

        columnas = ("Nombre", "Apellido", "Correo", "Teléfono", "Dirección", "Estado")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack()

        tk.Button(frame_botones, text="Crear Cliente", command=self.crear_cliente).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Modificar Cliente", command=self.modificar_cliente).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar Cliente", command=self.eliminar_cliente).grid(row=0, column=2, padx=5)

        self.listar_clientes()

    def listar_clientes(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            clientes = obtener_clientes()
            for c in clientes:
                estado_str = "Activo" if c["estado"] else "Inactivo"
                self.tree.insert("", tk.END, values=(
                    c["nombre"],
                    c["apellido"],
                    c["correo"],
                    c["telefono"],
                    c["direccion"],
                    estado_str
                ), tags=(c["idCliente"],))
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            messagebox.showwarning("Advertencia", "No se pudieron cargar los clientes.")

    def crear_cliente(self):
        self.abrir_formulario_cliente()

    def modificar_cliente(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente.")
            return

        id_cliente = self.tree.item(seleccionado[0])["tags"][0]
        cliente = obtener_cliente_por_id(id_cliente)
        self.abrir_formulario_cliente(cliente)

    def eliminar_cliente(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un cliente.")
            return

        id_cliente = self.tree.item(seleccionado[0])["tags"][0]
        if messagebox.askyesno("Confirmar", "¿Desea eliminar este cliente?"):
            eliminar_cliente(id_cliente)
            self.listar_clientes()
            messagebox.showinfo("Éxito", "Cliente eliminado correctamente.")

    def abrir_formulario_cliente(self, cliente=None):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Cliente")

        campos = ["nombre", "apellido", "correo", "telefono", "direccion"]
        entradas = {}

        for i, campo in enumerate(campos):
            tk.Label(ventana, text=f"{campo.capitalize()}:").grid(row=i, column=0, padx=5, pady=5)
            entrada = tk.Entry(ventana)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            if cliente:
                entrada.insert(0, cliente.get(campo, ""))
            entradas[campo] = entrada

        estado_var = tk.StringVar(value="Activo" if (cliente and cliente["estado"]) else "Inactivo")
        tk.Label(ventana, text="Estado:").grid(row=len(campos), column=0, padx=5, pady=5)
        estado_combo = ttk.Combobox(ventana, textvariable=estado_var, values=["Activo", "Inactivo"], state="readonly")
        estado_combo.grid(row=len(campos), column=1, padx=5, pady=5)

        def guardar_cliente():
            datos = {k: entradas[k].get() for k in entradas}
            datos["estado"] = True if estado_var.get() == "Activo" else False

            if any(not v for v in datos.values()):
                messagebox.showwarning("Advertencia", "Complete todos los campos.")
                return

            try:
                if cliente:
                    modificar_cliente(cliente["idCliente"], datos)
                    messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")
                else:
                    crear_cliente(datos)
                    messagebox.showinfo("Éxito", "Cliente creado correctamente.")
                self.listar_clientes()
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Guardar", command=guardar_cliente).grid(row=len(campos)+1, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionClientes(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
