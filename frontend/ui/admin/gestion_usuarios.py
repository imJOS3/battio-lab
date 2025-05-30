import tkinter as tk
from tkinter import messagebox, ttk
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

        columnas = ("ID Usuario", "ID Empleado", "Rol", "Usuario")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
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
        # Limpia tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = obtener_usuarios()
        if usuarios:
            for usuario in usuarios:
                rol_str = "Administrador" if usuario["idRol"] == 1 else "Técnico" if usuario["idRol"] == 2 else "Desconocido"
                self.tree.insert("", tk.END, values=(
                    usuario.get("idUsuario"),
                    usuario.get("idEmpleado"),
                    rol_str,
                    usuario.get("username")
                ), tags=(usuario.get("idUsuario"),))

    def crear_usuario(self):
        self.abrir_formulario_usuario()

    def modificar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para modificar.")
            return

        id_usuario = self.tree.item(seleccionado[0])["tags"][0]
        datos = obtener_usuario_por_id(id_usuario)

        if datos:
            self.abrir_formulario_usuario(datos_usuario=datos)

    def eliminar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return

        id_usuario = self.tree.item(seleccionado[0])["tags"][0]
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este usuario?"):
            if eliminar_usuario(id_usuario):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.listar_usuarios()

    def abrir_formulario_usuario(self, datos_usuario=None):
        formulario_user = tk.Toplevel(self)
        formulario_user.title("Formulario Usuario")

        # ID Empleado
        tk.Label(formulario_user, text="ID Empleado:").grid(row=0, column=0, padx=5, pady=5)
        entry_id_empleado = tk.Entry(formulario_user)
        entry_id_empleado.grid(row=0, column=1, padx=5, pady=5)

        # Usuario (username)
        tk.Label(formulario_user, text="Usuario:").grid(row=1, column=0, padx=5, pady=5)
        entry_user = tk.Entry(formulario_user)
        entry_user.grid(row=1, column=1, padx=5, pady=5)

        # Contraseña
        tk.Label(formulario_user, text="Contraseña:").grid(row=2, column=0, padx=5, pady=5)
        entry_pass = tk.Entry(formulario_user, show="*")
        entry_pass.grid(row=2, column=1, padx=5, pady=5)

        # Rol
        tk.Label(formulario_user, text="Rol:").grid(row=3, column=0, padx=5, pady=5)
        combo_rol = ttk.Combobox(formulario_user, values=["Administrador", "Técnico"], state="readonly")
        combo_rol.grid(row=3, column=1, padx=5, pady=5)

        if datos_usuario:
            entry_id_empleado.insert(0, datos_usuario.get("idEmpleado"))
            entry_user.insert(0, datos_usuario.get("username"))
            # Nota: por seguridad, no rellenamos contraseña
            rol_str = "Administrador" if datos_usuario["idRol"] == 1 else "Técnico" if datos_usuario["idRol"] == 2 else ""
            combo_rol.set(rol_str)

        def guardar_usuario():
            try:
                id_empleado = int(entry_id_empleado.get())
            except ValueError:
                messagebox.showerror("Error", "ID Empleado debe ser un número entero.")
                return

            username = entry_user.get()
            password = entry_pass.get()
            rol = combo_rol.get()

            if not (id_empleado and username and rol and (password or datos_usuario)):
                # password obligatorio solo si es creación, no en edición si no se quiere cambiar
                messagebox.showerror("Error", "Complete todos los campos. La contraseña es obligatoria al crear.")
                return

            id_rol = 1 if rol == "Administrador" else 2

            data_usuario = {
                "idEmpleado": id_empleado,
                "idRol": id_rol,
                "username": username,
            }
            if password:
                data_usuario["password"] = password

            if datos_usuario:  # edición
                actualizar_usuario(datos_usuario["idUsuario"], data_usuario)
                messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            else:
                crear_usuario(data_usuario)
                messagebox.showinfo("Éxito", "Usuario creado correctamente.")

            self.listar_usuarios()
            formulario_user.destroy()

        tk.Button(formulario_user, text="Guardar", command=guardar_usuario).grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Usuarios")
    app = GestionUsuarios(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
