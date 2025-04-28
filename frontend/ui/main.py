import tkinter as tk
from tkinter import messagebox, font as tkfont
import requests

from admin_panel import AdminPanel  # 👈 Importación del panel de administración

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BATTIO LAB")
        self.root.configure(bg="#7af40d")
        self.root.state('zoomed')  # Pantalla completa

        # Fuente personalizada
        self.custom_font = tkfont.Font(family="Helvetica", size=16)
        self.title_font = tkfont.Font(family="Helvetica", size=28, weight="bold")

        # Contenedor central
        frame = tk.Frame(root, bg="#7af40d")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título estilizado
        tk.Label(frame, text="BATTIO LAB", font=self.title_font, bg="#7af40d", fg="black").pack(pady=(0, 30))

        # Etiqueta y entrada de usuario
        tk.Label(frame, text="Usuario:", font=self.custom_font, bg="#7af40d", fg="black").pack(pady=5)
        self.entry_user = tk.Entry(frame, font=self.custom_font, width=25)
        self.entry_user.pack(pady=5)

        # Etiqueta y entrada de contraseña
        tk.Label(frame, text="Contraseña:", font=self.custom_font, bg="#7af40d", fg="black").pack(pady=5)
        self.entry_pass = tk.Entry(frame, show="*", font=self.custom_font, width=25)
        self.entry_pass.pack(pady=5)

        # Botón de inicio de sesión
        tk.Button(frame, text="Iniciar sesión", font=self.custom_font, command=self.login, bg="black", fg="white", width=20).pack(pady=30)

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        if not username or not password:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")
            return

        url = "http://127.0.0.1:5000/auth/login"
        data = {"username": username, "password": password}

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                result = response.json()
                token = result.get("access_token")
                id_rol = result.get("idRol")

                messagebox.showinfo("Éxito", f"Inicio de sesión exitoso.")

                self.root.destroy()  # Cierra la ventana de login

                if id_rol == 1:
                    open_admin_panel()
                elif id_rol == 2:
                    messagebox.showinfo("Redirección", "Aquí irá el panel del técnico.")
                    # Aquí puedes invocar otra función como open_technician_panel()
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor.")

# Función para abrir el Panel de Administración
def open_admin_panel():
    root = tk.Tk()
    app = AdminPanel(root, return_to_login)
    root.mainloop()

# Función para volver al login desde el panel
def return_to_login():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
