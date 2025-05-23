import tkinter as tk
from tkinter import messagebox, font as tkfont
import requests

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BATTIO LAB")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f2f2")

        self.title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        self.label_font = tkfont.Font(family="Arial", size=12)
        self.entry_font = tkfont.Font(family="Arial", size=12)

        self.frame = tk.Frame(root, bg="white", padx=30, pady=30)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title = tk.Label(self.frame, text="Iniciar sesión", font=self.title_font, bg="white", fg="#333")
        self.title.pack(pady=(0, 20))

        tk.Label(self.frame, text="Usuario", font=self.label_font, bg="white", anchor="w").pack(fill="x")
        self.entry_user = tk.Entry(self.frame, font=self.entry_font, bd=1, relief="solid")
        self.entry_user.pack(fill="x", pady=(0, 15))

        tk.Label(self.frame, text="Contraseña", font=self.label_font, bg="white", anchor="w").pack(fill="x")
        self.entry_pass = tk.Entry(self.frame, font=self.entry_font, show="*", bd=1, relief="solid")
        self.entry_pass.pack(fill="x", pady=(0, 25))

        self.login_btn = tk.Button(self.frame, text="Iniciar sesión", font=self.label_font,
                                   command=self.login, bg="#4CAF50", fg="white", activebackground="#45a049")
        self.login_btn.pack(fill="x")

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
                id_rol = result.get("idRol")

                messagebox.showinfo("Éxito", "Inicio de sesión exitoso.")
                self.root.destroy()

                if id_rol == 1:
                    self.open_admin_panel()
                elif id_rol == 2:
                    messagebox.showinfo("Redirección", "Aquí irá el panel del técnico.")
                else:
                    messagebox.showerror("Error", "Rol no reconocido.")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "No se pudo conectar con el servidor.")

    def open_admin_panel(self):
        import ui.admin.admin_panel as admin_panel
        root = tk.Tk()
        admin_panel.AdminPanel(root, run_login)
        root.mainloop()


def run_login():
    root = tk.Tk()

    # Tamaño de la ventana
    window_width = 400
    window_height = 400

    # Obtener tamaño de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular coordenadas para centrar
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Posicionar la ventana centrada
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = LoginApp(root)
    root.mainloop()

