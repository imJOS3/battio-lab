import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from api.users_api import (
    obtener_usuarios,
    obtener_usuario_por_id,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario
)

class GestionUsuarios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        titulo_label = tk.Label(self, text="Gestión de Usuarios", font=("Arial", 18, "bold"))
        titulo_label.pack(pady=10)

        columnas = ("Nombre", "Apellido", "Teléfono", "Estado", "Rol", "Usuario", "Contraseña")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack()

        btn_crear = tk.Button(frame_botones, text="Crear Usuario", command=self.crear_usuario)
        btn_crear.grid(row=0, column=0, padx=5)

        btn_modificar = tk.Button(frame_botones, text="Modificar Usuario", command=self.modificar_usuario)
        btn_modificar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Usuario", command=self.eliminar_usuario)
        btn_eliminar.grid(row=0, column=2, padx=5)

        self.listar_usuarios()

    def listar_usuarios(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = obtener_usuarios()
        if usuarios:
            for usuario in usuarios:
                contraseña_oculta = "*" * len(usuario["password"])
                self.tree.insert("", tk.END, values=(
                    usuario["empleado"]["nombre"],
                    usuario["empleado"]["apellido"],
                    usuario["empleado"]["numeroTel"],
                    usuario["empleado"]["estado"],
                    usuario["rol"],
                    usuario["username"],
                    contraseña_oculta
                ), tags=(usuario["idEmpleado"],))

    def crear_usuario(self):
        self.abrir_formulario_empleado()

    def modificar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para modificar.")
            return

        id_empleado = self.tree.item(seleccionado[0])["tags"][0]
        datos = obtener_usuario_por_id(id_empleado)

        if datos:
            self.abrir_formulario_empleado(datos_usuario=datos)

    def eliminar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return

        id_empleado = self.tree.item(seleccionado[0])["tags"][0]
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este usuario?"):
            if eliminar_usuario(id_empleado):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.listar_usuarios()

    def abrir_formulario_empleado(self, datos_usuario=None):
        formulario_emp = tk.Toplevel(self)
        formulario_emp.title("Formulario Empleado")

        labels = ["Nombre", "Apellido", "Correo", "Número Tel", "Dirección"]
        entries = {}
        for i, label in enumerate(labels):
            tk.Label(formulario_emp, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(formulario_emp)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entries[label.lower().replace(" ", "")] = entry

        estado_var = tk.StringVar(value="Activo")
        tk.Label(formulario_emp, text="Estado:").grid(row=5, column=0, padx=5, pady=5)
        estado_combo = ttk.Combobox(formulario_emp, textvariable=estado_var, values=["Activo", "Inactivo"], state="readonly")
        estado_combo.grid(row=5, column=1, padx=5, pady=5)

        if datos_usuario:
            emp = datos_usuario["empleado"]
            entries["nombre"].insert(0, emp["nombre"])
            entries["apellido"].insert(0, emp["apellido"])
            entries["correo"].insert(0, emp["correo"])
            entries["númerotel"].insert(0, emp["numeroTel"])
            entries["dirección"].insert(0, emp["direccion"] or "")
            estado_var.set(emp["estado"])

        def guardar_empleado():
            data_empleado = {k: e.get() for k, e in entries.items()}
            data_empleado["estado"] = estado_var.get()

            if not all(data_empleado.values()):
                messagebox.showerror("Error", "Todos los campos del empleado son obligatorios.")
                return

            if datos_usuario:
                actualizar_usuario(datos_usuario["idEmpleado"], data_empleado)
                self.listar_usuarios()
                formulario_emp.destroy()
            else:
                formulario_emp.destroy()
                self.abrir_formulario_usuario(data_empleado)

        tk.Button(formulario_emp, text="Guardar", command=guardar_empleado).grid(row=6, column=0, columnspan=2, pady=10)

    def abrir_formulario_usuario(self, data_empleado):
        formulario_user = tk.Toplevel(self)
        formulario_user.title("Formulario Usuario")

        tk.Label(formulario_user, text="Usuario:").grid(row=0, column=0, padx=5, pady=5)
        entry_user = tk.Entry(formulario_user)
        entry_user.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_user, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
        entry_pass = tk.Entry(formulario_user, show="*")
        entry_pass.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_user, text="Rol:").grid(row=2, column=0, padx=5, pady=5)
        combo_rol = ttk.Combobox(formulario_user, values=["Administrador", "Técnico"], state="readonly")
        combo_rol.grid(row=2, column=1, padx=5, pady=5)

        def guardar_usuario():
            username = entry_user.get()
            password = entry_pass.get()
            rol = combo_rol.get()

            if not (username and password and rol):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            id_rol = 1 if rol == "Administrador" else 2
            data_usuario = {
                "username": username,
                "password": password,
                "idRol": id_rol
            }

            crear_usuario(data_empleado, data_usuario)
            self.listar_usuarios()
            formulario_user.destroy()

        tk.Button(formulario_user, text="Guardar Usuario", command=guardar_usuario).grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUsuarios(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
