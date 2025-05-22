import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from datetime import date

class GestionUsuarios(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        titulo_label = tk.Label(self, text="Gestión de Usuarios", font=("Arial", 18, "bold"))
        titulo_label.pack(pady=10)

        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            #database="batio_lab"
            database="battiolab"
        )
        self.cursor = self.conexion.cursor(dictionary=True)

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

        consulta = """
            SELECT e.idEmpleados, e.nombre, e.apellido, e.numeroTel, e.estado, r.nombreRol, u.username, u.password
            FROM users u
            JOIN empleados e ON u.idEmpleado = e.idEmpleados
            JOIN roles r ON u.idRol = r.idRol
        """
        self.cursor.execute(consulta)
        for row in self.cursor.fetchall():
            contraseña_oculta = "*" * len(row["password"]) if row["password"] else ""
            self.tree.insert("", tk.END, values=(
                row["nombre"],
                row["apellido"],
                row["numeroTel"],
                row["estado"],
                row["nombreRol"],
                row["username"],
                contraseña_oculta
            ), tags=(row["idEmpleados"],))

    def crear_usuario(self):
        self.abrir_formulario_empleado()

    def modificar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para modificar.")
            return

        item = self.tree.item(seleccionado[0])
        id_empleado = item["tags"][0]

        self.cursor.execute("SELECT * FROM empleados WHERE idEmpleados = %s", (id_empleado,))
        datos_empleado = self.cursor.fetchone()

        if datos_empleado:
            self.abrir_formulario_empleado(datos_empleado)

    def eliminar_usuario(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este usuario?")
        if respuesta:
            # Obtener el username y el idEmpleados de la interfaz
            username = self.tree.item(seleccionado[0], 'values')[5]
            idEmpleados = self.tree.item(seleccionado[0], 'tags')[0]  # Usamos los 'tags' para obtener el id

            try:
                # Eliminar el usuario de la tabla 'users'
                self.cursor.execute("DELETE FROM users WHERE username = %s", (username,))
                # Eliminar el usuario de la tabla 'empleados'
                self.cursor.execute("DELETE FROM empleados WHERE idEmpleados = %s", (idEmpleados,))

                # Confirmar cambios en la base de datos
                self.conexion.commit()

                # Refrescar la lista de usuarios en la interfaz
                self.listar_usuarios()
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Se produjo un error al eliminar el usuario: {e}")

    def abrir_formulario_empleado(self, datos_usuario=None):
        formulario_emp = tk.Toplevel(self)
        formulario_emp.title("Formulario Empleado")

        # Campos
        tk.Label(formulario_emp, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(formulario_emp)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario_emp, text="Apellido:").grid(row=1, column=0, padx=5, pady=5)
        entry_apellido = tk.Entry(formulario_emp)
        entry_apellido.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(formulario_emp, text="Correo:").grid(row=2, column=0, padx=5, pady=5)
        entry_correo = tk.Entry(formulario_emp)
        entry_correo.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(formulario_emp, text="Número Tel:").grid(row=3, column=0, padx=5, pady=5)
        entry_tel = tk.Entry(formulario_emp)
        entry_tel.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(formulario_emp, text="Dirección:").grid(row=4, column=0, padx=5, pady=5)
        entry_direccion = tk.Entry(formulario_emp)
        entry_direccion.grid(row=4, column=1, padx=5, pady=5)

        estado_var = tk.StringVar()
        estado_var.set("Activo")
        tk.Label(formulario_emp, text="Estado:").grid(row=5, column=0, padx=5, pady=5)
        estado_combo = ttk.Combobox(formulario_emp, textvariable=estado_var, values=["Activo", "Inactivo"], state="readonly")
        estado_combo.grid(row=5, column=1, padx=5, pady=5)

        if datos_usuario:
            entry_nombre.insert(0, datos_usuario["nombre"])
            entry_apellido.insert(0, datos_usuario["apellido"])
            entry_correo.insert(0, datos_usuario["correo"])
            entry_tel.insert(0, datos_usuario["numeroTel"])
            entry_direccion.insert(0, datos_usuario["direccion"] if datos_usuario["direccion"] else "")
            estado_var.set(datos_usuario["estado"])

        def guardar_empleado():
            nombre = entry_nombre.get()
            apellido = entry_apellido.get()
            correo = entry_correo.get()
            numeroTel = entry_tel.get()
            direccion = entry_direccion.get()
            estado = estado_var.get()

            if not (nombre and apellido and correo and numeroTel and direccion and estado):
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if datos_usuario:
                # Modificar existente
                id_empleado = datos_usuario["idEmpleados"]
                if estado == "Inactivo" and datos_usuario["estado"] != "Inactivo":
                    fecha_salida = date.today()
                    self.cursor.execute(""" 
                        UPDATE empleados
                        SET nombre=%s, apellido=%s, correo=%s, numeroTel=%s, direccion=%s, estado=%s, fechaSalida=%s
                        WHERE idEmpleados=%s
                    """, (nombre, apellido, correo, numeroTel, direccion, estado, fecha_salida, id_empleado))
                else:
                    self.cursor.execute("""
                        UPDATE empleados
                        SET nombre=%s, apellido=%s, correo=%s, numeroTel=%s, direccion=%s, estado=%s
                        WHERE idEmpleados=%s
                    """, (nombre, apellido, correo, numeroTel, direccion, estado, id_empleado))
                self.conexion.commit()
                formulario_emp.destroy()
                self.listar_usuarios()

            else:
                # Crear nuevo
                self.cursor.execute("""
                    INSERT INTO empleados (nombre, apellido, correo, numeroTel, direccion, fechaIngreso, estado)
                    VALUES (%s, %s, %s, %s, %s, CURDATE(), %s)
                """, (nombre, apellido, correo, numeroTel, direccion, estado))
                self.conexion.commit()
                id_empleado = self.cursor.lastrowid
                formulario_emp.destroy()
                self.abrir_formulario_usuario(id_empleado)

        btn_guardar_emp = tk.Button(formulario_emp, text="Guardar", command=guardar_empleado)
        btn_guardar_emp.grid(row=6, column=0, columnspan=2, pady=10)

    def abrir_formulario_usuario(self, id_empleado):
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

            self.cursor.execute("""
                INSERT INTO users (idEmpleado, idRol, username, password)
                VALUES (%s, %s, %s, %s)
            """, (id_empleado, id_rol, username, password))
            self.conexion.commit()

            formulario_user.destroy()
            self.listar_usuarios()

        btn_guardar_user = tk.Button(formulario_user, text="Guardar Usuario", command=guardar_usuario)
        btn_guardar_user.grid(row=3, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionUsuarios(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
